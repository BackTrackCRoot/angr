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
lib.set_library_names("bcrypt.dll")
prototypes = \
    {
        #
        'BCryptOpenAlgorithmProvider': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="BCRYPT_OPEN_ALGORITHM_PROVIDER_FLAGS")], SimTypeInt(signed=True, label="Int32"), arg_names=["phAlgorithm", "pszAlgId", "pszImplementation", "dwFlags"]),
        #
        'BCryptEnumAlgorithms': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_OPERATION"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"pszName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwClass": SimTypeInt(signed=False, label="UInt32"), "dwFlags": SimTypeInt(signed=False, label="UInt32")}, name="BCRYPT_ALGORITHM_IDENTIFIER", pack=False, align=None), offset=0), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["dwAlgOperations", "pAlgCount", "ppAlgList", "dwFlags"]),
        #
        'BCryptEnumProviders': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"pszProviderName": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="BCRYPT_PROVIDER_NAME", pack=False, align=None), offset=0), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["pszAlgId", "pImplCount", "ppImplList", "dwFlags"]),
        #
        'BCryptGetProperty': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hObject", "pszProperty", "pbOutput", "cbOutput", "pcbResult", "dwFlags"]),
        #
        'BCryptSetProperty': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hObject", "pszProperty", "pbInput", "cbInput", "dwFlags"]),
        #
        'BCryptCloseAlgorithmProvider': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hAlgorithm", "dwFlags"]),
        #
        'BCryptFreeBuffer': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeBottom(label="Void"), arg_names=["pvBuffer"]),
        #
        'BCryptGenerateSymmetricKey': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hAlgorithm", "phKey", "pbKeyObject", "cbKeyObject", "pbSecret", "cbSecret", "dwFlags"]),
        #
        'BCryptGenerateKeyPair': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hAlgorithm", "phKey", "dwLength", "dwFlags"]),
        #
        'BCryptEncrypt': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="NCRYPT_FLAGS")], SimTypeInt(signed=True, label="Int32"), arg_names=["hKey", "pbInput", "cbInput", "pPaddingInfo", "pbIV", "cbIV", "pbOutput", "cbOutput", "pcbResult", "dwFlags"]),
        #
        'BCryptDecrypt': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="NCRYPT_FLAGS")], SimTypeInt(signed=True, label="Int32"), arg_names=["hKey", "pbInput", "cbInput", "pPaddingInfo", "pbIV", "cbIV", "pbOutput", "cbOutput", "pcbResult", "dwFlags"]),
        #
        'BCryptExportKey': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hKey", "hExportKey", "pszBlobType", "pbOutput", "cbOutput", "pcbResult", "dwFlags"]),
        #
        'BCryptImportKey': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hAlgorithm", "hImportKey", "pszBlobType", "phKey", "pbKeyObject", "cbKeyObject", "pbInput", "cbInput", "dwFlags"]),
        #
        'BCryptImportKeyPair': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hAlgorithm", "hImportKey", "pszBlobType", "phKey", "pbInput", "cbInput", "dwFlags"]),
        #
        'BCryptDuplicateKey': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hKey", "phNewKey", "pbKeyObject", "cbKeyObject", "dwFlags"]),
        #
        'BCryptFinalizeKeyPair': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hKey", "dwFlags"]),
        #
        'BCryptDestroyKey': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hKey"]),
        #
        'BCryptDestroySecret': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hSecret"]),
        #
        'BCryptSignHash': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="NCRYPT_FLAGS")], SimTypeInt(signed=True, label="Int32"), arg_names=["hKey", "pPaddingInfo", "pbInput", "cbInput", "pbOutput", "cbOutput", "pcbResult", "dwFlags"]),
        #
        'BCryptVerifySignature': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="NCRYPT_FLAGS")], SimTypeInt(signed=True, label="Int32"), arg_names=["hKey", "pPaddingInfo", "pbHash", "cbHash", "pbSignature", "cbSignature", "dwFlags"]),
        #
        'BCryptSecretAgreement': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hPrivKey", "hPubKey", "phAgreedSecret", "dwFlags"]),
        #
        'BCryptDeriveKey': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"ulVersion": SimTypeInt(signed=False, label="UInt32"), "cBuffers": SimTypeInt(signed=False, label="UInt32"), "pBuffers": SimTypePointer(SimStruct({"cbBuffer": SimTypeInt(signed=False, label="UInt32"), "BufferType": SimTypeInt(signed=False, label="UInt32"), "pvBuffer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="BCryptBuffer", pack=False, align=None), offset=0)}, name="BCryptBufferDesc", pack=False, align=None), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hSharedSecret", "pwszKDF", "pParameterList", "pbDerivedKey", "cbDerivedKey", "pcbResult", "dwFlags"]),
        #
        'BCryptKeyDerivation': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"ulVersion": SimTypeInt(signed=False, label="UInt32"), "cBuffers": SimTypeInt(signed=False, label="UInt32"), "pBuffers": SimTypePointer(SimStruct({"cbBuffer": SimTypeInt(signed=False, label="UInt32"), "BufferType": SimTypeInt(signed=False, label="UInt32"), "pvBuffer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="BCryptBuffer", pack=False, align=None), offset=0)}, name="BCryptBufferDesc", pack=False, align=None), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hKey", "pParameterList", "pbDerivedKey", "cbDerivedKey", "pcbResult", "dwFlags"]),
        #
        'BCryptCreateHash': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hAlgorithm", "phHash", "pbHashObject", "cbHashObject", "pbSecret", "cbSecret", "dwFlags"]),
        #
        'BCryptHashData': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hHash", "pbInput", "cbInput", "dwFlags"]),
        #
        'BCryptFinishHash': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hHash", "pbOutput", "cbOutput", "dwFlags"]),
        #
        'BCryptCreateMultiHash': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hAlgorithm", "phHash", "nHashes", "pbHashObject", "cbHashObject", "pbSecret", "cbSecret", "dwFlags"]),
        #
        'BCryptProcessMultiOperations': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="BCRYPT_MULTI_OPERATION_TYPE"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hObject", "operationType", "pOperations", "cbOperations", "dwFlags"]),
        #
        'BCryptDuplicateHash': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hHash", "phNewHash", "pbHashObject", "cbHashObject", "dwFlags"]),
        #
        'BCryptDestroyHash': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hHash"]),
        #
        'BCryptHash': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hAlgorithm", "pbSecret", "cbSecret", "pbInput", "cbInput", "pbOutput", "cbOutput"]),
        #
        'BCryptGenRandom': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hAlgorithm", "pbBuffer", "cbBuffer", "dwFlags"]),
        #
        'BCryptDeriveKeyCapi': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hHash", "hTargetAlg", "pbDerivedKey", "cbDerivedKey", "dwFlags"]),
        #
        'BCryptDeriveKeyPBKDF2': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeLongLong(signed=False, label="UInt64"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hPrf", "pbPassword", "cbPassword", "pbSalt", "cbSalt", "cIterations", "pbDerivedKey", "cbDerivedKey", "dwFlags"]),
        #
        'BCryptQueryProviderRegistration': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="BCRYPT_QUERY_PROVIDER_MODE"), SimTypeInt(signed=False, label="BCRYPT_INTERFACE"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"cAliases": SimTypeInt(signed=False, label="UInt32"), "rgpszAliases": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "pUM": SimTypePointer(SimStruct({"pszImage": SimTypePointer(SimTypeChar(label="Char"), offset=0), "cInterfaces": SimTypeInt(signed=False, label="UInt32"), "rgpInterfaces": SimTypePointer(SimTypePointer(SimStruct({"dwInterface": SimTypeInt(signed=False, label="BCRYPT_INTERFACE"), "dwFlags": SimTypeInt(signed=False, label="BCRYPT_TABLE"), "cFunctions": SimTypeInt(signed=False, label="UInt32"), "rgpszFunctions": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0)}, name="CRYPT_INTERFACE_REG", pack=False, align=None), offset=0), offset=0)}, name="CRYPT_IMAGE_REG", pack=False, align=None), offset=0), "pKM": SimTypePointer(SimStruct({"pszImage": SimTypePointer(SimTypeChar(label="Char"), offset=0), "cInterfaces": SimTypeInt(signed=False, label="UInt32"), "rgpInterfaces": SimTypePointer(SimTypePointer(SimStruct({"dwInterface": SimTypeInt(signed=False, label="BCRYPT_INTERFACE"), "dwFlags": SimTypeInt(signed=False, label="BCRYPT_TABLE"), "cFunctions": SimTypeInt(signed=False, label="UInt32"), "rgpszFunctions": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0)}, name="CRYPT_INTERFACE_REG", pack=False, align=None), offset=0), offset=0)}, name="CRYPT_IMAGE_REG", pack=False, align=None), offset=0)}, name="CRYPT_PROVIDER_REG", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pszProvider", "dwMode", "dwInterface", "pcbBuffer", "ppBuffer"]),
        #
        'BCryptEnumRegisteredProviders': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"cProviders": SimTypeInt(signed=False, label="UInt32"), "rgpszProviders": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0)}, name="CRYPT_PROVIDERS", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pcbBuffer", "ppBuffer"]),
        #
        'BCryptCreateContext': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_TABLE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"dwFlags": SimTypeInt(signed=False, label="CRYPT_CONTEXT_CONFIG_FLAGS"), "dwReserved": SimTypeInt(signed=False, label="UInt32")}, name="CRYPT_CONTEXT_CONFIG", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwTable", "pszContext", "pConfig"]),
        #
        'BCryptDeleteContext': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_TABLE"), SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwTable", "pszContext"]),
        #
        'BCryptEnumContexts': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_TABLE"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"cContexts": SimTypeInt(signed=False, label="UInt32"), "rgpszContexts": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0)}, name="CRYPT_CONTEXTS", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwTable", "pcbBuffer", "ppBuffer"]),
        #
        'BCryptConfigureContext': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_TABLE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"dwFlags": SimTypeInt(signed=False, label="CRYPT_CONTEXT_CONFIG_FLAGS"), "dwReserved": SimTypeInt(signed=False, label="UInt32")}, name="CRYPT_CONTEXT_CONFIG", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwTable", "pszContext", "pConfig"]),
        #
        'BCryptQueryContextConfiguration': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_TABLE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwFlags": SimTypeInt(signed=False, label="CRYPT_CONTEXT_CONFIG_FLAGS"), "dwReserved": SimTypeInt(signed=False, label="UInt32")}, name="CRYPT_CONTEXT_CONFIG", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwTable", "pszContext", "pcbBuffer", "ppBuffer"]),
        #
        'BCryptAddContextFunction': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_TABLE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="BCRYPT_INTERFACE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["dwTable", "pszContext", "dwInterface", "pszFunction", "dwPosition"]),
        #
        'BCryptRemoveContextFunction': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_TABLE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="BCRYPT_INTERFACE"), SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwTable", "pszContext", "dwInterface", "pszFunction"]),
        #
        'BCryptEnumContextFunctions': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_TABLE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="BCRYPT_INTERFACE"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"cFunctions": SimTypeInt(signed=False, label="UInt32"), "rgpszFunctions": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0)}, name="CRYPT_CONTEXT_FUNCTIONS", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwTable", "pszContext", "dwInterface", "pcbBuffer", "ppBuffer"]),
        #
        'BCryptConfigureContextFunction': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_TABLE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="BCRYPT_INTERFACE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"dwFlags": SimTypeInt(signed=False, label="UInt32"), "dwReserved": SimTypeInt(signed=False, label="UInt32")}, name="CRYPT_CONTEXT_FUNCTION_CONFIG", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwTable", "pszContext", "dwInterface", "pszFunction", "pConfig"]),
        #
        'BCryptQueryContextFunctionConfiguration': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_TABLE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="BCRYPT_INTERFACE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"dwFlags": SimTypeInt(signed=False, label="UInt32"), "dwReserved": SimTypeInt(signed=False, label="UInt32")}, name="CRYPT_CONTEXT_FUNCTION_CONFIG", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwTable", "pszContext", "dwInterface", "pszFunction", "pcbBuffer", "ppBuffer"]),
        #
        'BCryptEnumContextFunctionProviders': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_TABLE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="BCRYPT_INTERFACE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"cProviders": SimTypeInt(signed=False, label="UInt32"), "rgpszProviders": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0)}, name="CRYPT_CONTEXT_FUNCTION_PROVIDERS", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwTable", "pszContext", "dwInterface", "pszFunction", "pcbBuffer", "ppBuffer"]),
        #
        'BCryptSetContextFunctionProperty': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_TABLE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="BCRYPT_INTERFACE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwTable", "pszContext", "dwInterface", "pszFunction", "pszProperty", "cbValue", "pbValue"]),
        #
        'BCryptQueryContextFunctionProperty': SimTypeFunction([SimTypeInt(signed=False, label="BCRYPT_TABLE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="BCRYPT_INTERFACE"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwTable", "pszContext", "dwInterface", "pszFunction", "pszProperty", "pcbValue", "ppbValue"]),
        #
        'BCryptRegisterConfigChangeNotify': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["phEvent"]),
        #
        'BCryptUnregisterConfigChangeNotify': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hEvent"]),
        #
        'BCryptResolveProviders': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="BCRYPT_QUERY_PROVIDER_MODE"), SimTypeInt(signed=False, label="BCRYPT_RESOLVE_PROVIDERS_FLAGS"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"cProviders": SimTypeInt(signed=False, label="UInt32"), "rgpProviders": SimTypePointer(SimTypePointer(SimStruct({"dwInterface": SimTypeInt(signed=False, label="UInt32"), "pszFunction": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszProvider": SimTypePointer(SimTypeChar(label="Char"), offset=0), "cProperties": SimTypeInt(signed=False, label="UInt32"), "rgpProperties": SimTypePointer(SimTypePointer(SimStruct({"pszProperty": SimTypePointer(SimTypeChar(label="Char"), offset=0), "cbValue": SimTypeInt(signed=False, label="UInt32"), "pbValue": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="CRYPT_PROPERTY_REF", pack=False, align=None), offset=0), offset=0), "pUM": SimTypePointer(SimStruct({"pszImage": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwFlags": SimTypeInt(signed=False, label="CRYPT_IMAGE_REF_FLAGS")}, name="CRYPT_IMAGE_REF", pack=False, align=None), offset=0), "pKM": SimTypePointer(SimStruct({"pszImage": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwFlags": SimTypeInt(signed=False, label="CRYPT_IMAGE_REF_FLAGS")}, name="CRYPT_IMAGE_REF", pack=False, align=None), offset=0)}, name="CRYPT_PROVIDER_REF", pack=False, align=None), offset=0), offset=0)}, name="CRYPT_PROVIDER_REFS", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pszContext", "dwInterface", "pszFunction", "pszProvider", "dwMode", "dwFlags", "pcbBuffer", "ppBuffer"]),
        #
        'BCryptGetFipsAlgorithmMode': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pfEnabled"]),
    }

lib.set_prototypes(prototypes)
