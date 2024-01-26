# pylint:disable=missing-class-docstring
from typing import Union, Type, Callable, Set, Dict, Optional, Tuple, List, DefaultDict
import itertools
import enum
from collections import defaultdict
import logging

import networkx

from .typevars import (
    Existence,
    Subtype,
    TypeVariable,
    DerivedTypeVariable,
    HasField,
    IsArray,
    TypeConstraint,
    Load,
    Store,
    BaseLabel,
    FuncIn,
    FuncOut,
)
from .typeconsts import (
    BottomType,
    TopType,
    TypeConstant,
    Int,
    Int8,
    Int16,
    Int32,
    Int64,
    Pointer,
    Pointer32,
    Pointer64,
    Struct,
    Function,
)
from .variance import Variance
from .dfa import DFAConstraintSolver

_l = logging.getLogger(__name__)


PRIMITIVE_TYPES = {TopType(), Int(), Int8(), Int16(), Int32(), Int64(), Pointer32(), Pointer64(), BottomType()}

Top_ = TopType()
Int_ = Int()
Int64_ = Int64()
Int32_ = Int32()
Int16_ = Int16()
Int8_ = Int8()
Bottom_ = BottomType()
Pointer64_ = Pointer64()
Pointer32_ = Pointer32()

# lattice for 64-bit binaries
BASE_LATTICE_64 = networkx.DiGraph()
BASE_LATTICE_64.add_edge(Top_, Int_)
BASE_LATTICE_64.add_edge(Int_, Int64_)
BASE_LATTICE_64.add_edge(Int_, Int32_)
BASE_LATTICE_64.add_edge(Int_, Int16_)
BASE_LATTICE_64.add_edge(Int_, Int8_)
BASE_LATTICE_64.add_edge(Int32_, Bottom_)
BASE_LATTICE_64.add_edge(Int16_, Bottom_)
BASE_LATTICE_64.add_edge(Int8_, Bottom_)
BASE_LATTICE_64.add_edge(Int64_, Pointer64_)
BASE_LATTICE_64.add_edge(Pointer64_, Bottom_)

# lattice for 32-bit binaries
BASE_LATTICE_32 = networkx.DiGraph()
BASE_LATTICE_32.add_edge(Top_, Int_)
BASE_LATTICE_32.add_edge(Int_, Int64_)
BASE_LATTICE_32.add_edge(Int_, Int32_)
BASE_LATTICE_32.add_edge(Int_, Int16_)
BASE_LATTICE_32.add_edge(Int_, Int8_)
BASE_LATTICE_32.add_edge(Int32_, Pointer32_)
BASE_LATTICE_32.add_edge(Int64_, Bottom_)
BASE_LATTICE_32.add_edge(Pointer32_, Bottom_)
BASE_LATTICE_32.add_edge(Int16_, Bottom_)
BASE_LATTICE_32.add_edge(Int8_, Bottom_)

BASE_LATTICES = {
    32: BASE_LATTICE_32,
    64: BASE_LATTICE_64,
}


#
# Sketch
#


class SketchNodeBase:
    """
    The base class for nodes in a sketch.
    """

    __slots__ = ()


class SketchNode(SketchNodeBase):
    """
    Represents a node in a sketch graph.
    """

    __slots__ = ("typevar", "upper_bound", "lower_bound")

    def __init__(self, typevar: Union[TypeVariable, DerivedTypeVariable]):
        self.typevar: Union[TypeVariable, DerivedTypeVariable] = typevar
        self.upper_bound = TopType()
        self.lower_bound = BottomType()

    def __repr__(self):
        return f"{self.lower_bound} <: {self.typevar} <: {self.upper_bound}"


_ref_node_ctr = itertools.count()


class RecursiveRefNode(SketchNodeBase):
    """
    Represents a cycle in a sketch graph.

    This is equivalent to sketches.LabelNode in the reference implementation of retypd.
    """

    def __init__(self, target: DerivedTypeVariable):
        self.target: DerivedTypeVariable = target
        self.idx: int = next(_ref_node_ctr)

    def __hash__(self):
        return hash((RecursiveRefNode, self.idx))

    def __eq__(self, other):
        return type(other) is RecursiveRefNode and other.target is self.target and other.idx == self.idx


class Sketch:
    """
    Describes the sketch of a type variable.
    """

    __slots__ = (
        "graph",
        "root",
        "node_mapping",
        "solver",
    )

    def __init__(self, solver: "SimpleSolver", root: TypeVariable):
        self.root: SketchNode = SketchNode(root)
        self.graph = networkx.DiGraph()
        self.node_mapping: Dict[Union[TypeVariable, DerivedTypeVariable], SketchNodeBase] = {}
        self.solver = solver

        # add the root node
        self.graph.add_node(self.root)
        self.node_mapping[root] = self.root

    def lookup(self, typevar: Union[TypeVariable, DerivedTypeVariable]) -> Optional[SketchNodeBase]:
        if typevar in self.node_mapping:
            return self.node_mapping[typevar]
        node = None
        if isinstance(typevar, DerivedTypeVariable):
            node = self.node_mapping[typevar.type_var]
            for label in typevar.labels:
                succs = []
                for _, dst, data in self.graph.out_edges(node, data=True):
                    if "label" in data and data["label"] == label:
                        succs.append(dst)
                assert len(succs) <= 1
                if not succs:
                    return None
                node = succs[0]
                if isinstance(node, RecursiveRefNode):
                    node = node.target
        return node

    def add_edge(self, src: SketchNodeBase, dst: SketchNodeBase, label):
        assert not self.graph.has_edge(src, dst)
        self.graph.add_edge(src, dst, label=label)

    def add_constraint(self, constraint: TypeConstraint) -> None:
        # sub <: super
        if not isinstance(constraint, Subtype):
            return
        subtype = constraint.sub_type
        supertype = constraint.super_type
        if subtype in PRIMITIVE_TYPES and supertype not in PRIMITIVE_TYPES:
            super_node: Optional[SketchNode] = self.lookup(supertype)
            assert super_node is not None
            super_node.lower_bound = self.solver.join(super_node.lower_bound, subtype)
        elif supertype in PRIMITIVE_TYPES and subtype not in PRIMITIVE_TYPES:
            sub_node: Optional[SketchNode] = self.lookup(subtype)
            assert sub_node is not None
            sub_node.upper_bound = self.solver.meet(sub_node.upper_bound, supertype)


#
# Constraint graph
#


class ConstraintGraphTag(enum.Enum):
    LEFT = 0
    RIGHT = 1
    UNKNOWN = 2


class FORGOTTEN(enum.Enum):
    PRE_FORGOTTEN = 0
    POST_FORGOTTEN = 1


class ConstraintGraphNode:
    __slots__ = ("typevar", "variance", "tag", "forgotten")

    def __init__(
        self,
        typevar: Union[TypeVariable, DerivedTypeVariable],
        variance: Variance,
        tag: ConstraintGraphTag,
        forgotten: FORGOTTEN,
    ):
        self.typevar = typevar
        self.variance = variance
        self.tag = tag
        self.forgotten = forgotten

    def __repr__(self):
        variance_str = "CO" if self.variance == Variance.COVARIANT else "CONTRA"
        if self.tag == ConstraintGraphTag.LEFT:
            tag_str = "L"
        elif self.tag == ConstraintGraphTag.RIGHT:
            tag_str = "R"
        else:
            tag_str = "U"
        forgotten_str = "PRE" if FORGOTTEN.PRE_FORGOTTEN else "POST"
        return f"{self.typevar}#{variance_str}.{tag_str}.{forgotten_str}"

    def __eq__(self, other):
        if not isinstance(other, ConstraintGraphNode):
            return False
        return (
            self.typevar == other.typevar
            and self.variance == other.variance
            and self.tag == other.tag
            and self.forgotten == other.forgotten
        )

    def __hash__(self):
        return hash((ConstraintGraphNode, self.typevar, self.variance, self.tag, self.forgotten))

    def forget_last_label(self) -> Optional[Tuple["ConstraintGraphNode", BaseLabel]]:
        if isinstance(self.typevar, DerivedTypeVariable) and self.typevar.labels:
            last_label = self.typevar.labels[-1]
            if len(self.typevar.labels) == 1:
                prefix = self.typevar.type_var
            else:
                prefix = DerivedTypeVariable(self.typevar.type_var, None, labels=self.typevar.labels[:-1])
            if self.variance == last_label.variance:
                variance = Variance.COVARIANT
            else:
                variance = Variance.CONTRAVARIANT
            return (
                ConstraintGraphNode(prefix, variance, self.tag, FORGOTTEN.PRE_FORGOTTEN),
                self.typevar.labels[-1],
            )
        return None

    def recall(self, label: BaseLabel) -> "ConstraintGraphNode":
        if isinstance(self.typevar, DerivedTypeVariable):
            labels = self.typevar.labels + (label,)
            typevar = self.typevar.type_var
        elif isinstance(self.typevar, TypeVariable):
            labels = (label,)
            typevar = self.typevar
        else:
            raise TypeError(f"Unsupported type {type(self.typevar)}")
        if self.variance == label.variance:
            variance = Variance.COVARIANT
        else:
            variance = Variance.CONTRAVARIANT
        if not labels:
            var = typevar
        else:
            var = DerivedTypeVariable(typevar, None, labels=labels)
        return ConstraintGraphNode(var, variance, self.tag, FORGOTTEN.PRE_FORGOTTEN)

    def inverse(self) -> "ConstraintGraphNode":
        if self.tag == ConstraintGraphTag.LEFT:
            tag = ConstraintGraphTag.RIGHT
        elif self.tag == ConstraintGraphTag.RIGHT:
            tag = ConstraintGraphTag.LEFT
        else:
            tag = ConstraintGraphTag.UNKNOWN

        if self.variance == Variance.COVARIANT:
            variance = Variance.CONTRAVARIANT
        else:
            variance = Variance.COVARIANT

        return ConstraintGraphNode(self.typevar, variance, tag, self.forgotten)

    def inverse_wo_tag(self) -> "ConstraintGraphNode":
        """
        Invert the variance only.
        """
        if self.variance == Variance.COVARIANT:
            variance = Variance.CONTRAVARIANT
        else:
            variance = Variance.COVARIANT

        return ConstraintGraphNode(self.typevar, variance, self.tag, self.forgotten)


#
# The solver
#


class SimpleSolver:
    """
    SimpleSolver is, by its name, a simple solver. Most of this solver is based on the (complex) simplification logic
    that the retypd paper describes and the retypd re-implementation (https://github.com/GrammaTech/retypd) implements.
    Additionally, we add some improvements to allow type propagation of known struct names, among a few other
    improvements.
    """

    def __init__(self, bits: int, constraints):
        if bits not in (32, 64):
            raise ValueError("Pointer size %d is not supported. Expect 32 or 64." % bits)

        self.bits = bits
        self._constraints: Dict[TypeVariable, Set[TypeConstraint]] = constraints
        self._base_lattice = BASE_LATTICES[bits]
        self._base_lattice_inverted = networkx.DiGraph()
        for src, dst in self._base_lattice.edges:
            self._base_lattice_inverted.add_edge(dst, src)

        #
        # Solving state
        #
        # self._equivalence = {}
        # self._lower_bounds = defaultdict(BottomType)
        # self._upper_bounds = defaultdict(TopType)
        # self._recursive_types = defaultdict(set)

        equ_classes, sketches, type_schemes = self.solve()
        self.solution = {}
        self._solution_cache = {}
        self.determine(equ_classes, sketches, self.solution)

    def solve(self):
        """
        Steps:

        - Infer shapes
        -
        """

        func_typevars = set(self._constraints)
        constraints = set()
        for tv in func_typevars:
            constraints |= self._constraints[tv]
        equivalence_classes, sketches = self.infer_shapes(func_typevars, constraints)
        # TODO: Handle global variables

        # TODO: Generate function-specific type schemes
        type_schemes = constraints

        for tv in func_typevars:
            primitive_constraints = self._generate_primitive_constraints(type_schemes, {tv})
            for primitive_constraint in primitive_constraints:
                sketches[tv].add_constraint(primitive_constraint)

        return equivalence_classes, sketches, type_schemes

    def infer_shapes(
        self, func_typevars: Set[TypeVariable], constraints: Set[TypeConstraint]
    ) -> Dict[TypeVariable, Sketch]:
        """
        Computing sketches from constraint sets. Implements Algorithm E.1 in the retypd paper.
        """

        equivalence_classes, quotient_graph = self.compute_quotient_graph(constraints)

        sketches: Dict[TypeVariable, Sketch] = {}
        for tv in func_typevars:
            sketches[tv] = Sketch(self, tv)

        for tv, sketch in sketches.items():
            sketch_node = sketch.lookup(tv)
            graph_node = equivalence_classes.get(tv, None)
            # assert graph_node is not None
            if graph_node is None:
                continue
            visited = {graph_node: sketch_node}
            self._get_all_paths(quotient_graph, sketch, graph_node, visited)
        return equivalence_classes, sketches

    def compute_quotient_graph(self, constraints: Set[TypeConstraint]):
        """
        Compute the quotient graph (the constraint graph modulo ~ in Algorithm E.1 in the retypd paper) with respect to
        a given set of type constraints.
        """

        g = networkx.DiGraph()
        # collect all derived type variables
        typevars = self._typevars_from_constraints(constraints)
        g.add_nodes_from(typevars)
        # add paths for each derived type variable into the graph
        for tv in typevars:
            last_node = tv
            prefix = tv
            while isinstance(prefix, DerivedTypeVariable) and prefix.labels:
                prefix = prefix.longest_prefix()
                if prefix is None:
                    continue
                g.add_edge(prefix, last_node, label=last_node.labels[-1])
                last_node = prefix

        # compute the constraint graph modulo ~
        equivalence_classes = dict((node, node) for node in g)

        load = Load()
        store = Store()
        for node in g.nodes:
            lbl_to_node = {}
            for succ in g.successors(node):
                lbl_to_node[succ.labels[-1]] = succ
                if load in lbl_to_node and store in lbl_to_node:
                    self._unify(equivalence_classes, lbl_to_node[load], lbl_to_node[store], g)

        for constraint in constraints:
            if isinstance(constraint, Subtype):
                if constraint.super_type in PRIMITIVE_TYPES or constraint.sub_type in PRIMITIVE_TYPES:
                    continue
                self._unify(equivalence_classes, constraint.super_type, constraint.sub_type, g)

        out_graph = networkx.MultiDiGraph()  # there can be multiple edges between two nodes, each edge is associated
        # with a different label
        for src, dst, data in g.edges(data=True):
            src_cls = equivalence_classes[src]
            dst_cls = equivalence_classes[dst]
            label = None if not data else data["label"]
            if label is not None and out_graph.has_edge(src_cls, dst_cls):
                # do not add the same edge twice
                existing_labels = {
                    data["label"]
                    for _, dst_cls_, data_ in out_graph.out_edges(src_cls, data=True)
                    if dst_cls_ == dst_cls and data
                }
                if label in existing_labels:
                    continue
            out_graph.add_edge(src_cls, dst_cls, label=label)

        return equivalence_classes, out_graph

    def _generate_primitive_constraints(
        self, constraints: Set[TypeConstraint], non_primitive_endpoints: Set[Union[TypeVariable, DerivedTypeVariable]]
    ) -> Set[TypeConstraint]:
        # FIXME: Extract interesting variables
        constraint_graph = self._generate_constraint_graph(constraints, non_primitive_endpoints | PRIMITIVE_TYPES)
        constraints_0 = self._solve_constraints_between(constraint_graph, non_primitive_endpoints, PRIMITIVE_TYPES)
        constraints_1 = self._solve_constraints_between(constraint_graph, PRIMITIVE_TYPES, non_primitive_endpoints)
        return constraints_0 | constraints_1

    @staticmethod
    def _typevars_from_constraints(constraints: Set[TypeConstraint]) -> Set[Union[TypeVariable, DerivedTypeVariable]]:
        """
        Collect derived type variables from a set of constraints.
        """

        typevars: Set[Union[TypeVariable, DerivedTypeVariable]] = set()
        for constraint in constraints:
            if isinstance(constraint, Subtype):
                typevars.add(constraint.sub_type)
                typevars.add(constraint.super_type)
            # TODO: Other types of constraints?
        return typevars

    @staticmethod
    def _get_all_paths(
        graph: networkx.DiGraph,
        sketch: Sketch,
        node: DerivedTypeVariable,
        visited: Dict[Union[TypeVariable, DerivedTypeVariable], SketchNode],
    ):
        curr_node = visited[node]
        for _, succ, data in graph.out_edges(node, data=True):
            label = data["label"]
            if succ not in visited:
                if isinstance(curr_node.typevar, DerivedTypeVariable):
                    base_typevar = curr_node.typevar.type_var
                    labels = curr_node.typevar.labels
                elif isinstance(curr_node.typevar, TypeVariable):
                    base_typevar = curr_node.typevar
                    labels = tuple()
                else:
                    raise TypeError("Unexpected")
                labels += (label,)
                succ_derived_typevar = DerivedTypeVariable(
                    base_typevar,
                    None,
                    labels=labels,
                )
                succ_node = SketchNode(succ_derived_typevar)
                sketch.add_edge(curr_node, succ_node, label)
                visited[succ] = succ_node
                SimpleSolver._get_all_paths(graph, sketch, succ, visited)
                del visited[succ]
            else:
                # a cycle exists
                ref_node = RecursiveRefNode(visited[succ].typevar)
                sketch.add_edge(curr_node, ref_node, label)

    @staticmethod
    def _unify(
        equivalence_classes: Dict, cls0: DerivedTypeVariable, cls1: DerivedTypeVariable, graph: networkx.DiGraph
    ) -> None:
        # first convert cls0 and cls1 to their equivalence classes
        cls0 = equivalence_classes[cls0]
        cls1 = equivalence_classes[cls1]

        # unify if needed
        if cls0 != cls1:
            # MakeEquiv
            existing_elements = {key for key, item in equivalence_classes.items() if item in {cls0, cls1}}
            rep_cls = cls0
            for elem in existing_elements:
                equivalence_classes[elem] = rep_cls
            # the logic below refers to the retypd reference implementation. it is different from Algorithm E.1
            # note that graph is used read-only in this method, so we do not need to make copy of edges
            for _, dst0, data0 in graph.out_edges(cls0, data=True):
                if "label" in data0 and data0["label"] is not None:
                    for _, dst1, data1 in graph.out_edges(cls1, data=True):
                        if (
                            data0["label"] == data1["label"]
                            or isinstance(data0["label"], Load)
                            and isinstance(data1["label"], Store)
                        ):
                            SimpleSolver._unify(
                                equivalence_classes, equivalence_classes[dst0], equivalence_classes[dst1], graph
                            )

    #
    # Constraint graph
    #

    def _generate_constraint_graph(
        self, constraints: Set[TypeConstraint], interesting_variables: Set[DerivedTypeVariable]
    ) -> networkx.DiGraph:
        """
        A constraint graph  is the same as the finite state transducer that is presented in Appendix D in the retypd
        paper.
        """

        graph = networkx.DiGraph()
        for constraint in constraints:
            if isinstance(constraint, Subtype):
                self._constraint_graph_add_edges(
                    graph, constraint.sub_type, constraint.super_type, interesting_variables
                )
        self._constraint_graph_saturate(graph)
        self._constraint_graph_remove_self_loops(graph)
        self._constraint_graph_recall_forget_split(graph)
        return graph

    def _constraint_graph_add_recall_edges(self, graph: networkx.DiGraph, node: ConstraintGraphNode) -> None:
        while True:
            r = node.forget_last_label()
            if r is None:
                break
            prefix, last_label = r
            graph.add_edge(prefix, node, label=(last_label, "recall"))
            node = prefix

    def _constraint_graph_add_forget_edges(self, graph: networkx.DiGraph, node: ConstraintGraphNode) -> None:
        while True:
            r = node.forget_last_label()
            if r is None:
                break
            prefix, last_label = r
            graph.add_edge(node, prefix, label=(last_label, "forget"))
            node = prefix

    def _constraint_graph_add_edges(
        self,
        graph: networkx.DiGraph,
        subtype: Union[TypeVariable, DerivedTypeVariable],
        supertype: Union[TypeVariable, DerivedTypeVariable],
        interesting_variables: Set[DerivedTypeVariable],
    ):
        # left and right tags
        if self._to_typevar_or_typeconst(subtype) in interesting_variables:
            left_tag = ConstraintGraphTag.LEFT
        else:
            left_tag = ConstraintGraphTag.UNKNOWN
        if self._to_typevar_or_typeconst(supertype) in interesting_variables:
            right_tag = ConstraintGraphTag.RIGHT
        else:
            right_tag = ConstraintGraphTag.UNKNOWN
        # nodes
        forward_src = ConstraintGraphNode(subtype, Variance.COVARIANT, left_tag, FORGOTTEN.PRE_FORGOTTEN)
        forward_dst = ConstraintGraphNode(supertype, Variance.COVARIANT, right_tag, FORGOTTEN.PRE_FORGOTTEN)
        graph.add_edge(forward_src, forward_dst)
        # add recall edges and forget edges
        self._constraint_graph_add_recall_edges(graph, forward_src)
        self._constraint_graph_add_forget_edges(graph, forward_dst)

        # backward edges
        backward_src = forward_dst.inverse()
        backward_dst = forward_src.inverse()
        graph.add_edge(backward_src, backward_dst)
        self._constraint_graph_add_recall_edges(graph, backward_src)
        self._constraint_graph_add_forget_edges(graph, backward_dst)

    def _constraint_graph_saturate(self, graph: networkx.DiGraph) -> None:
        """
        The saturation algorithm D.2 as described in Appendix of the retypd paper.
        """
        R: DefaultDict[ConstraintGraphNode, Set[Tuple[BaseLabel, ConstraintGraphNode]]] = defaultdict(set)

        # initialize the reaching-push sets R(x)
        for x, y, data in graph.edges(data=True):
            if "label" in data and data.get("label")[1] == "forget":
                d = data["label"][0], x
                R[y].add(d)

        # repeat ... until fixed point
        changed = True
        while changed:
            changed = False
            for x, y, data in graph.edges(data=True):
                if "label" not in data:
                    if R[y].issuperset(R[x]):
                        continue
                    changed = True
                    R[y] |= R[x]
            for x, y, data in graph.edges(data=True):
                lbl = data.get("label")
                if lbl and lbl[1] == "recall":
                    for label, z in R[x]:
                        if not graph.has_edge(z, y):
                            changed = True
                            graph.add_edge(z, y)
            v_contravariant = []
            for node in graph.nodes:
                node: ConstraintGraphNode
                if node.variance == Variance.CONTRAVARIANT:
                    v_contravariant.append(node)
            # lazily apply saturation rules corresponding to S-Pointer
            for x in v_contravariant:
                for z_label, z in R[x]:
                    label = None
                    if isinstance(z_label, Store):
                        label = Load()
                    elif isinstance(z_label, Load):
                        label = Store()
                    if label is not None:
                        x_inverse = x.inverse_wo_tag()
                        d = label, z
                        if d not in R[x_inverse]:
                            changed = True
                            R[x_inverse].add(d)

    def _constraint_graph_remove_self_loops(self, graph: networkx.DiGraph):
        for node in list(graph.nodes):
            if graph.has_edge(node, node):
                graph.remove_edge(node, node)

    def _constraint_graph_recall_forget_split(self, graph: networkx.DiGraph):
        """
        Ensure that recall edges are not reachable after traversing a forget node.
        """
        for src, dst, data in list(graph.edges(data=True)):
            src: ConstraintGraphNode
            dst: ConstraintGraphNode
            if "label" in data and data["label"][1] == "recall":
                continue
            forget_src = ConstraintGraphNode(src.typevar, src.variance, src.tag, FORGOTTEN.POST_FORGOTTEN)
            forget_dst = ConstraintGraphNode(dst.typevar, dst.variance, dst.tag, FORGOTTEN.POST_FORGOTTEN)
            if "label" in data and data["label"][1] == "forget":
                graph.remove_edge(src, dst)
                graph.add_edge(src, forget_dst, **data)
            graph.add_edge(forget_src, forget_dst, **data)

    @staticmethod
    def _to_typevar_or_typeconst(
        obj: Union[TypeVariable, DerivedTypeVariable, TypeConstant]
    ) -> Union[TypeVariable, TypeConstant]:
        if isinstance(obj, DerivedTypeVariable):
            return obj.type_var
        elif isinstance(obj, TypeVariable):
            return obj
        elif isinstance(obj, TypeConstant):
            return obj
        raise TypeError(f"Unsupported type {type(obj)}")

    #
    # Graph solver
    #

    def _solve_constraints_between(
        self,
        graph: networkx.DiGraph,
        starts: Set[Union[TypeConstant, TypeVariable, DerivedTypeVariable]],
        ends: Set[Union[TypeConstant, TypeVariable, DerivedTypeVariable]],
    ) -> Set[TypeConstraint]:
        start_nodes = set()
        end_nodes = set()
        for node in graph.nodes:
            node: ConstraintGraphNode
            if node.typevar in starts and node.tag == ConstraintGraphTag.LEFT:
                start_nodes.add(node)
            if node.typevar in ends and node.tag == ConstraintGraphTag.RIGHT:
                end_nodes.add(node)

        assert start_nodes, "Start nodes cannot be empty"
        assert end_nodes, "End nodes cannot be empty"

        dfa_solver = DFAConstraintSolver()
        return dfa_solver.generate_constraints_between(graph, start_nodes, end_nodes)

    #
    # Type lattice
    #

    def join(self, t1: Union[TypeConstant, TypeVariable], t2: Union[TypeConstant, TypeVariable]) -> Type:
        return networkx.lowest_common_ancestor(self._base_lattice, t1, t2)

    def meet(self, t1: Union[TypeConstant, TypeVariable], t2: Union[TypeConstant, TypeVariable]) -> Type:
        return networkx.lowest_common_ancestor(self._base_lattice_inverted, t1, t2)

    def determine(self, equivalent_classes, sketches, solution: Dict, nodes: Optional[Set[SketchNode]] = None):
        """
        Return the solution from sketches
        """

        func_typevar = list(sketches)[0]
        if not nodes:
            # if type variables are not specified, collect all type variables and derived type variables
            typevars = set(v for v in equivalent_classes.values() if v not in PRIMITIVE_TYPES)

            # TODO: resolve references
            node = sketches[func_typevar].lookup(func_typevar)
            assert node is not None
            nodes = {node}

        # consult the cache
        cached_results = set()
        for node in nodes:
            if node.typevar in self._solution_cache:
                cached_results.add(self._solution_cache[node.typevar])
        if len(cached_results) == 1:
            return next(iter(cached_results))
        elif len(cached_results) > 1:
            # we get nodes for multiple type variables?
            raise RuntimeError("Getting nodes for multiple type variables. Unexpected.")

        # collect all successors and the paths (labels) of this type variable
        path_and_successors = []
        last_labels = []
        for node in nodes:
            path_and_successors += self._collect_sketch_paths(node, sketches[func_typevar])
        for labels, _ in path_and_successors:
            if labels:
                last_labels.append(labels[-1])

        # now, what is this variable?
        if last_labels and all(isinstance(label, (FuncIn, FuncOut)) for label in last_labels):
            # create a dummy result and dump it to the cache
            func_type = Function([], [])
            result = self._pointer_class()(basetype=func_type)
            for node in nodes:
                self._solution_cache[node.typevar] = result

            # this is a function variable
            func_inputs = defaultdict(set)
            func_outputs = defaultdict(set)

            for labels, succ in path_and_successors:
                last_label = labels[-1] if labels else None

                if isinstance(last_label, FuncIn):
                    func_inputs[last_label.loc].add(succ)
                elif isinstance(last_label, FuncOut):
                    func_outputs[last_label.loc].add(succ)
                else:
                    raise RuntimeError("Unreachable")

            input_args = []
            output_values = []
            for vals, out in [(func_inputs, input_args), (func_outputs, output_values)]:
                for idx in range(0, max(vals) + 1):
                    if idx in vals:
                        sol = self.determine(equivalent_classes, sketches, solution, vals[idx])
                        out.append(sol)
                    else:
                        out.append(None)

            # back patch
            func_type.params = input_args
            func_type.outputs = output_values

            for node in nodes:
                solution[node.typevar] = result

        elif not path_and_successors:
            # this is a primitive variable
            lower_bound = Bottom_
            upper_bound = Top_

            for node in nodes:
                lower_bound = self.join(lower_bound, node.lower_bound)
                upper_bound = self.meet(upper_bound, node.upper_bound)
                # TODO: Support variables that are accessed via differently sized pointers

            result = lower_bound if not isinstance(lower_bound, BottomType) else upper_bound
            for node in nodes:
                solution[node.typevar] = result
                self._solution_cache[node.typevar] = result

        else:
            # create a dummy result and shove it into the cache
            struct_type = Struct(fields={})
            result = self._pointer_class()(struct_type)
            for node in nodes:
                self._solution_cache[node.typevar] = result

            # this might be a struct
            fields = {}

            candidate_bases = defaultdict(set)

            for labels, succ in path_and_successors:
                last_label = labels[-1] if labels else None
                if isinstance(last_label, HasField):
                    candidate_bases[last_label.offset].add(last_label.bits // 8)

            node_to_base = {}

            for labels, succ in path_and_successors:
                last_label = labels[-1] if labels else None
                if isinstance(last_label, HasField):
                    for start_offset, sizes in candidate_bases.items():
                        for size in sizes:
                            if last_label.offset > start_offset:
                                if last_label.offset < start_offset + size:  # ???
                                    node_to_base[succ] = start_offset

            node_by_offset = defaultdict(set)

            for labels, succ in path_and_successors:
                last_label = labels[-1] if labels else None
                if isinstance(last_label, HasField):
                    if succ in node_to_base:
                        node_by_offset[node_to_base[succ]].add(succ)
                    else:
                        node_by_offset[last_label.offset].add(succ)

            for offset, nodes in node_by_offset.items():
                sol = self.determine(equivalent_classes, sketches, solution, nodes)
                fields[offset] = sol

            # back-patch
            struct_type.fields = fields
            for node in nodes:
                solution[node.typevar] = result

        # import pprint

        # print("Solution")
        # pprint.pprint(result)
        return result

    def _collect_sketch_paths(
        self, node: SketchNodeBase, sketch: Sketch
    ) -> List[Tuple[List[BaseLabel], SketchNodeBase]]:
        """
        Collect all paths that go from `typevar` to its leaves.
        """
        paths = []
        visited: Set[SketchNodeBase] = set()
        queue: List[Tuple[List[BaseLabel], SketchNodeBase]] = [([], node)]

        while queue:
            curr_labels, curr_node = queue.pop(0)
            if curr_node in visited:
                continue
            visited.add(curr_node)

            out_edges = sketch.graph.out_edges(curr_node, data=True)
            for _, succ, data in out_edges:
                if isinstance(succ, RecursiveRefNode):
                    ref = succ
                    succ = sketch.lookup(succ.target)
                    if succ is None:
                        # failed to resolve...
                        _l.warning(
                            "Failed to resolve reference node to a real sketch node for type variable %s", ref.target
                        )
                        continue
                label = data["label"]
                new_labels = curr_labels + [label]
                succ: SketchNode
                if isinstance(succ.typevar, DerivedTypeVariable) and isinstance(succ.typevar.labels[-1], (Load, Store)):
                    queue.append((new_labels, succ))
                else:
                    paths.append((new_labels, succ))

        return paths

    def _pointer_class(self) -> Union[Type[Pointer32], Type[Pointer64]]:
        if self.bits == 32:
            return Pointer32
        elif self.bits == 64:
            return Pointer64
        raise NotImplementedError("Unsupported bits %d" % self.bits)

    def _convert_arrays(self, constraints):
        for constraint in constraints:
            if not isinstance(constraint, Existence):
                continue
            inner = constraint.type_
            if isinstance(inner, DerivedTypeVariable) and isinstance(inner.label, IsArray):
                if inner.type_var in self._lower_bounds:
                    curr_type = self._lower_bounds[inner.type_var]
                    if isinstance(curr_type, Pointer) and isinstance(curr_type.basetype, Struct):
                        # replace all fields with the first field
                        if 0 in curr_type.basetype.fields:
                            first_field = curr_type.basetype.fields[0]
                            for offset in curr_type.basetype.fields.keys():
                                curr_type.basetype.fields[offset] = first_field
