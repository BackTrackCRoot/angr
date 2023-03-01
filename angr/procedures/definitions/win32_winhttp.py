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
lib.set_library_names("winhttp.dll")
prototypes = \
    {
        #
        'WinHttpSetStatusCallback': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeBottom(label="Void"), arg_names=["hInternet", "dwContext", "dwInternetStatus", "lpvStatusInformation", "dwStatusInformationLength"]), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0)], SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeBottom(label="Void"), arg_names=["hInternet", "dwContext", "dwInternetStatus", "lpvStatusInformation", "dwStatusInformationLength"]), offset=0), arg_names=["hInternet", "lpfnInternetCallback", "dwNotificationFlags", "dwReserved"]),
        #
        'WinHttpTimeFromSystemTime': SimTypeFunction([SimTypePointer(SimStruct({"wYear": SimTypeShort(signed=False, label="UInt16"), "wMonth": SimTypeShort(signed=False, label="UInt16"), "wDayOfWeek": SimTypeShort(signed=False, label="UInt16"), "wDay": SimTypeShort(signed=False, label="UInt16"), "wHour": SimTypeShort(signed=False, label="UInt16"), "wMinute": SimTypeShort(signed=False, label="UInt16"), "wSecond": SimTypeShort(signed=False, label="UInt16"), "wMilliseconds": SimTypeShort(signed=False, label="UInt16")}, name="SYSTEMTIME", pack=False, align=None), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pst", "pwszTime"]),
        #
        'WinHttpTimeToSystemTime': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"wYear": SimTypeShort(signed=False, label="UInt16"), "wMonth": SimTypeShort(signed=False, label="UInt16"), "wDayOfWeek": SimTypeShort(signed=False, label="UInt16"), "wDay": SimTypeShort(signed=False, label="UInt16"), "wHour": SimTypeShort(signed=False, label="UInt16"), "wMinute": SimTypeShort(signed=False, label="UInt16"), "wSecond": SimTypeShort(signed=False, label="UInt16"), "wMilliseconds": SimTypeShort(signed=False, label="UInt16")}, name="SYSTEMTIME", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pwszTime", "pst"]),
        #
        'WinHttpCrackUrl': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"dwStructSize": SimTypeInt(signed=False, label="UInt32"), "lpszScheme": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwSchemeLength": SimTypeInt(signed=False, label="UInt32"), "nScheme": SimTypeInt(signed=False, label="WINHTTP_INTERNET_SCHEME"), "lpszHostName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwHostNameLength": SimTypeInt(signed=False, label="UInt32"), "nPort": SimTypeShort(signed=False, label="UInt16"), "lpszUserName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwUserNameLength": SimTypeInt(signed=False, label="UInt32"), "lpszPassword": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwPasswordLength": SimTypeInt(signed=False, label="UInt32"), "lpszUrlPath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwUrlPathLength": SimTypeInt(signed=False, label="UInt32"), "lpszExtraInfo": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwExtraInfoLength": SimTypeInt(signed=False, label="UInt32")}, name="URL_COMPONENTS", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pwszUrl", "dwUrlLength", "dwFlags", "lpUrlComponents"]),
        #
        'WinHttpCreateUrl': SimTypeFunction([SimTypePointer(SimStruct({"dwStructSize": SimTypeInt(signed=False, label="UInt32"), "lpszScheme": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwSchemeLength": SimTypeInt(signed=False, label="UInt32"), "nScheme": SimTypeInt(signed=False, label="WINHTTP_INTERNET_SCHEME"), "lpszHostName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwHostNameLength": SimTypeInt(signed=False, label="UInt32"), "nPort": SimTypeShort(signed=False, label="UInt16"), "lpszUserName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwUserNameLength": SimTypeInt(signed=False, label="UInt32"), "lpszPassword": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwPasswordLength": SimTypeInt(signed=False, label="UInt32"), "lpszUrlPath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwUrlPathLength": SimTypeInt(signed=False, label="UInt32"), "lpszExtraInfo": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwExtraInfoLength": SimTypeInt(signed=False, label="UInt32")}, name="URL_COMPONENTS", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="WIN_HTTP_CREATE_URL_FLAGS"), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["lpUrlComponents", "dwFlags", "pwszUrl", "pdwUrlLength"]),
        #
        'WinHttpCheckPlatform': SimTypeFunction([], SimTypeInt(signed=True, label="Int32")),
        #
        'WinHttpGetDefaultProxyConfiguration': SimTypeFunction([SimTypePointer(SimStruct({"dwAccessType": SimTypeInt(signed=False, label="WINHTTP_ACCESS_TYPE"), "lpszProxy": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpszProxyBypass": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="WINHTTP_PROXY_INFO", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pProxyInfo"]),
        #
        'WinHttpSetDefaultProxyConfiguration': SimTypeFunction([SimTypePointer(SimStruct({"dwAccessType": SimTypeInt(signed=False, label="WINHTTP_ACCESS_TYPE"), "lpszProxy": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpszProxyBypass": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="WINHTTP_PROXY_INFO", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pProxyInfo"]),
        #
        'WinHttpOpen': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="WINHTTP_ACCESS_TYPE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypePointer(SimTypeBottom(label="Void"), offset=0), arg_names=["pszAgentW", "dwAccessType", "pszProxyW", "pszProxyBypassW", "dwFlags"]),
        #
        'WinHttpCloseHandle': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hInternet"]),
        #
        'WinHttpConnect': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="INTERNET_PORT"), SimTypeInt(signed=False, label="UInt32")], SimTypePointer(SimTypeBottom(label="Void"), offset=0), arg_names=["hSession", "pswzServerName", "nServerPort", "dwReserved"]),
        #
        'WinHttpReadData': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hRequest", "lpBuffer", "dwNumberOfBytesToRead", "lpdwNumberOfBytesRead"]),
        #
        'WinHttpWriteData': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hRequest", "lpBuffer", "dwNumberOfBytesToWrite", "lpdwNumberOfBytesWritten"]),
        #
        'WinHttpQueryDataAvailable': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hRequest", "lpdwNumberOfBytesAvailable"]),
        #
        'WinHttpQueryOption': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hInternet", "dwOption", "lpBuffer", "lpdwBufferLength"]),
        #
        'WinHttpSetOption': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hInternet", "dwOption", "lpBuffer", "dwBufferLength"]),
        #
        'WinHttpSetTimeouts': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hInternet", "nResolveTimeout", "nConnectTimeout", "nSendTimeout", "nReceiveTimeout"]),
        #
        'WinHttpOpenRequest': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), SimTypeInt(signed=False, label="WINHTTP_OPEN_REQUEST_FLAGS")], SimTypePointer(SimTypeBottom(label="Void"), offset=0), arg_names=["hConnect", "pwszVerb", "pwszObjectName", "pwszVersion", "pwszReferrer", "ppwszAcceptTypes", "dwFlags"]),
        #
        'WinHttpAddRequestHeaders': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hRequest", "lpszHeaders", "dwHeadersLength", "dwModifiers"]),
        #
        'WinHttpAddRequestHeadersEx': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeLongLong(signed=False, label="UInt64"), SimTypeLongLong(signed=False, label="UInt64"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Anonymous1": SimUnion({"pwszName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszName": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="<anon>", label="None"), "Anonymous2": SimUnion({"pwszValue": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszValue": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="<anon>", label="None")}, name="WINHTTP_EXTENDED_HEADER", pack=False, align=None), label="LPArray", offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hRequest", "dwModifiers", "ullFlags", "ullExtra", "cHeaders", "pHeaders"]),
        #
        'WinHttpSendRequest': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hRequest", "lpszHeaders", "dwHeadersLength", "lpOptional", "dwOptionalLength", "dwTotalLength", "dwContext"]),
        #
        'WinHttpSetCredentials': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hRequest", "AuthTargets", "AuthScheme", "pwszUserName", "pwszPassword", "pAuthParams"]),
        #
        'WinHttpQueryAuthSchemes': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hRequest", "lpdwSupportedSchemes", "lpdwFirstScheme", "pdwAuthTarget"]),
        #
        'WinHttpReceiveResponse': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hRequest", "lpReserved"]),
        #
        'WinHttpQueryHeaders': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hRequest", "dwInfoLevel", "pwszName", "lpBuffer", "lpdwBufferLength", "lpdwIndex"]),
        #
        'WinHttpDetectAutoProxyConfigUrl': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwAutoDetectFlags", "ppwstrAutoConfigUrl"]),
        #
        'WinHttpGetProxyForUrl': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"dwFlags": SimTypeInt(signed=False, label="UInt32"), "dwAutoDetectFlags": SimTypeInt(signed=False, label="UInt32"), "lpszAutoConfigUrl": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpvReserved": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwReserved": SimTypeInt(signed=False, label="UInt32"), "fAutoLogonIfChallenged": SimTypeInt(signed=True, label="Int32")}, name="WINHTTP_AUTOPROXY_OPTIONS", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"dwAccessType": SimTypeInt(signed=False, label="WINHTTP_ACCESS_TYPE"), "lpszProxy": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpszProxyBypass": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="WINHTTP_PROXY_INFO", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hSession", "lpcwszUrl", "pAutoProxyOptions", "pProxyInfo"]),
        #
        'WinHttpCreateProxyResolver': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hSession", "phResolver"]),
        #
        'WinHttpGetProxyForUrlEx': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"dwFlags": SimTypeInt(signed=False, label="UInt32"), "dwAutoDetectFlags": SimTypeInt(signed=False, label="UInt32"), "lpszAutoConfigUrl": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpvReserved": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwReserved": SimTypeInt(signed=False, label="UInt32"), "fAutoLogonIfChallenged": SimTypeInt(signed=True, label="Int32")}, name="WINHTTP_AUTOPROXY_OPTIONS", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hResolver", "pcwszUrl", "pAutoProxyOptions", "pContext"]),
        #
        'WinHttpGetProxyForUrlEx2': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"dwFlags": SimTypeInt(signed=False, label="UInt32"), "dwAutoDetectFlags": SimTypeInt(signed=False, label="UInt32"), "lpszAutoConfigUrl": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpvReserved": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "dwReserved": SimTypeInt(signed=False, label="UInt32"), "fAutoLogonIfChallenged": SimTypeInt(signed=True, label="Int32")}, name="WINHTTP_AUTOPROXY_OPTIONS", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hResolver", "pcwszUrl", "pAutoProxyOptions", "cbInterfaceSelectionContext", "pInterfaceSelectionContext", "pContext"]),
        #
        'WinHttpGetProxyResult': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"cEntries": SimTypeInt(signed=False, label="UInt32"), "pEntries": SimTypePointer(SimStruct({"fProxy": SimTypeInt(signed=True, label="Int32"), "fBypass": SimTypeInt(signed=True, label="Int32"), "ProxyScheme": SimTypeInt(signed=False, label="WINHTTP_INTERNET_SCHEME"), "pwszProxy": SimTypePointer(SimTypeChar(label="Char"), offset=0), "ProxyPort": SimTypeShort(signed=False, label="UInt16")}, name="WINHTTP_PROXY_RESULT_ENTRY", pack=False, align=None), offset=0)}, name="WINHTTP_PROXY_RESULT", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hResolver", "pProxyResult"]),
        #
        'WinHttpGetProxyResultEx': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"cEntries": SimTypeInt(signed=False, label="UInt32"), "pEntries": SimTypePointer(SimStruct({"fProxy": SimTypeInt(signed=True, label="Int32"), "fBypass": SimTypeInt(signed=True, label="Int32"), "ProxyScheme": SimTypeInt(signed=False, label="WINHTTP_INTERNET_SCHEME"), "pwszProxy": SimTypePointer(SimTypeChar(label="Char"), offset=0), "ProxyPort": SimTypeShort(signed=False, label="UInt16")}, name="WINHTTP_PROXY_RESULT_ENTRY", pack=False, align=None), offset=0), "hProxyDetectionHandle": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "dwProxyInterfaceAffinity": SimTypeInt(signed=False, label="UInt32")}, name="WINHTTP_PROXY_RESULT_EX", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hResolver", "pProxyResultEx"]),
        #
        'WinHttpFreeProxyResult': SimTypeFunction([SimTypePointer(SimStruct({"cEntries": SimTypeInt(signed=False, label="UInt32"), "pEntries": SimTypePointer(SimStruct({"fProxy": SimTypeInt(signed=True, label="Int32"), "fBypass": SimTypeInt(signed=True, label="Int32"), "ProxyScheme": SimTypeInt(signed=False, label="WINHTTP_INTERNET_SCHEME"), "pwszProxy": SimTypePointer(SimTypeChar(label="Char"), offset=0), "ProxyPort": SimTypeShort(signed=False, label="UInt16")}, name="WINHTTP_PROXY_RESULT_ENTRY", pack=False, align=None), offset=0)}, name="WINHTTP_PROXY_RESULT", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["pProxyResult"]),
        #
        'WinHttpFreeProxyResultEx': SimTypeFunction([SimTypePointer(SimStruct({"cEntries": SimTypeInt(signed=False, label="UInt32"), "pEntries": SimTypePointer(SimStruct({"fProxy": SimTypeInt(signed=True, label="Int32"), "fBypass": SimTypeInt(signed=True, label="Int32"), "ProxyScheme": SimTypeInt(signed=False, label="WINHTTP_INTERNET_SCHEME"), "pwszProxy": SimTypePointer(SimTypeChar(label="Char"), offset=0), "ProxyPort": SimTypeShort(signed=False, label="UInt16")}, name="WINHTTP_PROXY_RESULT_ENTRY", pack=False, align=None), offset=0), "hProxyDetectionHandle": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "dwProxyInterfaceAffinity": SimTypeInt(signed=False, label="UInt32")}, name="WINHTTP_PROXY_RESULT_EX", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["pProxyResultEx"]),
        #
        'WinHttpResetAutoProxy': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["hSession", "dwFlags"]),
        #
        'WinHttpGetIEProxyConfigForCurrentUser': SimTypeFunction([SimTypePointer(SimStruct({"fAutoDetect": SimTypeInt(signed=True, label="Int32"), "lpszAutoConfigUrl": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpszProxy": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpszProxyBypass": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="WINHTTP_CURRENT_USER_IE_PROXY_CONFIG", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pProxyConfig"]),
        #
        'WinHttpWriteProxySettings': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimStruct({"dwStructSize": SimTypeInt(signed=False, label="UInt32"), "dwFlags": SimTypeInt(signed=False, label="UInt32"), "dwCurrentSettingsVersion": SimTypeInt(signed=False, label="UInt32"), "pwszConnectionName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszProxy": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszProxyBypass": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszAutoconfigUrl": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszAutoconfigSecondaryUrl": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwAutoDiscoveryFlags": SimTypeInt(signed=False, label="UInt32"), "pwszLastKnownGoodAutoConfigUrl": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwAutoconfigReloadDelayMins": SimTypeInt(signed=False, label="UInt32"), "ftLastKnownDetectTime": SimStruct({"dwLowDateTime": SimTypeInt(signed=False, label="UInt32"), "dwHighDateTime": SimTypeInt(signed=False, label="UInt32")}, name="FILETIME", pack=False, align=None), "dwDetectedInterfaceIpCount": SimTypeInt(signed=False, label="UInt32"), "pdwDetectedInterfaceIp": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), "cNetworkKeys": SimTypeInt(signed=False, label="UInt32"), "pNetworkKeys": SimTypePointer(SimStruct({"pbBuffer": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 128)}, name="_WinHttpProxyNetworkKey", pack=False, align=None), offset=0)}, name="WINHTTP_PROXY_SETTINGS", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hSession", "fForceUpdate", "pWinHttpProxySettings"]),
        #
        'WinHttpReadProxySettings': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), SimTypePointer(SimStruct({"dwStructSize": SimTypeInt(signed=False, label="UInt32"), "dwFlags": SimTypeInt(signed=False, label="UInt32"), "dwCurrentSettingsVersion": SimTypeInt(signed=False, label="UInt32"), "pwszConnectionName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszProxy": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszProxyBypass": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszAutoconfigUrl": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszAutoconfigSecondaryUrl": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwAutoDiscoveryFlags": SimTypeInt(signed=False, label="UInt32"), "pwszLastKnownGoodAutoConfigUrl": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwAutoconfigReloadDelayMins": SimTypeInt(signed=False, label="UInt32"), "ftLastKnownDetectTime": SimStruct({"dwLowDateTime": SimTypeInt(signed=False, label="UInt32"), "dwHighDateTime": SimTypeInt(signed=False, label="UInt32")}, name="FILETIME", pack=False, align=None), "dwDetectedInterfaceIpCount": SimTypeInt(signed=False, label="UInt32"), "pdwDetectedInterfaceIp": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), "cNetworkKeys": SimTypeInt(signed=False, label="UInt32"), "pNetworkKeys": SimTypePointer(SimStruct({"pbBuffer": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 128)}, name="_WinHttpProxyNetworkKey", pack=False, align=None), offset=0)}, name="WINHTTP_PROXY_SETTINGS", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hSession", "pcwszConnectionName", "fFallBackToDefaultSettings", "fSetAutoDiscoverForDefaultSettings", "pdwSettingsVersion", "pfDefaultSettingsAreReturned", "pWinHttpProxySettings"]),
        #
        'WinHttpFreeProxySettings': SimTypeFunction([SimTypePointer(SimStruct({"dwStructSize": SimTypeInt(signed=False, label="UInt32"), "dwFlags": SimTypeInt(signed=False, label="UInt32"), "dwCurrentSettingsVersion": SimTypeInt(signed=False, label="UInt32"), "pwszConnectionName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszProxy": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszProxyBypass": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszAutoconfigUrl": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pwszAutoconfigSecondaryUrl": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwAutoDiscoveryFlags": SimTypeInt(signed=False, label="UInt32"), "pwszLastKnownGoodAutoConfigUrl": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwAutoconfigReloadDelayMins": SimTypeInt(signed=False, label="UInt32"), "ftLastKnownDetectTime": SimStruct({"dwLowDateTime": SimTypeInt(signed=False, label="UInt32"), "dwHighDateTime": SimTypeInt(signed=False, label="UInt32")}, name="FILETIME", pack=False, align=None), "dwDetectedInterfaceIpCount": SimTypeInt(signed=False, label="UInt32"), "pdwDetectedInterfaceIp": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), "cNetworkKeys": SimTypeInt(signed=False, label="UInt32"), "pNetworkKeys": SimTypePointer(SimStruct({"pbBuffer": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 128)}, name="_WinHttpProxyNetworkKey", pack=False, align=None), offset=0)}, name="WINHTTP_PROXY_SETTINGS", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["pWinHttpProxySettings"]),
        #
        'WinHttpGetProxySettingsVersion': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hSession", "pdwProxySettingsVersion"]),
        #
        'WinHttpSetProxySettingsPerUser': SimTypeFunction([SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["fProxySettingsPerUser"]),
        #
        'WinHttpWebSocketCompleteUpgrade': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0)], SimTypePointer(SimTypeBottom(label="Void"), offset=0), arg_names=["hRequest", "pContext"]),
        #
        'WinHttpWebSocketSend': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="WINHTTP_WEB_SOCKET_BUFFER_TYPE"), SimTypePointer(SimTypeBottom(label="Void"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["hWebSocket", "eBufferType", "pvBuffer", "dwBufferLength"]),
        #
        'WinHttpWebSocketReceive': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="WINHTTP_WEB_SOCKET_BUFFER_TYPE"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hWebSocket", "pvBuffer", "dwBufferLength", "pdwBytesRead", "peBufferType"]),
        #
        'WinHttpWebSocketShutdown': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeShort(signed=False, label="UInt16"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["hWebSocket", "usStatus", "pvReason", "dwReasonLength"]),
        #
        'WinHttpWebSocketClose': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeShort(signed=False, label="UInt16"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["hWebSocket", "usStatus", "pvReason", "dwReasonLength"]),
        #
        'WinHttpWebSocketQueryCloseStatus': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hWebSocket", "pusStatus", "pvReason", "dwReasonLength", "pdwReasonLengthConsumed"]),
    }

lib.set_prototypes(prototypes)
