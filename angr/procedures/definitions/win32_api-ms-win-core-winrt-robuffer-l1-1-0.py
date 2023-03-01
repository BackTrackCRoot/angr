# pylint:disable=line-too-long
import logging

from angr.sim_type import SimTypeFunction, SimTypeShort, SimTypeInt, SimTypeLong, SimTypeLongLong, SimTypeDouble, SimTypeFloat, SimTypePointer, SimTypeChar, SimStruct, SimTypeFixedSizeArray, SimTypeBottom, SimUnion, SimTypeBool
from angr.calling_conventions import SimCCStdcall, SimCCMicrosoftAMD64
from angr.procedures import SIM_PROCEDURES as P
from . import SimLibrary


_l = logging.getLogger(name=__name__)


lib = SimLibrary()
lib.set_default_cc('X86', SimCCStdcall)
lib.set_default_cc('AMD64', SimCCMicrosoftAMD64)
lib.set_library_names("api-ms-win-core-winrt-robuffer-l1-1-0.dll")
prototypes = \
    {
        #
        'RoGetBufferMarshaler': SimTypeFunction([SimTypePointer(SimTypeBottom(label="IMarshal"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["bufferMarshaler"]),
    }

lib.set_prototypes(prototypes)
