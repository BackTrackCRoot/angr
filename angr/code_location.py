from typing import Optional, Dict


class CodeLocation:
    """
    Stands for a specific program point by specifying basic block address and statement ID (for IRSBs), or SimProcedure
    name (for SimProcedures).
    """

    __slots__ = ('block_addr', 'stmt_idx', 'sim_procedure', 'ins_addr', 'info', )

    def __init__(self, block_addr, stmt_idx, sim_procedure=None, ins_addr=None, **kwargs):
        """
        Constructor.

        :param int block_addr:      Address of the block
        :param int stmt_idx:        Statement ID. None for SimProcedures
        :param class sim_procedure: The corresponding SimProcedure class.
        :param int ins_addr:        The instruction address. Optional.
        :param kwargs:              Optional arguments, will be stored, but not used in __eq__ or __hash__.
        """

        self.block_addr = block_addr
        self.stmt_idx = stmt_idx
        self.sim_procedure = sim_procedure
        self.ins_addr = ins_addr

        self.info: Optional[Dict] = None

        self._store_kwargs(**kwargs)

    def __repr__(self):
        if self.block_addr is None:
            return '<%s>' % self.sim_procedure

        else:
            if self.stmt_idx is None:
                s = "<%s%#x(-)" % (
                    ("%#x " % self.ins_addr) if self.ins_addr else "",
                    self.block_addr,
                )
            else:
                s = "<%s%#x[%d]" % (
                    ("%#x id=" % self.ins_addr) if self.ins_addr else "",
                    self.block_addr,
                    self.stmt_idx,
                )

            ss = [ ]
            if self.info:
                for k, v in self.info.items():
                    if v != tuple() and v is not None:
                        ss.append("%s=%s" % (k, v))
                if ss:
                    s += " with %s" % ", ".join(ss)
            s += ">"

            return s

    @property
    def short_repr(self):
        if self.ins_addr is not None:
            return "%#x" % self.ins_addr
        else:
            return repr(self)

    def __eq__(self, other):
        """
        Check if self is the same as other.
        """
        if type(self) is type(other) and self.block_addr == other.block_addr and \
               self.stmt_idx == other.stmt_idx and self.sim_procedure is other.sim_procedure:
            # compare context
            ctx0 = self.info.get('context', None)
            ctx1 = other.info.get('context', None)
            if not ctx0 and not ctx1:
                return True
            return ctx0 == ctx1
        return False

    def __hash__(self):
        """
        returns the hash value of self.
        """
        context = self.info.get('context', None)
        return hash((self.block_addr, self.stmt_idx, self.sim_procedure, context))

    def _store_kwargs(self, **kwargs):
        if self.info is None:
            self.info = { }
        for k, v in kwargs.items():
            self.info[k] = v
