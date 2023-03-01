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
lib.set_library_names("ksuser.dll")
prototypes = \
    {
        #
        'KsCreateAllocator': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Anonymous1": SimUnion({"OptionsFlags": SimTypeInt(signed=False, label="UInt32"), "RequirementsFlags": SimTypeInt(signed=False, label="UInt32")}, name="<anon>", label="None"), "PoolType": SimTypeInt(signed=False, label="UInt32"), "Frames": SimTypeInt(signed=False, label="UInt32"), "FrameSize": SimTypeInt(signed=False, label="UInt32"), "Anonymous2": SimUnion({"FileAlignment": SimTypeInt(signed=False, label="UInt32"), "FramePitch": SimTypeInt(signed=True, label="Int32")}, name="<anon>", label="None"), "Reserved": SimTypeInt(signed=False, label="UInt32")}, name="KSALLOCATOR_FRAMING", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["ConnectionHandle", "AllocatorFraming", "AllocatorHandle"]),
        #
        'KsCreateClock': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"CreateFlags": SimTypeInt(signed=False, label="UInt32")}, name="KSCLOCK_CREATE", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["ConnectionHandle", "ClockCreate", "ClockHandle"]),
        #
        'KsCreatePin': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Interface": SimStruct({"Anonymous": SimUnion({"Anonymous": SimStruct({"Set": SimTypeBottom(label="Guid"), "Id": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Alignment": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None")}, name="KSIDENTIFIER", pack=False, align=None), "Medium": SimStruct({"Anonymous": SimUnion({"Anonymous": SimStruct({"Set": SimTypeBottom(label="Guid"), "Id": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Alignment": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None")}, name="KSIDENTIFIER", pack=False, align=None), "PinId": SimTypeInt(signed=False, label="UInt32"), "PinToHandle": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Priority": SimStruct({"PriorityClass": SimTypeInt(signed=False, label="UInt32"), "PrioritySubClass": SimTypeInt(signed=False, label="UInt32")}, name="KSPRIORITY", pack=False, align=None)}, name="KSPIN_CONNECT", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["FilterHandle", "Connect", "DesiredAccess", "ConnectionHandle"]),
        #
        'KsCreateTopologyNode': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"CreateFlags": SimTypeInt(signed=False, label="UInt32"), "Node": SimTypeInt(signed=False, label="UInt32")}, name="KSNODE_CREATE", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["ParentHandle", "NodeCreate", "DesiredAccess", "NodeHandle"]),
        #
        'KsCreateAllocator2': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Anonymous1": SimUnion({"OptionsFlags": SimTypeInt(signed=False, label="UInt32"), "RequirementsFlags": SimTypeInt(signed=False, label="UInt32")}, name="<anon>", label="None"), "PoolType": SimTypeInt(signed=False, label="UInt32"), "Frames": SimTypeInt(signed=False, label="UInt32"), "FrameSize": SimTypeInt(signed=False, label="UInt32"), "Anonymous2": SimUnion({"FileAlignment": SimTypeInt(signed=False, label="UInt32"), "FramePitch": SimTypeInt(signed=True, label="Int32")}, name="<anon>", label="None"), "Reserved": SimTypeInt(signed=False, label="UInt32")}, name="KSALLOCATOR_FRAMING", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["ConnectionHandle", "AllocatorFraming", "AllocatorHandle"]),
        #
        'KsCreateClock2': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"CreateFlags": SimTypeInt(signed=False, label="UInt32")}, name="KSCLOCK_CREATE", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["ConnectionHandle", "ClockCreate", "ClockHandle"]),
        #
        'KsCreatePin2': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Interface": SimStruct({"Anonymous": SimUnion({"Anonymous": SimStruct({"Set": SimTypeBottom(label="Guid"), "Id": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Alignment": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None")}, name="KSIDENTIFIER", pack=False, align=None), "Medium": SimStruct({"Anonymous": SimUnion({"Anonymous": SimStruct({"Set": SimTypeBottom(label="Guid"), "Id": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Alignment": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None")}, name="KSIDENTIFIER", pack=False, align=None), "PinId": SimTypeInt(signed=False, label="UInt32"), "PinToHandle": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Priority": SimStruct({"PriorityClass": SimTypeInt(signed=False, label="UInt32"), "PrioritySubClass": SimTypeInt(signed=False, label="UInt32")}, name="KSPRIORITY", pack=False, align=None)}, name="KSPIN_CONNECT", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["FilterHandle", "Connect", "DesiredAccess", "ConnectionHandle"]),
        #
        'KsCreateTopologyNode2': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"CreateFlags": SimTypeInt(signed=False, label="UInt32"), "Node": SimTypeInt(signed=False, label="UInt32")}, name="KSNODE_CREATE", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["ParentHandle", "NodeCreate", "DesiredAccess", "NodeHandle"]),
    }

lib.set_prototypes(prototypes)
