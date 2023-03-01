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
lib.set_library_names("eappcfg.dll")
prototypes = \
    {
        #
        'EapHostPeerGetMethods': SimTypeFunction([SimTypePointer(SimStruct({"dwNumberOfMethods": SimTypeInt(signed=False, label="UInt32"), "pEapMethods": SimTypePointer(SimStruct({"eaptype": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "pwszAuthorName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszFriendlyName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "eapProperties": SimTypeInt(signed=False, label="UInt32"), "pInnerMethodInfo": SimTypePointer(SimTypeBottom(label="EAP_METHOD_INFO"), offset=0)}, name="EAP_METHOD_INFO", pack=False, align=None), offset=0)}, name="EAP_METHOD_INFO_ARRAY", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwWinError": SimTypeInt(signed=False, label="UInt32"), "type": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "dwReasonCode": SimTypeInt(signed=False, label="UInt32"), "rootCauseGuid": SimTypeBottom(label="Guid"), "repairGuid": SimTypeBottom(label="Guid"), "helpLinkGuid": SimTypeBottom(label="Guid"), "pRootCauseString": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pRepairString": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="EAP_ERROR", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["pEapMethodInfoArray", "ppEapError"]),
        #
        'EapHostPeerGetMethodProperties': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimStruct({"dwNumberOfProperties": SimTypeInt(signed=False, label="UInt32"), "pMethodProperty": SimTypePointer(SimStruct({"eapMethodPropertyType": SimTypeInt(signed=False, label="EAP_METHOD_PROPERTY_TYPE"), "eapMethodPropertyValueType": SimTypeInt(signed=False, label="EAP_METHOD_PROPERTY_VALUE_TYPE"), "eapMethodPropertyValue": SimUnion({"empvBool": SimStruct({"length": SimTypeInt(signed=False, label="UInt32"), "value": SimTypeInt(signed=True, label="Int32")}, name="EAP_METHOD_PROPERTY_VALUE_BOOL", pack=False, align=None), "empvDword": SimStruct({"length": SimTypeInt(signed=False, label="UInt32"), "value": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_PROPERTY_VALUE_DWORD", pack=False, align=None), "empvString": SimStruct({"length": SimTypeInt(signed=False, label="UInt32"), "value": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="EAP_METHOD_PROPERTY_VALUE_STRING", pack=False, align=None)}, name="<anon>", label="None")}, name="EAP_METHOD_PROPERTY", pack=False, align=None), offset=0)}, name="EAP_METHOD_PROPERTY_ARRAY", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwWinError": SimTypeInt(signed=False, label="UInt32"), "type": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "dwReasonCode": SimTypeInt(signed=False, label="UInt32"), "rootCauseGuid": SimTypeBottom(label="Guid"), "repairGuid": SimTypeBottom(label="Guid"), "helpLinkGuid": SimTypeBottom(label="Guid"), "pRootCauseString": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pRepairString": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="EAP_ERROR", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["dwVersion", "dwFlags", "eapMethodType", "hUserImpersonationToken", "dwEapConnDataSize", "pbEapConnData", "dwUserDataSize", "pbUserData", "pMethodPropertyArray", "ppEapError"]),
        #
        'EapHostPeerInvokeConfigUI': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwWinError": SimTypeInt(signed=False, label="UInt32"), "type": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "dwReasonCode": SimTypeInt(signed=False, label="UInt32"), "rootCauseGuid": SimTypeBottom(label="Guid"), "repairGuid": SimTypeBottom(label="Guid"), "helpLinkGuid": SimTypeBottom(label="Guid"), "pRootCauseString": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pRepairString": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="EAP_ERROR", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwndParent", "dwFlags", "eapMethodType", "dwSizeOfConfigIn", "pConfigIn", "pdwSizeOfConfigOut", "ppConfigOut", "ppEapError"]),
        #
        'EapHostPeerQueryCredentialInputFields': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimStruct({"dwVersion": SimTypeInt(signed=False, label="UInt32"), "dwNumberOfFields": SimTypeInt(signed=False, label="UInt32"), "pFields": SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Type": SimTypeInt(signed=False, label="EAP_CONFIG_INPUT_FIELD_TYPE"), "dwFlagProps": SimTypeInt(signed=False, label="UInt32"), "pwszLabel": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszData": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwMinDataLength": SimTypeInt(signed=False, label="UInt32"), "dwMaxDataLength": SimTypeInt(signed=False, label="UInt32")}, name="EAP_CONFIG_INPUT_FIELD_DATA", pack=False, align=None), offset=0)}, name="EAP_CONFIG_INPUT_FIELD_ARRAY", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwWinError": SimTypeInt(signed=False, label="UInt32"), "type": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "dwReasonCode": SimTypeInt(signed=False, label="UInt32"), "rootCauseGuid": SimTypeBottom(label="Guid"), "repairGuid": SimTypeBottom(label="Guid"), "helpLinkGuid": SimTypeBottom(label="Guid"), "pRootCauseString": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pRepairString": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="EAP_ERROR", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hUserImpersonationToken", "eapMethodType", "dwFlags", "dwEapConnDataSize", "pbEapConnData", "pEapConfigInputFieldArray", "ppEapError"]),
        #
        'EapHostPeerQueryUserBlobFromCredentialInputFields': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimStruct({"dwVersion": SimTypeInt(signed=False, label="UInt32"), "dwNumberOfFields": SimTypeInt(signed=False, label="UInt32"), "pFields": SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Type": SimTypeInt(signed=False, label="EAP_CONFIG_INPUT_FIELD_TYPE"), "dwFlagProps": SimTypeInt(signed=False, label="UInt32"), "pwszLabel": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszData": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwMinDataLength": SimTypeInt(signed=False, label="UInt32"), "dwMaxDataLength": SimTypeInt(signed=False, label="UInt32")}, name="EAP_CONFIG_INPUT_FIELD_DATA", pack=False, align=None), offset=0)}, name="EAP_CONFIG_INPUT_FIELD_ARRAY", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), label="LPArray", offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwWinError": SimTypeInt(signed=False, label="UInt32"), "type": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "dwReasonCode": SimTypeInt(signed=False, label="UInt32"), "rootCauseGuid": SimTypeBottom(label="Guid"), "repairGuid": SimTypeBottom(label="Guid"), "helpLinkGuid": SimTypeBottom(label="Guid"), "pRootCauseString": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pRepairString": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="EAP_ERROR", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hUserImpersonationToken", "eapMethodType", "dwFlags", "dwEapConnDataSize", "pbEapConnData", "pEapConfigInputFieldArray", "pdwUserBlobSize", "ppbUserBlob", "ppEapError"]),
        #
        'EapHostPeerInvokeIdentityUI': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwWinError": SimTypeInt(signed=False, label="UInt32"), "type": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "dwReasonCode": SimTypeInt(signed=False, label="UInt32"), "rootCauseGuid": SimTypeBottom(label="Guid"), "repairGuid": SimTypeBottom(label="Guid"), "helpLinkGuid": SimTypeBottom(label="Guid"), "pRootCauseString": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pRepairString": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="EAP_ERROR", pack=False, align=None), offset=0), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["dwVersion", "eapMethodType", "dwFlags", "hwndParent", "dwSizeofConnectionData", "pConnectionData", "dwSizeofUserData", "pUserData", "pdwSizeOfUserDataOut", "ppUserDataOut", "ppwszIdentity", "ppEapError", "ppvReserved"]),
        #
        'EapHostPeerInvokeInteractiveUI': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwWinError": SimTypeInt(signed=False, label="UInt32"), "type": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "dwReasonCode": SimTypeInt(signed=False, label="UInt32"), "rootCauseGuid": SimTypeBottom(label="Guid"), "repairGuid": SimTypeBottom(label="Guid"), "helpLinkGuid": SimTypeBottom(label="Guid"), "pRootCauseString": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pRepairString": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="EAP_ERROR", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwndParent", "dwSizeofUIContextData", "pUIContextData", "pdwSizeOfDataFromInteractiveUI", "ppDataFromInteractiveUI", "ppEapError"]),
        #
        'EapHostPeerQueryInteractiveUIInputFields': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimStruct({"dwVersion": SimTypeInt(signed=False, label="UInt32"), "dwSize": SimTypeInt(signed=False, label="UInt32"), "dwDataType": SimTypeInt(signed=False, label="EAP_INTERACTIVE_UI_DATA_TYPE"), "cbUiData": SimTypeInt(signed=False, label="UInt32"), "pbUiData": SimUnion({"credData": SimTypePointer(SimStruct({"dwVersion": SimTypeInt(signed=False, label="UInt32"), "dwNumberOfFields": SimTypeInt(signed=False, label="UInt32"), "pFields": SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Type": SimTypeInt(signed=False, label="EAP_CONFIG_INPUT_FIELD_TYPE"), "dwFlagProps": SimTypeInt(signed=False, label="UInt32"), "pwszLabel": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszData": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwMinDataLength": SimTypeInt(signed=False, label="UInt32"), "dwMaxDataLength": SimTypeInt(signed=False, label="UInt32")}, name="EAP_CONFIG_INPUT_FIELD_DATA", pack=False, align=None), offset=0)}, name="EAP_CONFIG_INPUT_FIELD_ARRAY", pack=False, align=None), offset=0), "credExpiryData": SimTypePointer(SimStruct({"curCreds": SimStruct({"dwVersion": SimTypeInt(signed=False, label="UInt32"), "dwNumberOfFields": SimTypeInt(signed=False, label="UInt32"), "pFields": SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Type": SimTypeInt(signed=False, label="EAP_CONFIG_INPUT_FIELD_TYPE"), "dwFlagProps": SimTypeInt(signed=False, label="UInt32"), "pwszLabel": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszData": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwMinDataLength": SimTypeInt(signed=False, label="UInt32"), "dwMaxDataLength": SimTypeInt(signed=False, label="UInt32")}, name="EAP_CONFIG_INPUT_FIELD_DATA", pack=False, align=None), offset=0)}, name="EAP_CONFIG_INPUT_FIELD_ARRAY", pack=False, align=None), "newCreds": SimStruct({"dwVersion": SimTypeInt(signed=False, label="UInt32"), "dwNumberOfFields": SimTypeInt(signed=False, label="UInt32"), "pFields": SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Type": SimTypeInt(signed=False, label="EAP_CONFIG_INPUT_FIELD_TYPE"), "dwFlagProps": SimTypeInt(signed=False, label="UInt32"), "pwszLabel": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszData": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwMinDataLength": SimTypeInt(signed=False, label="UInt32"), "dwMaxDataLength": SimTypeInt(signed=False, label="UInt32")}, name="EAP_CONFIG_INPUT_FIELD_DATA", pack=False, align=None), offset=0)}, name="EAP_CONFIG_INPUT_FIELD_ARRAY", pack=False, align=None)}, name="EAP_CRED_EXPIRY_REQ", pack=False, align=None), offset=0), "credLogonData": SimTypePointer(SimStruct({"dwVersion": SimTypeInt(signed=False, label="UInt32"), "dwNumberOfFields": SimTypeInt(signed=False, label="UInt32"), "pFields": SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Type": SimTypeInt(signed=False, label="EAP_CONFIG_INPUT_FIELD_TYPE"), "dwFlagProps": SimTypeInt(signed=False, label="UInt32"), "pwszLabel": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszData": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwMinDataLength": SimTypeInt(signed=False, label="UInt32"), "dwMaxDataLength": SimTypeInt(signed=False, label="UInt32")}, name="EAP_CONFIG_INPUT_FIELD_DATA", pack=False, align=None), offset=0)}, name="EAP_CONFIG_INPUT_FIELD_ARRAY", pack=False, align=None), offset=0)}, name="<anon>", label="None")}, name="EAP_INTERACTIVE_UI_DATA", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwWinError": SimTypeInt(signed=False, label="UInt32"), "type": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "dwReasonCode": SimTypeInt(signed=False, label="UInt32"), "rootCauseGuid": SimTypeBottom(label="Guid"), "repairGuid": SimTypeBottom(label="Guid"), "helpLinkGuid": SimTypeBottom(label="Guid"), "pRootCauseString": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pRepairString": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="EAP_ERROR", pack=False, align=None), offset=0), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["dwVersion", "dwFlags", "dwSizeofUIContextData", "pUIContextData", "pEapInteractiveUIData", "ppEapError", "ppvReserved"]),
        #
        'EapHostPeerQueryUIBlobFromInteractiveUIInputFields': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimStruct({"dwVersion": SimTypeInt(signed=False, label="UInt32"), "dwSize": SimTypeInt(signed=False, label="UInt32"), "dwDataType": SimTypeInt(signed=False, label="EAP_INTERACTIVE_UI_DATA_TYPE"), "cbUiData": SimTypeInt(signed=False, label="UInt32"), "pbUiData": SimUnion({"credData": SimTypePointer(SimStruct({"dwVersion": SimTypeInt(signed=False, label="UInt32"), "dwNumberOfFields": SimTypeInt(signed=False, label="UInt32"), "pFields": SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Type": SimTypeInt(signed=False, label="EAP_CONFIG_INPUT_FIELD_TYPE"), "dwFlagProps": SimTypeInt(signed=False, label="UInt32"), "pwszLabel": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszData": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwMinDataLength": SimTypeInt(signed=False, label="UInt32"), "dwMaxDataLength": SimTypeInt(signed=False, label="UInt32")}, name="EAP_CONFIG_INPUT_FIELD_DATA", pack=False, align=None), offset=0)}, name="EAP_CONFIG_INPUT_FIELD_ARRAY", pack=False, align=None), offset=0), "credExpiryData": SimTypePointer(SimStruct({"curCreds": SimStruct({"dwVersion": SimTypeInt(signed=False, label="UInt32"), "dwNumberOfFields": SimTypeInt(signed=False, label="UInt32"), "pFields": SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Type": SimTypeInt(signed=False, label="EAP_CONFIG_INPUT_FIELD_TYPE"), "dwFlagProps": SimTypeInt(signed=False, label="UInt32"), "pwszLabel": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszData": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwMinDataLength": SimTypeInt(signed=False, label="UInt32"), "dwMaxDataLength": SimTypeInt(signed=False, label="UInt32")}, name="EAP_CONFIG_INPUT_FIELD_DATA", pack=False, align=None), offset=0)}, name="EAP_CONFIG_INPUT_FIELD_ARRAY", pack=False, align=None), "newCreds": SimStruct({"dwVersion": SimTypeInt(signed=False, label="UInt32"), "dwNumberOfFields": SimTypeInt(signed=False, label="UInt32"), "pFields": SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Type": SimTypeInt(signed=False, label="EAP_CONFIG_INPUT_FIELD_TYPE"), "dwFlagProps": SimTypeInt(signed=False, label="UInt32"), "pwszLabel": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszData": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwMinDataLength": SimTypeInt(signed=False, label="UInt32"), "dwMaxDataLength": SimTypeInt(signed=False, label="UInt32")}, name="EAP_CONFIG_INPUT_FIELD_DATA", pack=False, align=None), offset=0)}, name="EAP_CONFIG_INPUT_FIELD_ARRAY", pack=False, align=None)}, name="EAP_CRED_EXPIRY_REQ", pack=False, align=None), offset=0), "credLogonData": SimTypePointer(SimStruct({"dwVersion": SimTypeInt(signed=False, label="UInt32"), "dwNumberOfFields": SimTypeInt(signed=False, label="UInt32"), "pFields": SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Type": SimTypeInt(signed=False, label="EAP_CONFIG_INPUT_FIELD_TYPE"), "dwFlagProps": SimTypeInt(signed=False, label="UInt32"), "pwszLabel": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszData": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwMinDataLength": SimTypeInt(signed=False, label="UInt32"), "dwMaxDataLength": SimTypeInt(signed=False, label="UInt32")}, name="EAP_CONFIG_INPUT_FIELD_DATA", pack=False, align=None), offset=0)}, name="EAP_CONFIG_INPUT_FIELD_ARRAY", pack=False, align=None), offset=0)}, name="<anon>", label="None")}, name="EAP_INTERACTIVE_UI_DATA", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwWinError": SimTypeInt(signed=False, label="UInt32"), "type": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "dwReasonCode": SimTypeInt(signed=False, label="UInt32"), "rootCauseGuid": SimTypeBottom(label="Guid"), "repairGuid": SimTypeBottom(label="Guid"), "helpLinkGuid": SimTypeBottom(label="Guid"), "pRootCauseString": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pRepairString": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="EAP_ERROR", pack=False, align=None), offset=0), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["dwVersion", "dwFlags", "dwSizeofUIContextData", "pUIContextData", "pEapInteractiveUIData", "pdwSizeOfDataFromInteractiveUI", "ppDataFromInteractiveUI", "ppEapError", "ppvReserved"]),
        #
        'EapHostPeerConfigXml2Blob': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeBottom(label="IXMLDOMNode"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), offset=0), SimTypePointer(SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwWinError": SimTypeInt(signed=False, label="UInt32"), "type": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "dwReasonCode": SimTypeInt(signed=False, label="UInt32"), "rootCauseGuid": SimTypeBottom(label="Guid"), "repairGuid": SimTypeBottom(label="Guid"), "helpLinkGuid": SimTypeBottom(label="Guid"), "pRootCauseString": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pRepairString": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="EAP_ERROR", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["dwFlags", "pConfigDoc", "pdwSizeOfConfigOut", "ppConfigOut", "pEapMethodType", "ppEapError"]),
        #
        'EapHostPeerCredentialsXml2Blob': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeBottom(label="IXMLDOMNode"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), offset=0), SimTypePointer(SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwWinError": SimTypeInt(signed=False, label="UInt32"), "type": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "dwReasonCode": SimTypeInt(signed=False, label="UInt32"), "rootCauseGuid": SimTypeBottom(label="Guid"), "repairGuid": SimTypeBottom(label="Guid"), "helpLinkGuid": SimTypeBottom(label="Guid"), "pRootCauseString": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pRepairString": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="EAP_ERROR", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["dwFlags", "pCredentialsDoc", "dwSizeOfConfigIn", "pConfigIn", "pdwSizeOfCredentialsOut", "ppCredentialsOut", "pEapMethodType", "ppEapError"]),
        #
        'EapHostPeerConfigBlob2Xml': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeBottom(label="IXMLDOMDocument2"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwWinError": SimTypeInt(signed=False, label="UInt32"), "type": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "dwReasonCode": SimTypeInt(signed=False, label="UInt32"), "rootCauseGuid": SimTypeBottom(label="Guid"), "repairGuid": SimTypeBottom(label="Guid"), "helpLinkGuid": SimTypeBottom(label="Guid"), "pRootCauseString": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pRepairString": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="EAP_ERROR", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["dwFlags", "eapMethodType", "dwSizeOfConfigIn", "pConfigIn", "ppConfigDoc", "ppEapError"]),
        #
        'EapHostPeerFreeMemory': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeBottom(label="Void"), arg_names=["pData"]),
        #
        'EapHostPeerFreeErrorMemory': SimTypeFunction([SimTypePointer(SimStruct({"dwWinError": SimTypeInt(signed=False, label="UInt32"), "type": SimStruct({"eapType": SimStruct({"type": SimTypeChar(label="Byte"), "dwVendorId": SimTypeInt(signed=False, label="UInt32"), "dwVendorType": SimTypeInt(signed=False, label="UInt32")}, name="EAP_TYPE", pack=False, align=None), "dwAuthorId": SimTypeInt(signed=False, label="UInt32")}, name="EAP_METHOD_TYPE", pack=False, align=None), "dwReasonCode": SimTypeInt(signed=False, label="UInt32"), "rootCauseGuid": SimTypeBottom(label="Guid"), "repairGuid": SimTypeBottom(label="Guid"), "helpLinkGuid": SimTypeBottom(label="Guid"), "pRootCauseString": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pRepairString": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="EAP_ERROR", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["pEapError"]),
    }

lib.set_prototypes(prototypes)
