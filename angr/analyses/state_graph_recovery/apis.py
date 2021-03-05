
# This file defines APIs for altering a state graph inside a binary. Some patches are defined by Patcherex.
#
#
# Do not import this file anywhere in angr by default since that would add a dependency from angr to Patcherex. Instead,
# import this file when needed::
#
#   from angr.analyses.state_graph_recovery import apis
#

from typing import Optional, Iterable

from patcherex.patches import AddCodePatch, InsertCodePatch, AddLabelPatch
from patcherex.patches import Patch

from .abstract_state import AbstractState


class AddStatePatch(Patch):
    """
    Add a new state and its corresponding logic (implemented as assembly code for now) to the state graph inside the
    binary.

    This patch is implemented as a combination of lower-level Patcherex patches.

    :ivar pred_states:  Predecessor states of this new abstract state.
    :ivar succ_states:  Successor states of this new abstract state.
    :ivar asm_code:     The assembly code that implements the logic of this new abstract state.
    """
    def __init__(self, pred_states: Iterable[AbstractState], succ_states: Optional[Iterable[AbstractState]]=None,
                 asm_code: Optional[str]=None, name: Optional[str]=None):

        super().__init__(name)

        self.pred_states = pred_states
        self.succ_states = succ_states
        self.asm_code = asm_code

    def __repr__(self):
        return "AddStatePatch"


class EditDataPatch(Patch):
    """
    Edit an existing constant value in the binary. Note that the constant value to be edited may or may not be in a
    data section. In other words, you may use EditDataPatch to directly edit bytes anywhere in the binary.

    If old_data is specified, it will be used to check against existing data before applying this patch. The patch will
    not be applied if existing data does not match old_data.

    Example: Changing the 4-byte chunk at 0x83200 from 04 00 00 00 to 13 37 00 00

        0x83200    04 00 00 00

        p = EditDataPatch(0x83200, b"\x13\x37\x00\x00", old_data=b"\x04\x00\x00\x00")

    After applying this patch::

        0x83200    13 37 00 00
    """
    def __init__(self, addr: int, data: bytes, old_data: Optional[bytes]=None, name: Optional[str]=None):
        super().__init__(name)
        self.addr = addr
        self.data = data
        self.old_data = old_data


class EditInstrPatch(Patch):
    """
    Edit an existing instruction in the binary. Note that this patch is not always applicable.

    For now, the following edits are supported.

    - Changing comparison operators: (signed to unsigned, unsigned to signed, less than to greater than, less than or
      equal to to greater than or equal to, etc.)
    - Nopping instructions.
    """
    def __init__(self, addr: int, new_instr: str, name: Optional[str]=None):
        super().__init__(name)
        self.addr = addr
        self.new_instr = new_instr
