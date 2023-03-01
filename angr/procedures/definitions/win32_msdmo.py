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
lib.set_library_names("msdmo.dll")
prototypes = \
    {
        #
        'DMORegister': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"type": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid")}, name="DMO_PARTIAL_MEDIATYPE", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"type": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid")}, name="DMO_PARTIAL_MEDIATYPE", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["szName", "clsidDMO", "guidCategory", "dwFlags", "cInTypes", "pInTypes", "cOutTypes", "pOutTypes"]),
        #
        'DMOUnregister': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["clsidDMO", "guidCategory"]),
        #
        'DMOEnum': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"type": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid")}, name="DMO_PARTIAL_MEDIATYPE", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"type": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid")}, name="DMO_PARTIAL_MEDIATYPE", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="IEnumDMO"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["guidCategory", "dwFlags", "cInTypes", "pInTypes", "cOutTypes", "pOutTypes", "ppEnum"]),
        #
        'DMOGetTypes': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimStruct({"type": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid")}, name="DMO_PARTIAL_MEDIATYPE", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimStruct({"type": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid")}, name="DMO_PARTIAL_MEDIATYPE", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["clsidDMO", "ulInputTypesRequested", "pulInputTypesSupplied", "pInputTypes", "ulOutputTypesRequested", "pulOutputTypesSupplied", "pOutputTypes"]),
        #
        'DMOGetName': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["clsidDMO", "szName"]),
        #
        'MoInitMediaType': SimTypeFunction([SimTypePointer(SimStruct({"majortype": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid"), "bFixedSizeSamples": SimTypeInt(signed=True, label="Int32"), "bTemporalCompression": SimTypeInt(signed=True, label="Int32"), "lSampleSize": SimTypeInt(signed=False, label="UInt32"), "formattype": SimTypeBottom(label="Guid"), "pUnk": SimTypeBottom(label="IUnknown"), "cbFormat": SimTypeInt(signed=False, label="UInt32"), "pbFormat": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="AM_MEDIA_TYPE", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["pmt", "cbFormat"]),
        #
        'MoFreeMediaType': SimTypeFunction([SimTypePointer(SimStruct({"majortype": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid"), "bFixedSizeSamples": SimTypeInt(signed=True, label="Int32"), "bTemporalCompression": SimTypeInt(signed=True, label="Int32"), "lSampleSize": SimTypeInt(signed=False, label="UInt32"), "formattype": SimTypeBottom(label="Guid"), "pUnk": SimTypeBottom(label="IUnknown"), "cbFormat": SimTypeInt(signed=False, label="UInt32"), "pbFormat": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="AM_MEDIA_TYPE", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pmt"]),
        #
        'MoCopyMediaType': SimTypeFunction([SimTypePointer(SimStruct({"majortype": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid"), "bFixedSizeSamples": SimTypeInt(signed=True, label="Int32"), "bTemporalCompression": SimTypeInt(signed=True, label="Int32"), "lSampleSize": SimTypeInt(signed=False, label="UInt32"), "formattype": SimTypeBottom(label="Guid"), "pUnk": SimTypeBottom(label="IUnknown"), "cbFormat": SimTypeInt(signed=False, label="UInt32"), "pbFormat": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="AM_MEDIA_TYPE", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"majortype": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid"), "bFixedSizeSamples": SimTypeInt(signed=True, label="Int32"), "bTemporalCompression": SimTypeInt(signed=True, label="Int32"), "lSampleSize": SimTypeInt(signed=False, label="UInt32"), "formattype": SimTypeBottom(label="Guid"), "pUnk": SimTypeBottom(label="IUnknown"), "cbFormat": SimTypeInt(signed=False, label="UInt32"), "pbFormat": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="AM_MEDIA_TYPE", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pmtDest", "pmtSrc"]),
        #
        'MoCreateMediaType': SimTypeFunction([SimTypePointer(SimTypePointer(SimStruct({"majortype": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid"), "bFixedSizeSamples": SimTypeInt(signed=True, label="Int32"), "bTemporalCompression": SimTypeInt(signed=True, label="Int32"), "lSampleSize": SimTypeInt(signed=False, label="UInt32"), "formattype": SimTypeBottom(label="Guid"), "pUnk": SimTypeBottom(label="IUnknown"), "cbFormat": SimTypeInt(signed=False, label="UInt32"), "pbFormat": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="AM_MEDIA_TYPE", pack=False, align=None), offset=0), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["ppmt", "cbFormat"]),
        #
        'MoDeleteMediaType': SimTypeFunction([SimTypePointer(SimStruct({"majortype": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid"), "bFixedSizeSamples": SimTypeInt(signed=True, label="Int32"), "bTemporalCompression": SimTypeInt(signed=True, label="Int32"), "lSampleSize": SimTypeInt(signed=False, label="UInt32"), "formattype": SimTypeBottom(label="Guid"), "pUnk": SimTypeBottom(label="IUnknown"), "cbFormat": SimTypeInt(signed=False, label="UInt32"), "pbFormat": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="AM_MEDIA_TYPE", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pmt"]),
        #
        'MoDuplicateMediaType': SimTypeFunction([SimTypePointer(SimTypePointer(SimStruct({"majortype": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid"), "bFixedSizeSamples": SimTypeInt(signed=True, label="Int32"), "bTemporalCompression": SimTypeInt(signed=True, label="Int32"), "lSampleSize": SimTypeInt(signed=False, label="UInt32"), "formattype": SimTypeBottom(label="Guid"), "pUnk": SimTypeBottom(label="IUnknown"), "cbFormat": SimTypeInt(signed=False, label="UInt32"), "pbFormat": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="AM_MEDIA_TYPE", pack=False, align=None), offset=0), offset=0), SimTypePointer(SimStruct({"majortype": SimTypeBottom(label="Guid"), "subtype": SimTypeBottom(label="Guid"), "bFixedSizeSamples": SimTypeInt(signed=True, label="Int32"), "bTemporalCompression": SimTypeInt(signed=True, label="Int32"), "lSampleSize": SimTypeInt(signed=False, label="UInt32"), "formattype": SimTypeBottom(label="Guid"), "pUnk": SimTypeBottom(label="IUnknown"), "cbFormat": SimTypeInt(signed=False, label="UInt32"), "pbFormat": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="AM_MEDIA_TYPE", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["ppmtDest", "pmtSrc"]),
    }

lib.set_prototypes(prototypes)
