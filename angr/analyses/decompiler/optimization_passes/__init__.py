# pylint:disable=import-outside-toplevel
from typing import Optional, Union

from archinfo import Arch

from .base_ptr_save_simplifier import BasePointerSaveSimplifier
from .const_derefs import ConstantDereferencesSimplifier
from .div_simplifier import DivSimplifier
from .eager_returns import EagerReturnsSimplifier
from .expr_op_swapper import ExprOpSwapper
from .ite_expr_converter import ITEExprConverter
from .lowered_switch_simplifier import LoweredSwitchSimplifier
from .mod_simplifier import ModSimplifier
from .multi_simplifier import MultiSimplifier
from .optimization_pass import OptimizationPassStage
from .register_save_area_simplifier import RegisterSaveAreaSimplifier
from .ret_addr_save_simplifier import RetAddrSaveSimplifier
from .stack_canary_simplifier import StackCanarySimplifier
from .x86_gcc_getpc_simplifier import X86GccGetPcSimplifier

_all_optimization_passes = [
    (RegisterSaveAreaSimplifier, True),
    (StackCanarySimplifier, True),
    (BasePointerSaveSimplifier, True),
    (DivSimplifier, True),
    (MultiSimplifier, True),
    (ModSimplifier, True),
    (ConstantDereferencesSimplifier, True),
    (RetAddrSaveSimplifier, True),
    (X86GccGetPcSimplifier, True),
    (LoweredSwitchSimplifier, False),
    (EagerReturnsSimplifier, True),
    (ITEExprConverter, True),
    (ExprOpSwapper, True),
]


def get_optimization_passes(arch, platform):
    if isinstance(arch, Arch):
        arch = arch.name

    if platform is not None:
        platform = platform.lower()

    passes = []
    for pass_, _ in _all_optimization_passes:
        if (pass_.ARCHES is None or arch in pass_.ARCHES) and (
            pass_.PLATFORMS is None or platform is None or platform in pass_.PLATFORMS
        ):
            passes.append(pass_)

    return passes


def get_default_optimization_passes(arch: Union[Arch, str], platform: Optional[str]):
    if isinstance(arch, Arch):
        arch = arch.name

    if platform is not None:
        platform = platform.lower()

    passes = []
    for pass_, default in _all_optimization_passes:
        if not default:
            continue
        if (pass_.ARCHES is None or arch in pass_.ARCHES) and (
            pass_.PLATFORMS is None or platform is None or platform in pass_.PLATFORMS
        ):
            passes.append(pass_)

    return passes
