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
lib.set_library_names("winhvemulation.dll")
prototypes = \
    {
        #
        'WHvEmulatorCreateEmulator': SimTypeFunction([SimTypePointer(SimStruct({"Size": SimTypeInt(signed=False, label="UInt32"), "Reserved": SimTypeInt(signed=False, label="UInt32"), "WHvEmulatorIoPortCallback": SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"Direction": SimTypeChar(label="Byte"), "Port": SimTypeShort(signed=False, label="UInt16"), "AccessSize": SimTypeShort(signed=False, label="UInt16"), "Data": SimTypeInt(signed=False, label="UInt32")}, name="WHV_EMULATOR_IO_ACCESS_INFO", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Context", "IoAccess"]), offset=0), "WHvEmulatorMemoryCallback": SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"GpaAddress": SimTypeLongLong(signed=False, label="UInt64"), "Direction": SimTypeChar(label="Byte"), "AccessSize": SimTypeChar(label="Byte"), "Data": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 8)}, name="WHV_EMULATOR_MEMORY_ACCESS_INFO", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Context", "MemoryAccess"]), offset=0), "WHvEmulatorGetVirtualProcessorRegisters": SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="WHV_REGISTER_NAME"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimUnion({"Reg128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None"), "Reg64": SimTypeLongLong(signed=False, label="UInt64"), "Reg32": SimTypeInt(signed=False, label="UInt32"), "Reg16": SimTypeShort(signed=False, label="UInt16"), "Reg8": SimTypeChar(label="Byte"), "Fp": SimUnion({"Anonymous": SimStruct({"Mantissa": SimTypeLongLong(signed=False, label="UInt64"), "_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "FpControlStatus": SimUnion({"Anonymous": SimStruct({"FpControl": SimTypeShort(signed=False, label="UInt16"), "FpStatus": SimTypeShort(signed=False, label="UInt16"), "FpTag": SimTypeChar(label="Byte"), "Reserved": SimTypeChar(label="Byte"), "LastFpOp": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"LastFpRip": SimTypeLongLong(signed=False, label="UInt64"), "Anonymous": SimStruct({"LastFpEip": SimTypeInt(signed=False, label="UInt32"), "LastFpCs": SimTypeShort(signed=False, label="UInt16"), "Reserved2": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "XmmControlStatus": SimUnion({"Anonymous": SimStruct({"Anonymous": SimUnion({"LastFpRdp": SimTypeLongLong(signed=False, label="UInt64"), "Anonymous": SimStruct({"LastFpDp": SimTypeInt(signed=False, label="UInt32"), "LastFpDs": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None"), "XmmStatusControl": SimTypeInt(signed=False, label="UInt32"), "XmmStatusControlMask": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "Segment": SimStruct({"Base": SimTypeLongLong(signed=False, label="UInt64"), "Limit": SimTypeInt(signed=False, label="UInt32"), "Selector": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None), "Attributes": SimTypeShort(signed=False, label="UInt16")}, name="<anon>", label="None")}, name="WHV_X64_SEGMENT_REGISTER", pack=False, align=None), "Table": SimStruct({"Pad": SimTypeFixedSizeArray(SimTypeShort(signed=False, label="UInt16"), 3), "Limit": SimTypeShort(signed=False, label="UInt16"), "Base": SimTypeLongLong(signed=False, label="UInt64")}, name="WHV_X64_TABLE_REGISTER", pack=False, align=None), "InterruptState": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "PendingInterruption": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeInt(signed=False, label="UInt32"), "ErrorCode": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "DeliverabilityNotifications": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "ExceptionEvent": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeInt(signed=False, label="UInt32"), "ErrorCode": SimTypeInt(signed=False, label="UInt32"), "ExceptionParameter": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "ExtIntEvent": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64"), "Reserved2": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "InternalActivity": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "PendingDebugException": SimUnion({"AsUINT64": SimTypeLongLong(signed=False, label="UInt64"), "Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="<anon>", label="None"), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Context", "RegisterNames", "RegisterCount", "RegisterValues"]), offset=0), "WHvEmulatorSetVirtualProcessorRegisters": SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="WHV_REGISTER_NAME"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimUnion({"Reg128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None"), "Reg64": SimTypeLongLong(signed=False, label="UInt64"), "Reg32": SimTypeInt(signed=False, label="UInt32"), "Reg16": SimTypeShort(signed=False, label="UInt16"), "Reg8": SimTypeChar(label="Byte"), "Fp": SimUnion({"Anonymous": SimStruct({"Mantissa": SimTypeLongLong(signed=False, label="UInt64"), "_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "FpControlStatus": SimUnion({"Anonymous": SimStruct({"FpControl": SimTypeShort(signed=False, label="UInt16"), "FpStatus": SimTypeShort(signed=False, label="UInt16"), "FpTag": SimTypeChar(label="Byte"), "Reserved": SimTypeChar(label="Byte"), "LastFpOp": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"LastFpRip": SimTypeLongLong(signed=False, label="UInt64"), "Anonymous": SimStruct({"LastFpEip": SimTypeInt(signed=False, label="UInt32"), "LastFpCs": SimTypeShort(signed=False, label="UInt16"), "Reserved2": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "XmmControlStatus": SimUnion({"Anonymous": SimStruct({"Anonymous": SimUnion({"LastFpRdp": SimTypeLongLong(signed=False, label="UInt64"), "Anonymous": SimStruct({"LastFpDp": SimTypeInt(signed=False, label="UInt32"), "LastFpDs": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None"), "XmmStatusControl": SimTypeInt(signed=False, label="UInt32"), "XmmStatusControlMask": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "Segment": SimStruct({"Base": SimTypeLongLong(signed=False, label="UInt64"), "Limit": SimTypeInt(signed=False, label="UInt32"), "Selector": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None), "Attributes": SimTypeShort(signed=False, label="UInt16")}, name="<anon>", label="None")}, name="WHV_X64_SEGMENT_REGISTER", pack=False, align=None), "Table": SimStruct({"Pad": SimTypeFixedSizeArray(SimTypeShort(signed=False, label="UInt16"), 3), "Limit": SimTypeShort(signed=False, label="UInt16"), "Base": SimTypeLongLong(signed=False, label="UInt64")}, name="WHV_X64_TABLE_REGISTER", pack=False, align=None), "InterruptState": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "PendingInterruption": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeInt(signed=False, label="UInt32"), "ErrorCode": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "DeliverabilityNotifications": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "ExceptionEvent": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeInt(signed=False, label="UInt32"), "ErrorCode": SimTypeInt(signed=False, label="UInt32"), "ExceptionParameter": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "ExtIntEvent": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64"), "Reserved2": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "InternalActivity": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "PendingDebugException": SimUnion({"AsUINT64": SimTypeLongLong(signed=False, label="UInt64"), "Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="<anon>", label="None"), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Context", "RegisterNames", "RegisterCount", "RegisterValues"]), offset=0), "WHvEmulatorTranslateGvaPage": SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeLongLong(signed=False, label="UInt64"), SimTypeInt(signed=False, label="WHV_TRANSLATE_GVA_FLAGS"), SimTypePointer(SimTypeInt(signed=False, label="WHV_TRANSLATE_GVA_RESULT_CODE"), offset=0), SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Context", "Gva", "TranslateFlags", "TranslationResult", "Gpa"]), offset=0)}, name="WHV_EMULATOR_CALLBACKS", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Callbacks", "Emulator"]),
        #
        'WHvEmulatorDestroyEmulator': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Emulator"]),
        #
        'WHvEmulatorTryIoEmulation': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"ExecutionState": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT16": SimTypeShort(signed=False, label="UInt16")}, name="<anon>", label="None"), "_bitfield": SimTypeChar(label="Byte"), "Reserved": SimTypeChar(label="Byte"), "Reserved2": SimTypeInt(signed=False, label="UInt32"), "Cs": SimStruct({"Base": SimTypeLongLong(signed=False, label="UInt64"), "Limit": SimTypeInt(signed=False, label="UInt32"), "Selector": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None), "Attributes": SimTypeShort(signed=False, label="UInt16")}, name="<anon>", label="None")}, name="WHV_X64_SEGMENT_REGISTER", pack=False, align=None), "Rip": SimTypeLongLong(signed=False, label="UInt64"), "Rflags": SimTypeLongLong(signed=False, label="UInt64")}, name="WHV_VP_EXIT_CONTEXT", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"InstructionByteCount": SimTypeChar(label="Byte"), "Reserved": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 3), "InstructionBytes": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16), "AccessInfo": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT32": SimTypeInt(signed=False, label="UInt32")}, name="<anon>", label="None"), "PortNumber": SimTypeShort(signed=False, label="UInt16"), "Reserved2": SimTypeFixedSizeArray(SimTypeShort(signed=False, label="UInt16"), 3), "Rax": SimTypeLongLong(signed=False, label="UInt64"), "Rcx": SimTypeLongLong(signed=False, label="UInt64"), "Rsi": SimTypeLongLong(signed=False, label="UInt64"), "Rdi": SimTypeLongLong(signed=False, label="UInt64"), "Ds": SimStruct({"Base": SimTypeLongLong(signed=False, label="UInt64"), "Limit": SimTypeInt(signed=False, label="UInt32"), "Selector": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None), "Attributes": SimTypeShort(signed=False, label="UInt16")}, name="<anon>", label="None")}, name="WHV_X64_SEGMENT_REGISTER", pack=False, align=None), "Es": SimStruct({"Base": SimTypeLongLong(signed=False, label="UInt64"), "Limit": SimTypeInt(signed=False, label="UInt32"), "Selector": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None), "Attributes": SimTypeShort(signed=False, label="UInt16")}, name="<anon>", label="None")}, name="WHV_X64_SEGMENT_REGISTER", pack=False, align=None)}, name="WHV_X64_IO_PORT_ACCESS_CONTEXT", pack=False, align=None), offset=0), SimTypePointer(SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT32": SimTypeInt(signed=False, label="UInt32")}, name="<anon>", label="None"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Emulator", "Context", "VpContext", "IoInstructionContext", "EmulatorReturnStatus"]),
        #
        'WHvEmulatorTryMmioEmulation': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"ExecutionState": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT16": SimTypeShort(signed=False, label="UInt16")}, name="<anon>", label="None"), "_bitfield": SimTypeChar(label="Byte"), "Reserved": SimTypeChar(label="Byte"), "Reserved2": SimTypeInt(signed=False, label="UInt32"), "Cs": SimStruct({"Base": SimTypeLongLong(signed=False, label="UInt64"), "Limit": SimTypeInt(signed=False, label="UInt32"), "Selector": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None), "Attributes": SimTypeShort(signed=False, label="UInt16")}, name="<anon>", label="None")}, name="WHV_X64_SEGMENT_REGISTER", pack=False, align=None), "Rip": SimTypeLongLong(signed=False, label="UInt64"), "Rflags": SimTypeLongLong(signed=False, label="UInt64")}, name="WHV_VP_EXIT_CONTEXT", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"InstructionByteCount": SimTypeChar(label="Byte"), "Reserved": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 3), "InstructionBytes": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16), "AccessInfo": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT32": SimTypeInt(signed=False, label="UInt32")}, name="<anon>", label="None"), "Gpa": SimTypeLongLong(signed=False, label="UInt64"), "Gva": SimTypeLongLong(signed=False, label="UInt64")}, name="WHV_MEMORY_ACCESS_CONTEXT", pack=False, align=None), offset=0), SimTypePointer(SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT32": SimTypeInt(signed=False, label="UInt32")}, name="<anon>", label="None"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Emulator", "Context", "VpContext", "MmioInstructionContext", "EmulatorReturnStatus"]),
    }

lib.set_prototypes(prototypes)
