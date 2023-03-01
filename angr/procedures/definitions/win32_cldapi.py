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
lib.set_library_names("cldapi.dll")
prototypes = \
    {
        #
        'CfGetPlatformInfo': SimTypeFunction([SimTypePointer(SimStruct({"BuildNumber": SimTypeInt(signed=False, label="UInt32"), "RevisionNumber": SimTypeInt(signed=False, label="UInt32"), "IntegrationNumber": SimTypeInt(signed=False, label="UInt32")}, name="CF_PLATFORM_INFO", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["PlatformVersion"]),
        #
        'CfRegisterSyncRoot': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"StructSize": SimTypeInt(signed=False, label="UInt32"), "ProviderName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "ProviderVersion": SimTypePointer(SimTypeChar(label="Char"), offset=0), "SyncRootIdentity": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "SyncRootIdentityLength": SimTypeInt(signed=False, label="UInt32"), "FileIdentity": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "FileIdentityLength": SimTypeInt(signed=False, label="UInt32"), "ProviderId": SimTypeBottom(label="Guid")}, name="CF_SYNC_REGISTRATION", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"StructSize": SimTypeInt(signed=False, label="UInt32"), "Hydration": SimStruct({"Primary": SimStruct({"us": SimTypeShort(signed=False, label="UInt16")}, name="CF_HYDRATION_POLICY_PRIMARY_USHORT", pack=False, align=None), "Modifier": SimStruct({"us": SimTypeShort(signed=False, label="UInt16")}, name="CF_HYDRATION_POLICY_MODIFIER_USHORT", pack=False, align=None)}, name="CF_HYDRATION_POLICY", pack=False, align=None), "Population": SimStruct({"Primary": SimStruct({"us": SimTypeShort(signed=False, label="UInt16")}, name="CF_POPULATION_POLICY_PRIMARY_USHORT", pack=False, align=None), "Modifier": SimStruct({"us": SimTypeShort(signed=False, label="UInt16")}, name="CF_POPULATION_POLICY_MODIFIER_USHORT", pack=False, align=None)}, name="CF_POPULATION_POLICY", pack=False, align=None), "InSync": SimTypeInt(signed=False, label="CF_INSYNC_POLICY"), "HardLink": SimTypeInt(signed=False, label="CF_HARDLINK_POLICY"), "PlaceholderManagement": SimTypeInt(signed=False, label="CF_PLACEHOLDER_MANAGEMENT_POLICY")}, name="CF_SYNC_POLICIES", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="CF_REGISTER_FLAGS")], SimTypeInt(signed=True, label="Int32"), arg_names=["SyncRootPath", "Registration", "Policies", "RegisterFlags"]),
        #
        'CfUnregisterSyncRoot': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["SyncRootPath"]),
        #
        'CfConnectSyncRoot': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"Type": SimTypeInt(signed=False, label="CF_CALLBACK_TYPE"), "Callback": SimTypePointer(SimTypeFunction([SimTypePointer(SimStruct({"StructSize": SimTypeInt(signed=False, label="UInt32"), "ConnectionKey": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "CallbackContext": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "VolumeGuidName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "VolumeDosName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "VolumeSerialNumber": SimTypeInt(signed=False, label="UInt32"), "SyncRootFileId": SimTypeBottom(label="LARGE_INTEGER"), "SyncRootIdentity": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "SyncRootIdentityLength": SimTypeInt(signed=False, label="UInt32"), "FileId": SimTypeBottom(label="LARGE_INTEGER"), "FileSize": SimTypeBottom(label="LARGE_INTEGER"), "FileIdentity": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "FileIdentityLength": SimTypeInt(signed=False, label="UInt32"), "NormalizedPath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "TransferKey": SimTypeBottom(label="LARGE_INTEGER"), "PriorityHint": SimTypeChar(label="Byte"), "CorrelationVector": SimTypePointer(SimTypeBottom(label="CORRELATION_VECTOR"), offset=0), "ProcessInfo": SimTypePointer(SimStruct({"StructSize": SimTypeInt(signed=False, label="UInt32"), "ProcessId": SimTypeInt(signed=False, label="UInt32"), "ImagePath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "PackageName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "ApplicationId": SimTypePointer(SimTypeChar(label="Char"), offset=0), "CommandLine": SimTypePointer(SimTypeChar(label="Char"), offset=0), "SessionId": SimTypeInt(signed=False, label="UInt32")}, name="CF_PROCESS_INFO", pack=False, align=None), offset=0), "RequestKey": SimTypeBottom(label="LARGE_INTEGER")}, name="CF_CALLBACK_INFO", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"ParamSize": SimTypeInt(signed=False, label="UInt32"), "Anonymous": SimUnion({"Cancel": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_CALLBACK_CANCEL_FLAGS"), "Anonymous": SimUnion({"FetchData": SimStruct({"FileOffset": SimTypeBottom(label="LARGE_INTEGER"), "Length": SimTypeBottom(label="LARGE_INTEGER")}, name="_FetchData_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="_Cancel_e__Struct", pack=False, align=None), "FetchData": SimStruct({"FileOffset": SimTypeBottom(label="LARGE_INTEGER"), "Length": SimTypeBottom(label="LARGE_INTEGER")}, name="_FetchData_e__Struct", pack=False, align=None), "ValidateData": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_CALLBACK_VALIDATE_DATA_FLAGS"), "RequiredFileOffset": SimTypeBottom(label="LARGE_INTEGER"), "RequiredLength": SimTypeBottom(label="LARGE_INTEGER")}, name="_ValidateData_e__Struct", pack=False, align=None), "FetchPlaceholders": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_CALLBACK_FETCH_PLACEHOLDERS_FLAGS"), "Pattern": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="_FetchPlaceholders_e__Struct", pack=False, align=None), "OpenCompletion": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_CALLBACK_OPEN_COMPLETION_FLAGS")}, name="_OpenCompletion_e__Struct", pack=False, align=None), "CloseCompletion": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_CALLBACK_CLOSE_COMPLETION_FLAGS")}, name="_CloseCompletion_e__Struct", pack=False, align=None), "Dehydrate": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_CALLBACK_DEHYDRATE_FLAGS"), "Reason": SimTypeInt(signed=False, label="CF_CALLBACK_DEHYDRATION_REASON")}, name="_Dehydrate_e__Struct", pack=False, align=None), "DehydrateCompletion": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS"), "Reason": SimTypeInt(signed=False, label="CF_CALLBACK_DEHYDRATION_REASON")}, name="_DehydrateCompletion_e__Struct", pack=False, align=None), "Delete": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_CALLBACK_DELETE_FLAGS")}, name="_Delete_e__Struct", pack=False, align=None), "DeleteCompletion": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_CALLBACK_DELETE_COMPLETION_FLAGS")}, name="_DeleteCompletion_e__Struct", pack=False, align=None), "Rename": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_CALLBACK_RENAME_FLAGS"), "TargetPath": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="_Rename_e__Struct", pack=False, align=None), "RenameCompletion": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_CALLBACK_RENAME_COMPLETION_FLAGS"), "SourcePath": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="_RenameCompletion_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="CF_CALLBACK_PARAMETERS", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["CallbackInfo", "CallbackParameters"]), offset=0)}, name="CF_CALLBACK_REGISTRATION", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="CF_CONNECT_FLAGS"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["SyncRootPath", "CallbackTable", "CallbackContext", "ConnectFlags", "ConnectionKey"]),
        #
        'CfDisconnectSyncRoot': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["ConnectionKey"]),
        #
        'CfGetTransferKey': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FileHandle", "TransferKey"]),
        #
        'CfReleaseTransferKey': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), offset=0)], SimTypeBottom(label="Void"), arg_names=["FileHandle", "TransferKey"]),
        #
        'CfExecute': SimTypeFunction([SimTypePointer(SimStruct({"StructSize": SimTypeInt(signed=False, label="UInt32"), "Type": SimTypeInt(signed=False, label="CF_OPERATION_TYPE"), "ConnectionKey": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "TransferKey": SimTypeBottom(label="LARGE_INTEGER"), "CorrelationVector": SimTypePointer(SimTypeBottom(label="CORRELATION_VECTOR"), offset=0), "SyncStatus": SimTypePointer(SimStruct({"StructSize": SimTypeInt(signed=False, label="UInt32"), "Code": SimTypeInt(signed=False, label="UInt32"), "DescriptionOffset": SimTypeInt(signed=False, label="UInt32"), "DescriptionLength": SimTypeInt(signed=False, label="UInt32"), "DeviceIdOffset": SimTypeInt(signed=False, label="UInt32"), "DeviceIdLength": SimTypeInt(signed=False, label="UInt32")}, name="CF_SYNC_STATUS", pack=False, align=None), offset=0), "RequestKey": SimTypeBottom(label="LARGE_INTEGER")}, name="CF_OPERATION_INFO", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"ParamSize": SimTypeInt(signed=False, label="UInt32"), "Anonymous": SimUnion({"TransferData": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_OPERATION_TRANSFER_DATA_FLAGS"), "CompletionStatus": SimTypeInt(signed=True, label="Int32"), "Buffer": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "Offset": SimTypeBottom(label="LARGE_INTEGER"), "Length": SimTypeBottom(label="LARGE_INTEGER")}, name="_TransferData_e__Struct", pack=False, align=None), "RetrieveData": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_OPERATION_RETRIEVE_DATA_FLAGS"), "Buffer": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "Offset": SimTypeBottom(label="LARGE_INTEGER"), "Length": SimTypeBottom(label="LARGE_INTEGER"), "ReturnedLength": SimTypeBottom(label="LARGE_INTEGER")}, name="_RetrieveData_e__Struct", pack=False, align=None), "AckData": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_OPERATION_ACK_DATA_FLAGS"), "CompletionStatus": SimTypeInt(signed=True, label="Int32"), "Offset": SimTypeBottom(label="LARGE_INTEGER"), "Length": SimTypeBottom(label="LARGE_INTEGER")}, name="_AckData_e__Struct", pack=False, align=None), "RestartHydration": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_OPERATION_RESTART_HYDRATION_FLAGS"), "FsMetadata": SimTypePointer(SimStruct({"BasicInfo": SimTypeBottom(label="FILE_BASIC_INFO"), "FileSize": SimTypeBottom(label="LARGE_INTEGER")}, name="CF_FS_METADATA", pack=False, align=None), offset=0), "FileIdentity": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "FileIdentityLength": SimTypeInt(signed=False, label="UInt32")}, name="_RestartHydration_e__Struct", pack=False, align=None), "TransferPlaceholders": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS"), "CompletionStatus": SimTypeInt(signed=True, label="Int32"), "PlaceholderTotalCount": SimTypeBottom(label="LARGE_INTEGER"), "PlaceholderArray": SimTypePointer(SimStruct({"RelativeFileName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "FsMetadata": SimStruct({"BasicInfo": SimTypeBottom(label="FILE_BASIC_INFO"), "FileSize": SimTypeBottom(label="LARGE_INTEGER")}, name="CF_FS_METADATA", pack=False, align=None), "FileIdentity": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "FileIdentityLength": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="CF_PLACEHOLDER_CREATE_FLAGS"), "Result": SimTypeInt(signed=True, label="Int32"), "CreateUsn": SimTypeLongLong(signed=True, label="Int64")}, name="CF_PLACEHOLDER_CREATE_INFO", pack=False, align=None), offset=0), "PlaceholderCount": SimTypeInt(signed=False, label="UInt32"), "EntriesProcessed": SimTypeInt(signed=False, label="UInt32")}, name="_TransferPlaceholders_e__Struct", pack=False, align=None), "AckDehydrate": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_OPERATION_ACK_DEHYDRATE_FLAGS"), "CompletionStatus": SimTypeInt(signed=True, label="Int32"), "FileIdentity": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "FileIdentityLength": SimTypeInt(signed=False, label="UInt32")}, name="_AckDehydrate_e__Struct", pack=False, align=None), "AckRename": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_OPERATION_ACK_RENAME_FLAGS"), "CompletionStatus": SimTypeInt(signed=True, label="Int32")}, name="_AckRename_e__Struct", pack=False, align=None), "AckDelete": SimStruct({"Flags": SimTypeInt(signed=False, label="CF_OPERATION_ACK_DELETE_FLAGS"), "CompletionStatus": SimTypeInt(signed=True, label="Int32")}, name="_AckDelete_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="CF_OPERATION_PARAMETERS", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["OpInfo", "OpParams"]),
        #
        'CfUpdateSyncProviderStatus': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="CF_SYNC_PROVIDER_STATUS")], SimTypeInt(signed=True, label="Int32"), arg_names=["ConnectionKey", "ProviderStatus"]),
        #
        'CfQuerySyncProviderStatus': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="CF_SYNC_PROVIDER_STATUS"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["ConnectionKey", "ProviderStatus"]),
        #
        'CfReportSyncStatus': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"StructSize": SimTypeInt(signed=False, label="UInt32"), "Code": SimTypeInt(signed=False, label="UInt32"), "DescriptionOffset": SimTypeInt(signed=False, label="UInt32"), "DescriptionLength": SimTypeInt(signed=False, label="UInt32"), "DeviceIdOffset": SimTypeInt(signed=False, label="UInt32"), "DeviceIdLength": SimTypeInt(signed=False, label="UInt32")}, name="CF_SYNC_STATUS", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["SyncRootPath", "SyncStatus"]),
        #
        'CfCreatePlaceholders': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"RelativeFileName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "FsMetadata": SimStruct({"BasicInfo": SimTypeBottom(label="FILE_BASIC_INFO"), "FileSize": SimTypeBottom(label="LARGE_INTEGER")}, name="CF_FS_METADATA", pack=False, align=None), "FileIdentity": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "FileIdentityLength": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="CF_PLACEHOLDER_CREATE_FLAGS"), "Result": SimTypeInt(signed=True, label="Int32"), "CreateUsn": SimTypeLongLong(signed=True, label="Int64")}, name="CF_PLACEHOLDER_CREATE_INFO", pack=False, align=None), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="CF_CREATE_FLAGS"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["BaseDirectoryPath", "PlaceholderArray", "PlaceholderCount", "CreateFlags", "EntriesProcessed"]),
        #
        'CfOpenFileWithOplock': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="CF_OPEN_FILE_FLAGS"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FilePath", "Flags", "ProtectedHandle"]),
        #
        'CfReferenceProtectedHandle': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeChar(label="Byte"), arg_names=["ProtectedHandle"]),
        #
        'CfGetWin32HandleFromProtectedHandle': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), arg_names=["ProtectedHandle"]),
        #
        'CfReleaseProtectedHandle': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeBottom(label="Void"), arg_names=["ProtectedHandle"]),
        #
        'CfCloseHandle': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeBottom(label="Void"), arg_names=["FileHandle"]),
        #
        'CfConvertToPlaceholder': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="CF_CONVERT_FLAGS"), SimTypePointer(SimTypeLongLong(signed=True, label="Int64"), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FileHandle", "FileIdentity", "FileIdentityLength", "ConvertFlags", "ConvertUsn", "Overlapped"]),
        #
        'CfUpdatePlaceholder': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"BasicInfo": SimTypeBottom(label="FILE_BASIC_INFO"), "FileSize": SimTypeBottom(label="LARGE_INTEGER")}, name="CF_FS_METADATA", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"StartingOffset": SimTypeBottom(label="LARGE_INTEGER"), "Length": SimTypeBottom(label="LARGE_INTEGER")}, name="CF_FILE_RANGE", pack=False, align=None), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="CF_UPDATE_FLAGS"), SimTypePointer(SimTypeLongLong(signed=True, label="Int64"), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FileHandle", "FsMetadata", "FileIdentity", "FileIdentityLength", "DehydrateRangeArray", "DehydrateRangeCount", "UpdateFlags", "UpdateUsn", "Overlapped"]),
        #
        'CfRevertPlaceholder': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="CF_REVERT_FLAGS"), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FileHandle", "RevertFlags", "Overlapped"]),
        #
        'CfHydratePlaceholder': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), SimTypeInt(signed=False, label="CF_HYDRATE_FLAGS"), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FileHandle", "StartingOffset", "Length", "HydrateFlags", "Overlapped"]),
        #
        'CfDehydratePlaceholder': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), SimTypeInt(signed=False, label="CF_DEHYDRATE_FLAGS"), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FileHandle", "StartingOffset", "Length", "DehydrateFlags", "Overlapped"]),
        #
        'CfSetPinState': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="CF_PIN_STATE"), SimTypeInt(signed=False, label="CF_SET_PIN_FLAGS"), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FileHandle", "PinState", "PinFlags", "Overlapped"]),
        #
        'CfSetInSyncState': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="CF_IN_SYNC_STATE"), SimTypeInt(signed=False, label="CF_SET_IN_SYNC_FLAGS"), SimTypePointer(SimTypeLongLong(signed=True, label="Int64"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FileHandle", "InSyncState", "InSyncFlags", "InSyncUsn"]),
        #
        'CfSetCorrelationVector': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Version": SimTypeChar(label="Byte"), "Vector": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 129)}, name="CORRELATION_VECTOR", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FileHandle", "CorrelationVector"]),
        #
        'CfGetCorrelationVector': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Version": SimTypeChar(label="Byte"), "Vector": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 129)}, name="CORRELATION_VECTOR", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FileHandle", "CorrelationVector"]),
        #
        'CfGetPlaceholderStateFromAttributeTag': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CF_PLACEHOLDER_STATE"), arg_names=["FileAttributes", "ReparseTag"]),
        #
        'CfGetPlaceholderStateFromFileInfo': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="FILE_INFO_BY_HANDLE_CLASS")], SimTypeInt(signed=False, label="CF_PLACEHOLDER_STATE"), arg_names=["InfoBuffer", "InfoClass"]),
        #
        'CfGetPlaceholderStateFromFindData': SimTypeFunction([SimTypePointer(SimStruct({"dwFileAttributes": SimTypeInt(signed=False, label="UInt32"), "ftCreationTime": SimStruct({"dwLowDateTime": SimTypeInt(signed=False, label="UInt32"), "dwHighDateTime": SimTypeInt(signed=False, label="UInt32")}, name="FILETIME", pack=False, align=None), "ftLastAccessTime": SimStruct({"dwLowDateTime": SimTypeInt(signed=False, label="UInt32"), "dwHighDateTime": SimTypeInt(signed=False, label="UInt32")}, name="FILETIME", pack=False, align=None), "ftLastWriteTime": SimStruct({"dwLowDateTime": SimTypeInt(signed=False, label="UInt32"), "dwHighDateTime": SimTypeInt(signed=False, label="UInt32")}, name="FILETIME", pack=False, align=None), "nFileSizeHigh": SimTypeInt(signed=False, label="UInt32"), "nFileSizeLow": SimTypeInt(signed=False, label="UInt32"), "dwReserved0": SimTypeInt(signed=False, label="UInt32"), "dwReserved1": SimTypeInt(signed=False, label="UInt32"), "cFileName": SimTypeFixedSizeArray(SimTypeBottom(label="CHAR"), 260), "cAlternateFileName": SimTypeFixedSizeArray(SimTypeBottom(label="CHAR"), 14)}, name="WIN32_FIND_DATAA", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="CF_PLACEHOLDER_STATE"), arg_names=["FindData"]),
        #
        'CfGetPlaceholderInfo': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="CF_PLACEHOLDER_INFO_CLASS"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FileHandle", "InfoClass", "InfoBuffer", "InfoBufferLength", "ReturnedLength"]),
        #
        'CfGetSyncRootInfoByPath': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="CF_SYNC_ROOT_INFO_CLASS"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FilePath", "InfoClass", "InfoBuffer", "InfoBufferLength", "ReturnedLength"]),
        #
        'CfGetSyncRootInfoByHandle': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="CF_SYNC_ROOT_INFO_CLASS"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FileHandle", "InfoClass", "InfoBuffer", "InfoBufferLength", "ReturnedLength"]),
        #
        'CfGetPlaceholderRangeInfo': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="CF_PLACEHOLDER_RANGE_INFO_CLASS"), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FileHandle", "InfoClass", "StartingOffset", "Length", "InfoBuffer", "InfoBufferLength", "ReturnedLength"]),
        #
        'CfReportProviderProgress': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None")], SimTypeInt(signed=True, label="Int32"), arg_names=["ConnectionKey", "TransferKey", "ProviderProgressTotal", "ProviderProgressCompleted"]),
        #
        'CfReportProviderProgress2': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["ConnectionKey", "TransferKey", "RequestKey", "ProviderProgressTotal", "ProviderProgressCompleted", "TargetSessionId"]),
    }

lib.set_prototypes(prototypes)
