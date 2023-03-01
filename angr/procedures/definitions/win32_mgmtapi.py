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
lib.set_library_names("mgmtapi.dll")
prototypes = \
    {
        #
        'SnmpMgrOpen': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32")], SimTypePointer(SimTypeBottom(label="Void"), offset=0), arg_names=["lpAgentAddress", "lpAgentCommunity", "nTimeOut", "nRetries"]),
        #
        'SnmpMgrCtl': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["session", "dwCtlCode", "lpvInBuffer", "cbInBuffer", "lpvOUTBuffer", "cbOUTBuffer", "lpcbBytesReturned"]),
        #
        'SnmpMgrClose': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["session"]),
        #
        'SnmpMgrRequest': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeChar(label="Byte"), SimTypePointer(SimStruct({"list": SimTypePointer(SimStruct({"name": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "value": SimStruct({"asnType": SimTypeChar(label="Byte"), "asnValue": SimUnion({"number": SimTypeInt(signed=True, label="Int32"), "unsigned32": SimTypeInt(signed=False, label="UInt32"), "counter64": SimTypeBottom(label="ULARGE_INTEGER"), "string": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "bits": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "object": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "sequence": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "address": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "counter": SimTypeInt(signed=False, label="UInt32"), "gauge": SimTypeInt(signed=False, label="UInt32"), "ticks": SimTypeInt(signed=False, label="UInt32"), "arbitrary": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None)}, name="<anon>", label="None")}, name="AsnAny", pack=False, align=None)}, name="SnmpVarBind", pack=False, align=None), offset=0), "len": SimTypeInt(signed=False, label="UInt32")}, name="SnmpVarBindList", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="SNMP_ERROR_STATUS"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["session", "requestType", "variableBindings", "errorStatus", "errorIndex"]),
        #
        'SnmpMgrStrToOid': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["string", "oid"]),
        #
        'SnmpMgrOidToStr': SimTypeFunction([SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["oid", "string"]),
        #
        'SnmpMgrTrapListen': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["phTrapAvailable"]),
        #
        'SnmpMgrGetTrap': SimTypeFunction([SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="SNMP_GENERICTRAP"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimStruct({"list": SimTypePointer(SimStruct({"name": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "value": SimStruct({"asnType": SimTypeChar(label="Byte"), "asnValue": SimUnion({"number": SimTypeInt(signed=True, label="Int32"), "unsigned32": SimTypeInt(signed=False, label="UInt32"), "counter64": SimTypeBottom(label="ULARGE_INTEGER"), "string": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "bits": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "object": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "sequence": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "address": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "counter": SimTypeInt(signed=False, label="UInt32"), "gauge": SimTypeInt(signed=False, label="UInt32"), "ticks": SimTypeInt(signed=False, label="UInt32"), "arbitrary": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None)}, name="<anon>", label="None")}, name="AsnAny", pack=False, align=None)}, name="SnmpVarBind", pack=False, align=None), offset=0), "len": SimTypeInt(signed=False, label="UInt32")}, name="SnmpVarBindList", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["enterprise", "IPAddress", "genericTrap", "specificTrap", "timeStamp", "variableBindings"]),
        #
        'SnmpMgrGetTrapEx': SimTypeFunction([SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="SNMP_GENERICTRAP"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), SimTypePointer(SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimStruct({"list": SimTypePointer(SimStruct({"name": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "value": SimStruct({"asnType": SimTypeChar(label="Byte"), "asnValue": SimUnion({"number": SimTypeInt(signed=True, label="Int32"), "unsigned32": SimTypeInt(signed=False, label="UInt32"), "counter64": SimTypeBottom(label="ULARGE_INTEGER"), "string": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "bits": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "object": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "sequence": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "address": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "counter": SimTypeInt(signed=False, label="UInt32"), "gauge": SimTypeInt(signed=False, label="UInt32"), "ticks": SimTypeInt(signed=False, label="UInt32"), "arbitrary": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None)}, name="<anon>", label="None")}, name="AsnAny", pack=False, align=None)}, name="SnmpVarBind", pack=False, align=None), offset=0), "len": SimTypeInt(signed=False, label="UInt32")}, name="SnmpVarBindList", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["enterprise", "agentAddress", "sourceAddress", "genericTrap", "specificTrap", "community", "timeStamp", "variableBindings"]),
    }

lib.set_prototypes(prototypes)
