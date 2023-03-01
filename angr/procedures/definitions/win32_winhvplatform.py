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
lib.set_library_names("winhvplatform.dll")
prototypes = \
    {
        #
        'WHvGetCapability': SimTypeFunction([SimTypeInt(signed=False, label="WHV_CAPABILITY_CODE"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["CapabilityCode", "CapabilityBuffer", "CapabilityBufferSizeInBytes", "WrittenSizeInBytes"]),
        #
        'WHvCreatePartition': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition"]),
        #
        'WHvSetupPartition': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition"]),
        #
        'WHvDeletePartition': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition"]),
        #
        'WHvGetPartitionProperty': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="WHV_PARTITION_PROPERTY_CODE"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "PropertyCode", "PropertyBuffer", "PropertyBufferSizeInBytes", "WrittenSizeInBytes"]),
        #
        'WHvSetPartitionProperty': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="WHV_PARTITION_PROPERTY_CODE"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "PropertyCode", "PropertyBuffer", "PropertyBufferSizeInBytes"]),
        #
        'WHvSuspendPartitionTime': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition"]),
        #
        'WHvResumePartitionTime': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition"]),
        #
        'WHvMapGpaRange': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeLongLong(signed=False, label="UInt64"), SimTypeLongLong(signed=False, label="UInt64"), SimTypeInt(signed=False, label="WHV_MAP_GPA_RANGE_FLAGS")], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "SourceAddress", "GuestAddress", "SizeInBytes", "Flags"]),
        #
        'WHvUnmapGpaRange': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeLongLong(signed=False, label="UInt64"), SimTypeLongLong(signed=False, label="UInt64")], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "GuestAddress", "SizeInBytes"]),
        #
        'WHvTranslateGva': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeLongLong(signed=False, label="UInt64"), SimTypeInt(signed=False, label="WHV_TRANSLATE_GVA_FLAGS"), SimTypePointer(SimStruct({"ResultCode": SimTypeInt(signed=False, label="WHV_TRANSLATE_GVA_RESULT_CODE"), "Reserved": SimTypeInt(signed=False, label="UInt32")}, name="WHV_TRANSLATE_GVA_RESULT", pack=False, align=None), offset=0), SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex", "Gva", "TranslateFlags", "TranslationResult", "Gpa"]),
        #
        'WHvCreateVirtualProcessor': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex", "Flags"]),
        #
        'WHvDeleteVirtualProcessor': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex"]),
        #
        'WHvRunVirtualProcessor': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex", "ExitContext", "ExitContextSizeInBytes"]),
        #
        'WHvCancelRunVirtualProcessor': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex", "Flags"]),
        #
        'WHvGetVirtualProcessorRegisters': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="WHV_REGISTER_NAME"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimUnion({"Reg128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None"), "Reg64": SimTypeLongLong(signed=False, label="UInt64"), "Reg32": SimTypeInt(signed=False, label="UInt32"), "Reg16": SimTypeShort(signed=False, label="UInt16"), "Reg8": SimTypeChar(label="Byte"), "Fp": SimUnion({"Anonymous": SimStruct({"Mantissa": SimTypeLongLong(signed=False, label="UInt64"), "_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "FpControlStatus": SimUnion({"Anonymous": SimStruct({"FpControl": SimTypeShort(signed=False, label="UInt16"), "FpStatus": SimTypeShort(signed=False, label="UInt16"), "FpTag": SimTypeChar(label="Byte"), "Reserved": SimTypeChar(label="Byte"), "LastFpOp": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"LastFpRip": SimTypeLongLong(signed=False, label="UInt64"), "Anonymous": SimStruct({"LastFpEip": SimTypeInt(signed=False, label="UInt32"), "LastFpCs": SimTypeShort(signed=False, label="UInt16"), "Reserved2": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "XmmControlStatus": SimUnion({"Anonymous": SimStruct({"Anonymous": SimUnion({"LastFpRdp": SimTypeLongLong(signed=False, label="UInt64"), "Anonymous": SimStruct({"LastFpDp": SimTypeInt(signed=False, label="UInt32"), "LastFpDs": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None"), "XmmStatusControl": SimTypeInt(signed=False, label="UInt32"), "XmmStatusControlMask": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "Segment": SimStruct({"Base": SimTypeLongLong(signed=False, label="UInt64"), "Limit": SimTypeInt(signed=False, label="UInt32"), "Selector": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None), "Attributes": SimTypeShort(signed=False, label="UInt16")}, name="<anon>", label="None")}, name="WHV_X64_SEGMENT_REGISTER", pack=False, align=None), "Table": SimStruct({"Pad": SimTypeFixedSizeArray(SimTypeShort(signed=False, label="UInt16"), 3), "Limit": SimTypeShort(signed=False, label="UInt16"), "Base": SimTypeLongLong(signed=False, label="UInt64")}, name="WHV_X64_TABLE_REGISTER", pack=False, align=None), "InterruptState": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "PendingInterruption": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeInt(signed=False, label="UInt32"), "ErrorCode": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "DeliverabilityNotifications": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "ExceptionEvent": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeInt(signed=False, label="UInt32"), "ErrorCode": SimTypeInt(signed=False, label="UInt32"), "ExceptionParameter": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "ExtIntEvent": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64"), "Reserved2": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "InternalActivity": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "PendingDebugException": SimUnion({"AsUINT64": SimTypeLongLong(signed=False, label="UInt64"), "Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="<anon>", label="None"), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex", "RegisterNames", "RegisterCount", "RegisterValues"]),
        #
        'WHvSetVirtualProcessorRegisters': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="WHV_REGISTER_NAME"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimUnion({"Reg128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None"), "Reg64": SimTypeLongLong(signed=False, label="UInt64"), "Reg32": SimTypeInt(signed=False, label="UInt32"), "Reg16": SimTypeShort(signed=False, label="UInt16"), "Reg8": SimTypeChar(label="Byte"), "Fp": SimUnion({"Anonymous": SimStruct({"Mantissa": SimTypeLongLong(signed=False, label="UInt64"), "_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "FpControlStatus": SimUnion({"Anonymous": SimStruct({"FpControl": SimTypeShort(signed=False, label="UInt16"), "FpStatus": SimTypeShort(signed=False, label="UInt16"), "FpTag": SimTypeChar(label="Byte"), "Reserved": SimTypeChar(label="Byte"), "LastFpOp": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"LastFpRip": SimTypeLongLong(signed=False, label="UInt64"), "Anonymous": SimStruct({"LastFpEip": SimTypeInt(signed=False, label="UInt32"), "LastFpCs": SimTypeShort(signed=False, label="UInt16"), "Reserved2": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "XmmControlStatus": SimUnion({"Anonymous": SimStruct({"Anonymous": SimUnion({"LastFpRdp": SimTypeLongLong(signed=False, label="UInt64"), "Anonymous": SimStruct({"LastFpDp": SimTypeInt(signed=False, label="UInt32"), "LastFpDs": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None"), "XmmStatusControl": SimTypeInt(signed=False, label="UInt32"), "XmmStatusControlMask": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "Segment": SimStruct({"Base": SimTypeLongLong(signed=False, label="UInt64"), "Limit": SimTypeInt(signed=False, label="UInt32"), "Selector": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeShort(signed=False, label="UInt16")}, name="_Anonymous_e__Struct", pack=False, align=None), "Attributes": SimTypeShort(signed=False, label="UInt16")}, name="<anon>", label="None")}, name="WHV_X64_SEGMENT_REGISTER", pack=False, align=None), "Table": SimStruct({"Pad": SimTypeFixedSizeArray(SimTypeShort(signed=False, label="UInt16"), 3), "Limit": SimTypeShort(signed=False, label="UInt16"), "Base": SimTypeLongLong(signed=False, label="UInt64")}, name="WHV_X64_TABLE_REGISTER", pack=False, align=None), "InterruptState": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "PendingInterruption": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeInt(signed=False, label="UInt32"), "ErrorCode": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "DeliverabilityNotifications": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "ExceptionEvent": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeInt(signed=False, label="UInt32"), "ErrorCode": SimTypeInt(signed=False, label="UInt32"), "ExceptionParameter": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "ExtIntEvent": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64"), "Reserved2": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT128": SimUnion({"Anonymous": SimStruct({"Low64": SimTypeLongLong(signed=False, label="UInt64"), "High64": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "Dword": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 4)}, name="<anon>", label="None")}, name="<anon>", label="None"), "InternalActivity": SimUnion({"Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None), "AsUINT64": SimTypeLongLong(signed=False, label="UInt64")}, name="<anon>", label="None"), "PendingDebugException": SimUnion({"AsUINT64": SimTypeLongLong(signed=False, label="UInt64"), "Anonymous": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="<anon>", label="None"), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex", "RegisterNames", "RegisterCount", "RegisterValues"]),
        #
        'WHvGetVirtualProcessorInterruptControllerState': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex", "State", "StateSize", "WrittenSize"]),
        #
        'WHvSetVirtualProcessorInterruptControllerState': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex", "State", "StateSize"]),
        #
        'WHvRequestInterrupt': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64"), "Destination": SimTypeInt(signed=False, label="UInt32"), "Vector": SimTypeInt(signed=False, label="UInt32")}, name="WHV_INTERRUPT_CONTROL", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "Interrupt", "InterruptControlSize"]),
        #
        'WHvGetVirtualProcessorXsaveState': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex", "Buffer", "BufferSizeInBytes", "BytesWritten"]),
        #
        'WHvSetVirtualProcessorXsaveState': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex", "Buffer", "BufferSizeInBytes"]),
        #
        'WHvQueryGpaRangeDirtyBitmap': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeLongLong(signed=False, label="UInt64"), SimTypeLongLong(signed=False, label="UInt64"), SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "GuestAddress", "RangeSizeInBytes", "Bitmap", "BitmapSizeInBytes"]),
        #
        'WHvGetPartitionCounters': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="WHV_PARTITION_COUNTER_SET"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "CounterSet", "Buffer", "BufferSizeInBytes", "BytesWritten"]),
        #
        'WHvGetVirtualProcessorCounters': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="WHV_PROCESSOR_COUNTER_SET"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex", "CounterSet", "Buffer", "BufferSizeInBytes", "BytesWritten"]),
        #
        'WHvGetVirtualProcessorInterruptControllerState2': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex", "State", "StateSize", "WrittenSize"]),
        #
        'WHvSetVirtualProcessorInterruptControllerState2': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "VpIndex", "State", "StateSize"]),
        #
        'WHvRegisterPartitionDoorbellEvent': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"GuestAddress": SimTypeLongLong(signed=False, label="UInt64"), "Value": SimTypeLongLong(signed=False, label="UInt64"), "Length": SimTypeInt(signed=False, label="UInt32"), "_bitfield": SimTypeInt(signed=False, label="UInt32")}, name="WHV_DOORBELL_MATCH_DATA", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "MatchData", "EventHandle"]),
        #
        'WHvUnregisterPartitionDoorbellEvent': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"GuestAddress": SimTypeLongLong(signed=False, label="UInt64"), "Value": SimTypeLongLong(signed=False, label="UInt64"), "Length": SimTypeInt(signed=False, label="UInt32"), "_bitfield": SimTypeInt(signed=False, label="UInt32")}, name="WHV_DOORBELL_MATCH_DATA", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Partition", "MatchData"]),
    }

lib.set_prototypes(prototypes)
