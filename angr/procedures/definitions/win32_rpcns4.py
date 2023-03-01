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
lib.set_library_names("rpcns4.dll")
prototypes = \
    {
        #
        'RpcIfIdVectorFree': SimTypeFunction([SimTypePointer(SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "IfId": SimTypePointer(SimTypePointer(SimStruct({"Uuid": SimTypeBottom(label="Guid"), "VersMajor": SimTypeShort(signed=False, label="UInt16"), "VersMinor": SimTypeShort(signed=False, label="UInt16")}, name="RPC_IF_ID", pack=False, align=None), offset=0), offset=0)}, name="RPC_IF_ID_VECTOR", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["IfIdVector"]),
        #
        'RpcNsBindingExportA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "BindingH": SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)}, name="RPC_BINDING_VECTOR", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "Uuid": SimTypePointer(SimTypePointer(SimTypeBottom(label="Guid"), offset=0), offset=0)}, name="UUID_VECTOR", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfSpec", "BindingVec", "ObjectUuidVec"]),
        #
        'RpcNsBindingUnexportA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "Uuid": SimTypePointer(SimTypePointer(SimTypeBottom(label="Guid"), offset=0), offset=0)}, name="UUID_VECTOR", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfSpec", "ObjectUuidVec"]),
        #
        'RpcNsBindingExportW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "BindingH": SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)}, name="RPC_BINDING_VECTOR", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "Uuid": SimTypePointer(SimTypePointer(SimTypeBottom(label="Guid"), offset=0), offset=0)}, name="UUID_VECTOR", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfSpec", "BindingVec", "ObjectUuidVec"]),
        #
        'RpcNsBindingUnexportW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "Uuid": SimTypePointer(SimTypePointer(SimTypeBottom(label="Guid"), offset=0), offset=0)}, name="UUID_VECTOR", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfSpec", "ObjectUuidVec"]),
        #
        'RpcNsBindingExportPnPA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "Uuid": SimTypePointer(SimTypePointer(SimTypeBottom(label="Guid"), offset=0), offset=0)}, name="UUID_VECTOR", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfSpec", "ObjectVector"]),
        #
        'RpcNsBindingUnexportPnPA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "Uuid": SimTypePointer(SimTypePointer(SimTypeBottom(label="Guid"), offset=0), offset=0)}, name="UUID_VECTOR", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfSpec", "ObjectVector"]),
        #
        'RpcNsBindingExportPnPW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "Uuid": SimTypePointer(SimTypePointer(SimTypeBottom(label="Guid"), offset=0), offset=0)}, name="UUID_VECTOR", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfSpec", "ObjectVector"]),
        #
        'RpcNsBindingUnexportPnPW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "Uuid": SimTypePointer(SimTypePointer(SimTypeBottom(label="Guid"), offset=0), offset=0)}, name="UUID_VECTOR", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfSpec", "ObjectVector"]),
        #
        'RpcNsBindingLookupBeginA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfSpec", "ObjUuid", "BindingMaxCount", "LookupContext"]),
        #
        'RpcNsBindingLookupBeginW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfSpec", "ObjUuid", "BindingMaxCount", "LookupContext"]),
        #
        'RpcNsBindingLookupNext': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "BindingH": SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)}, name="RPC_BINDING_VECTOR", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["LookupContext", "BindingVec"]),
        #
        'RpcNsBindingLookupDone': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["LookupContext"]),
        #
        'RpcNsGroupDeleteA': SimTypeFunction([SimTypeInt(signed=False, label="GROUP_NAME_SYNTAX"), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["GroupNameSyntax", "GroupName"]),
        #
        'RpcNsGroupMbrAddA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["GroupNameSyntax", "GroupName", "MemberNameSyntax", "MemberName"]),
        #
        'RpcNsGroupMbrRemoveA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["GroupNameSyntax", "GroupName", "MemberNameSyntax", "MemberName"]),
        #
        'RpcNsGroupMbrInqBeginA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["GroupNameSyntax", "GroupName", "MemberNameSyntax", "InquiryContext"]),
        #
        'RpcNsGroupMbrInqNextA': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["InquiryContext", "MemberName"]),
        #
        'RpcNsGroupDeleteW': SimTypeFunction([SimTypeInt(signed=False, label="GROUP_NAME_SYNTAX"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["GroupNameSyntax", "GroupName"]),
        #
        'RpcNsGroupMbrAddW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["GroupNameSyntax", "GroupName", "MemberNameSyntax", "MemberName"]),
        #
        'RpcNsGroupMbrRemoveW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["GroupNameSyntax", "GroupName", "MemberNameSyntax", "MemberName"]),
        #
        'RpcNsGroupMbrInqBeginW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["GroupNameSyntax", "GroupName", "MemberNameSyntax", "InquiryContext"]),
        #
        'RpcNsGroupMbrInqNextW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["InquiryContext", "MemberName"]),
        #
        'RpcNsGroupMbrInqDone': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["InquiryContext"]),
        #
        'RpcNsProfileDeleteA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["ProfileNameSyntax", "ProfileName"]),
        #
        'RpcNsProfileEltAddA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimStruct({"Uuid": SimTypeBottom(label="Guid"), "VersMajor": SimTypeShort(signed=False, label="UInt16"), "VersMinor": SimTypeShort(signed=False, label="UInt16")}, name="RPC_IF_ID", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["ProfileNameSyntax", "ProfileName", "IfId", "MemberNameSyntax", "MemberName", "Priority", "Annotation"]),
        #
        'RpcNsProfileEltRemoveA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimStruct({"Uuid": SimTypeBottom(label="Guid"), "VersMajor": SimTypeShort(signed=False, label="UInt16"), "VersMinor": SimTypeShort(signed=False, label="UInt16")}, name="RPC_IF_ID", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["ProfileNameSyntax", "ProfileName", "IfId", "MemberNameSyntax", "MemberName"]),
        #
        'RpcNsProfileEltInqBeginA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Uuid": SimTypeBottom(label="Guid"), "VersMajor": SimTypeShort(signed=False, label="UInt16"), "VersMinor": SimTypeShort(signed=False, label="UInt16")}, name="RPC_IF_ID", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["ProfileNameSyntax", "ProfileName", "InquiryType", "IfId", "VersOption", "MemberNameSyntax", "MemberName", "InquiryContext"]),
        #
        'RpcNsProfileEltInqNextA': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"Uuid": SimTypeBottom(label="Guid"), "VersMajor": SimTypeShort(signed=False, label="UInt16"), "VersMinor": SimTypeShort(signed=False, label="UInt16")}, name="RPC_IF_ID", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["InquiryContext", "IfId", "MemberName", "Priority", "Annotation"]),
        #
        'RpcNsProfileDeleteW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["ProfileNameSyntax", "ProfileName"]),
        #
        'RpcNsProfileEltAddW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimStruct({"Uuid": SimTypeBottom(label="Guid"), "VersMajor": SimTypeShort(signed=False, label="UInt16"), "VersMinor": SimTypeShort(signed=False, label="UInt16")}, name="RPC_IF_ID", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["ProfileNameSyntax", "ProfileName", "IfId", "MemberNameSyntax", "MemberName", "Priority", "Annotation"]),
        #
        'RpcNsProfileEltRemoveW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimStruct({"Uuid": SimTypeBottom(label="Guid"), "VersMajor": SimTypeShort(signed=False, label="UInt16"), "VersMinor": SimTypeShort(signed=False, label="UInt16")}, name="RPC_IF_ID", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["ProfileNameSyntax", "ProfileName", "IfId", "MemberNameSyntax", "MemberName"]),
        #
        'RpcNsProfileEltInqBeginW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Uuid": SimTypeBottom(label="Guid"), "VersMajor": SimTypeShort(signed=False, label="UInt16"), "VersMinor": SimTypeShort(signed=False, label="UInt16")}, name="RPC_IF_ID", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["ProfileNameSyntax", "ProfileName", "InquiryType", "IfId", "VersOption", "MemberNameSyntax", "MemberName", "InquiryContext"]),
        #
        'RpcNsProfileEltInqNextW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"Uuid": SimTypeBottom(label="Guid"), "VersMajor": SimTypeShort(signed=False, label="UInt16"), "VersMinor": SimTypeShort(signed=False, label="UInt16")}, name="RPC_IF_ID", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["InquiryContext", "IfId", "MemberName", "Priority", "Annotation"]),
        #
        'RpcNsProfileEltInqDone': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["InquiryContext"]),
        #
        'RpcNsEntryObjectInqBeginA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "InquiryContext"]),
        #
        'RpcNsEntryObjectInqBeginW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "InquiryContext"]),
        #
        'RpcNsEntryObjectInqNext': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["InquiryContext", "ObjUuid"]),
        #
        'RpcNsEntryObjectInqDone': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["InquiryContext"]),
        #
        'RpcNsEntryExpandNameA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "ExpandedName"]),
        #
        'RpcNsMgmtBindingUnexportA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimStruct({"Uuid": SimTypeBottom(label="Guid"), "VersMajor": SimTypeShort(signed=False, label="UInt16"), "VersMinor": SimTypeShort(signed=False, label="UInt16")}, name="RPC_IF_ID", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "Uuid": SimTypePointer(SimTypePointer(SimTypeBottom(label="Guid"), offset=0), offset=0)}, name="UUID_VECTOR", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfId", "VersOption", "ObjectUuidVec"]),
        #
        'RpcNsMgmtEntryCreateA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName"]),
        #
        'RpcNsMgmtEntryDeleteA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName"]),
        #
        'RpcNsMgmtEntryInqIfIdsA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "IfId": SimTypePointer(SimTypePointer(SimStruct({"Uuid": SimTypeBottom(label="Guid"), "VersMajor": SimTypeShort(signed=False, label="UInt16"), "VersMinor": SimTypeShort(signed=False, label="UInt16")}, name="RPC_IF_ID", pack=False, align=None), offset=0), offset=0)}, name="RPC_IF_ID_VECTOR", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfIdVec"]),
        #
        'RpcNsMgmtHandleSetExpAge': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["NsHandle", "ExpirationAge"]),
        #
        'RpcNsMgmtInqExpAge': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["ExpirationAge"]),
        #
        'RpcNsMgmtSetExpAge': SimTypeFunction([SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["ExpirationAge"]),
        #
        'RpcNsEntryExpandNameW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "ExpandedName"]),
        #
        'RpcNsMgmtBindingUnexportW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimStruct({"Uuid": SimTypeBottom(label="Guid"), "VersMajor": SimTypeShort(signed=False, label="UInt16"), "VersMinor": SimTypeShort(signed=False, label="UInt16")}, name="RPC_IF_ID", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "Uuid": SimTypePointer(SimTypePointer(SimTypeBottom(label="Guid"), offset=0), offset=0)}, name="UUID_VECTOR", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfId", "VersOption", "ObjectUuidVec"]),
        #
        'RpcNsMgmtEntryCreateW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName"]),
        #
        'RpcNsMgmtEntryDeleteW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName"]),
        #
        'RpcNsMgmtEntryInqIfIdsW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "IfId": SimTypePointer(SimTypePointer(SimStruct({"Uuid": SimTypeBottom(label="Guid"), "VersMajor": SimTypeShort(signed=False, label="UInt16"), "VersMinor": SimTypeShort(signed=False, label="UInt16")}, name="RPC_IF_ID", pack=False, align=None), offset=0), offset=0)}, name="RPC_IF_ID_VECTOR", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfIdVec"]),
        #
        'RpcNsBindingImportBeginA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfSpec", "ObjUuid", "ImportContext"]),
        #
        'RpcNsBindingImportBeginW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["EntryNameSyntax", "EntryName", "IfSpec", "ObjUuid", "ImportContext"]),
        #
        'RpcNsBindingImportNext': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["ImportContext", "Binding"]),
        #
        'RpcNsBindingImportDone': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["ImportContext"]),
        #
        'RpcNsBindingSelect': SimTypeFunction([SimTypePointer(SimStruct({"Count": SimTypeInt(signed=False, label="UInt32"), "BindingH": SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)}, name="RPC_BINDING_VECTOR", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["BindingVec", "Binding"]),
        #
        'I_RpcNsGetBuffer': SimTypeFunction([SimTypePointer(SimStruct({"Handle": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "DataRepresentation": SimTypeInt(signed=False, label="UInt32"), "Buffer": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "BufferLength": SimTypeInt(signed=False, label="UInt32"), "ProcNum": SimTypeInt(signed=False, label="UInt32"), "TransferSyntax": SimTypePointer(SimStruct({"SyntaxGUID": SimTypeBottom(label="Guid"), "SyntaxVersion": SimStruct({"MajorVersion": SimTypeShort(signed=False, label="UInt16"), "MinorVersion": SimTypeShort(signed=False, label="UInt16")}, name="RPC_VERSION", pack=False, align=None)}, name="RPC_SYNTAX_IDENTIFIER", pack=False, align=None), offset=0), "RpcInterfaceInformation": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ReservedForRuntime": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ManagerEpv": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ImportContext": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "RpcFlags": SimTypeInt(signed=False, label="UInt32")}, name="RPC_MESSAGE", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["Message"]),
        #
        'I_RpcNsSendReceive': SimTypeFunction([SimTypePointer(SimStruct({"Handle": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "DataRepresentation": SimTypeInt(signed=False, label="UInt32"), "Buffer": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "BufferLength": SimTypeInt(signed=False, label="UInt32"), "ProcNum": SimTypeInt(signed=False, label="UInt32"), "TransferSyntax": SimTypePointer(SimStruct({"SyntaxGUID": SimTypeBottom(label="Guid"), "SyntaxVersion": SimStruct({"MajorVersion": SimTypeShort(signed=False, label="UInt16"), "MinorVersion": SimTypeShort(signed=False, label="UInt16")}, name="RPC_VERSION", pack=False, align=None)}, name="RPC_SYNTAX_IDENTIFIER", pack=False, align=None), offset=0), "RpcInterfaceInformation": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ReservedForRuntime": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ManagerEpv": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ImportContext": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "RpcFlags": SimTypeInt(signed=False, label="UInt32")}, name="RPC_MESSAGE", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["Message", "Handle"]),
        #
        'I_RpcNsRaiseException': SimTypeFunction([SimTypePointer(SimStruct({"Handle": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "DataRepresentation": SimTypeInt(signed=False, label="UInt32"), "Buffer": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "BufferLength": SimTypeInt(signed=False, label="UInt32"), "ProcNum": SimTypeInt(signed=False, label="UInt32"), "TransferSyntax": SimTypePointer(SimStruct({"SyntaxGUID": SimTypeBottom(label="Guid"), "SyntaxVersion": SimStruct({"MajorVersion": SimTypeShort(signed=False, label="UInt16"), "MinorVersion": SimTypeShort(signed=False, label="UInt16")}, name="RPC_VERSION", pack=False, align=None)}, name="RPC_SYNTAX_IDENTIFIER", pack=False, align=None), offset=0), "RpcInterfaceInformation": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ReservedForRuntime": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ManagerEpv": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ImportContext": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "RpcFlags": SimTypeInt(signed=False, label="UInt32")}, name="RPC_MESSAGE", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="RPC_STATUS")], SimTypeBottom(label="Void"), arg_names=["Message", "Status"]),
        #
        'I_RpcReBindBuffer': SimTypeFunction([SimTypePointer(SimStruct({"Handle": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "DataRepresentation": SimTypeInt(signed=False, label="UInt32"), "Buffer": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "BufferLength": SimTypeInt(signed=False, label="UInt32"), "ProcNum": SimTypeInt(signed=False, label="UInt32"), "TransferSyntax": SimTypePointer(SimStruct({"SyntaxGUID": SimTypeBottom(label="Guid"), "SyntaxVersion": SimStruct({"MajorVersion": SimTypeShort(signed=False, label="UInt16"), "MinorVersion": SimTypeShort(signed=False, label="UInt16")}, name="RPC_VERSION", pack=False, align=None)}, name="RPC_SYNTAX_IDENTIFIER", pack=False, align=None), offset=0), "RpcInterfaceInformation": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ReservedForRuntime": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ManagerEpv": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ImportContext": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "RpcFlags": SimTypeInt(signed=False, label="UInt32")}, name="RPC_MESSAGE", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="RPC_STATUS"), arg_names=["Message"]),
    }

lib.set_prototypes(prototypes)
