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
lib.set_library_names("winusb.dll")
prototypes = \
    {
        #
        'WinUsb_Initialize': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["DeviceHandle", "InterfaceHandle"]),
        #
        'WinUsb_Free': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle"]),
        #
        'WinUsb_GetAssociatedInterface': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte"), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "AssociatedInterfaceIndex", "AssociatedInterfaceHandle"]),
        #
        'WinUsb_GetDescriptor': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte"), SimTypeChar(label="Byte"), SimTypeShort(signed=False, label="UInt16"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "DescriptorType", "Index", "LanguageID", "Buffer", "BufferLength", "LengthTransferred"]),
        #
        'WinUsb_QueryInterfaceSettings': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte"), SimTypePointer(SimStruct({"bLength": SimTypeChar(label="Byte"), "bDescriptorType": SimTypeChar(label="Byte"), "bInterfaceNumber": SimTypeChar(label="Byte"), "bAlternateSetting": SimTypeChar(label="Byte"), "bNumEndpoints": SimTypeChar(label="Byte"), "bInterfaceClass": SimTypeChar(label="Byte"), "bInterfaceSubClass": SimTypeChar(label="Byte"), "bInterfaceProtocol": SimTypeChar(label="Byte"), "iInterface": SimTypeChar(label="Byte")}, name="USB_INTERFACE_DESCRIPTOR", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "AlternateInterfaceNumber", "UsbAltInterfaceDescriptor"]),
        #
        'WinUsb_QueryDeviceInformation': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "InformationType", "BufferLength", "Buffer"]),
        #
        'WinUsb_SetCurrentAlternateSetting': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte")], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "SettingNumber"]),
        #
        'WinUsb_GetCurrentAlternateSetting': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "SettingNumber"]),
        #
        'WinUsb_QueryPipe': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte"), SimTypeChar(label="Byte"), SimTypePointer(SimStruct({"PipeType": SimTypeInt(signed=False, label="USBD_PIPE_TYPE"), "PipeId": SimTypeChar(label="Byte"), "MaximumPacketSize": SimTypeShort(signed=False, label="UInt16"), "Interval": SimTypeChar(label="Byte")}, name="WINUSB_PIPE_INFORMATION", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "AlternateInterfaceNumber", "PipeIndex", "PipeInformation"]),
        #
        'WinUsb_QueryPipeEx': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte"), SimTypeChar(label="Byte"), SimTypePointer(SimStruct({"PipeType": SimTypeInt(signed=False, label="USBD_PIPE_TYPE"), "PipeId": SimTypeChar(label="Byte"), "MaximumPacketSize": SimTypeShort(signed=False, label="UInt16"), "Interval": SimTypeChar(label="Byte"), "MaximumBytesPerInterval": SimTypeInt(signed=False, label="UInt32")}, name="WINUSB_PIPE_INFORMATION_EX", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "AlternateSettingNumber", "PipeIndex", "PipeInformationEx"]),
        #
        'WinUsb_SetPipePolicy': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "PipeID", "PolicyType", "ValueLength", "Value"]),
        #
        'WinUsb_GetPipePolicy': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "PipeID", "PolicyType", "ValueLength", "Value"]),
        #
        'WinUsb_ReadPipe': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "PipeID", "Buffer", "BufferLength", "LengthTransferred", "Overlapped"]),
        #
        'WinUsb_WritePipe': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "PipeID", "Buffer", "BufferLength", "LengthTransferred", "Overlapped"]),
        #
        'WinUsb_ControlTransfer': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimStruct({"RequestType": SimTypeChar(label="Byte"), "Request": SimTypeChar(label="Byte"), "Value": SimTypeShort(signed=False, label="UInt16"), "Index": SimTypeShort(signed=False, label="UInt16"), "Length": SimTypeShort(signed=False, label="UInt16")}, name="WINUSB_SETUP_PACKET", pack=False, align=None), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "SetupPacket", "Buffer", "BufferLength", "LengthTransferred", "Overlapped"]),
        #
        'WinUsb_ResetPipe': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte")], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "PipeID"]),
        #
        'WinUsb_AbortPipe': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte")], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "PipeID"]),
        #
        'WinUsb_FlushPipe': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte")], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "PipeID"]),
        #
        'WinUsb_SetPowerPolicy': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "PolicyType", "ValueLength", "Value"]),
        #
        'WinUsb_GetPowerPolicy': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "PolicyType", "ValueLength", "Value"]),
        #
        'WinUsb_GetOverlappedResult': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "lpOverlapped", "lpNumberOfBytesTransferred", "bWait"]),
        #
        'WinUsb_ParseConfigurationDescriptor': SimTypeFunction([SimTypePointer(SimStruct({"bLength": SimTypeChar(label="Byte"), "bDescriptorType": SimTypeChar(label="Byte"), "wTotalLength": SimTypeShort(signed=False, label="UInt16"), "bNumInterfaces": SimTypeChar(label="Byte"), "bConfigurationValue": SimTypeChar(label="Byte"), "iConfiguration": SimTypeChar(label="Byte"), "bmAttributes": SimTypeChar(label="Byte"), "MaxPower": SimTypeChar(label="Byte")}, name="USB_CONFIGURATION_DESCRIPTOR", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32")], SimTypePointer(SimStruct({"bLength": SimTypeChar(label="Byte"), "bDescriptorType": SimTypeChar(label="Byte"), "bInterfaceNumber": SimTypeChar(label="Byte"), "bAlternateSetting": SimTypeChar(label="Byte"), "bNumEndpoints": SimTypeChar(label="Byte"), "bInterfaceClass": SimTypeChar(label="Byte"), "bInterfaceSubClass": SimTypeChar(label="Byte"), "bInterfaceProtocol": SimTypeChar(label="Byte"), "iInterface": SimTypeChar(label="Byte")}, name="USB_INTERFACE_DESCRIPTOR", pack=False, align=None), offset=0), arg_names=["ConfigurationDescriptor", "StartPosition", "InterfaceNumber", "AlternateSetting", "InterfaceClass", "InterfaceSubClass", "InterfaceProtocol"]),
        #
        'WinUsb_ParseDescriptors': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypePointer(SimStruct({"bLength": SimTypeChar(label="Byte"), "bDescriptorType": SimTypeChar(label="Byte")}, name="USB_COMMON_DESCRIPTOR", pack=False, align=None), offset=0), arg_names=["DescriptorBuffer", "TotalLength", "StartPosition", "DescriptorType"]),
        #
        'WinUsb_GetCurrentFrameNumber': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "CurrentFrameNumber", "TimeStamp"]),
        #
        'WinUsb_GetAdjustedFrameNumber': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None")], SimTypeInt(signed=True, label="Int32"), arg_names=["CurrentFrameNumber", "TimeStamp"]),
        #
        'WinUsb_RegisterIsochBuffer': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "PipeID", "Buffer", "BufferLength", "IsochBufferHandle"]),
        #
        'WinUsb_UnregisterIsochBuffer': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["IsochBufferHandle"]),
        #
        'WinUsb_WriteIsochPipe': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["BufferHandle", "Offset", "Length", "FrameNumber", "Overlapped"]),
        #
        'WinUsb_ReadIsochPipe': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "Length": SimTypeInt(signed=False, label="UInt32"), "Status": SimTypeInt(signed=True, label="Int32")}, name="USBD_ISO_PACKET_DESCRIPTOR", pack=False, align=None), label="LPArray", offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["BufferHandle", "Offset", "Length", "FrameNumber", "NumberOfPackets", "IsoPacketDescriptors", "Overlapped"]),
        #
        'WinUsb_WriteIsochPipeAsap': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["BufferHandle", "Offset", "Length", "ContinueStream", "Overlapped"]),
        #
        'WinUsb_ReadIsochPipeAsap': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "Length": SimTypeInt(signed=False, label="UInt32"), "Status": SimTypeInt(signed=True, label="Int32")}, name="USBD_ISO_PACKET_DESCRIPTOR", pack=False, align=None), label="LPArray", offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["BufferHandle", "Offset", "Length", "ContinueStream", "NumberOfPackets", "IsoPacketDescriptors", "Overlapped"]),
        #
        'WinUsb_StartTrackingForTimeSync': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"TimeTrackingHandle": SimTypeBottom(label="HANDLE"), "IsStartupDelayTolerable": SimTypeBottom(label="BOOLEAN")}, name="USB_START_TRACKING_FOR_TIME_SYNC_INFORMATION", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "StartTrackingInfo"]),
        #
        'WinUsb_GetCurrentFrameNumberAndQpc': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"TimeTrackingHandle": SimTypeBottom(label="HANDLE"), "InputFrameNumber": SimTypeInt(signed=False, label="UInt32"), "InputMicroFrameNumber": SimTypeInt(signed=False, label="UInt32"), "QueryPerformanceCounterAtInputFrameOrMicroFrame": SimTypeBottom(label="LARGE_INTEGER"), "QueryPerformanceCounterFrequency": SimTypeBottom(label="LARGE_INTEGER"), "PredictedAccuracyInMicroSeconds": SimTypeInt(signed=False, label="UInt32"), "CurrentGenerationID": SimTypeInt(signed=False, label="UInt32"), "CurrentQueryPerformanceCounter": SimTypeBottom(label="LARGE_INTEGER"), "CurrentHardwareFrameNumber": SimTypeInt(signed=False, label="UInt32"), "CurrentHardwareMicroFrameNumber": SimTypeInt(signed=False, label="UInt32"), "CurrentUSBFrameNumber": SimTypeInt(signed=False, label="UInt32")}, name="USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "FrameQpcInfo"]),
        #
        'WinUsb_StopTrackingForTimeSync': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"TimeTrackingHandle": SimTypeBottom(label="HANDLE")}, name="USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["InterfaceHandle", "StopTrackingInfo"]),
    }

lib.set_prototypes(prototypes)
