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
lib.set_library_names("d2d1.dll")
prototypes = \
    {
        #
        'D2D1CreateFactory': SimTypeFunction([SimTypeInt(signed=False, label="D2D1_FACTORY_TYPE"), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimStruct({"debugLevel": SimTypeInt(signed=False, label="D2D1_DEBUG_LEVEL")}, name="D2D1_FACTORY_OPTIONS", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["factoryType", "riid", "pFactoryOptions", "ppIFactory"]),
        #
        'D2D1MakeRotateMatrix': SimTypeFunction([SimTypeFloat(size=32), SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), SimTypePointer(SimStruct({"Anonymous": SimUnion({"Anonymous1": SimStruct({"m11": SimTypeFloat(size=32), "m12": SimTypeFloat(size=32), "m21": SimTypeFloat(size=32), "m22": SimTypeFloat(size=32), "dx": SimTypeFloat(size=32), "dy": SimTypeFloat(size=32)}, name="_Anonymous1_e__Struct", pack=False, align=None), "Anonymous2": SimStruct({"_11": SimTypeFloat(size=32), "_12": SimTypeFloat(size=32), "_21": SimTypeFloat(size=32), "_22": SimTypeFloat(size=32), "_31": SimTypeFloat(size=32), "_32": SimTypeFloat(size=32)}, name="_Anonymous2_e__Struct", pack=False, align=None), "m": SimTypeFixedSizeArray(SimTypeFloat(size=32), 6)}, name="<anon>", label="None")}, name="D2D_MATRIX_3X2_F", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["angle", "center", "matrix"]),
        #
        'D2D1MakeSkewMatrix': SimTypeFunction([SimTypeFloat(size=32), SimTypeFloat(size=32), SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), SimTypePointer(SimStruct({"Anonymous": SimUnion({"Anonymous1": SimStruct({"m11": SimTypeFloat(size=32), "m12": SimTypeFloat(size=32), "m21": SimTypeFloat(size=32), "m22": SimTypeFloat(size=32), "dx": SimTypeFloat(size=32), "dy": SimTypeFloat(size=32)}, name="_Anonymous1_e__Struct", pack=False, align=None), "Anonymous2": SimStruct({"_11": SimTypeFloat(size=32), "_12": SimTypeFloat(size=32), "_21": SimTypeFloat(size=32), "_22": SimTypeFloat(size=32), "_31": SimTypeFloat(size=32), "_32": SimTypeFloat(size=32)}, name="_Anonymous2_e__Struct", pack=False, align=None), "m": SimTypeFixedSizeArray(SimTypeFloat(size=32), 6)}, name="<anon>", label="None")}, name="D2D_MATRIX_3X2_F", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["angleX", "angleY", "center", "matrix"]),
        #
        'D2D1IsMatrixInvertible': SimTypeFunction([SimTypePointer(SimStruct({"Anonymous": SimUnion({"Anonymous1": SimStruct({"m11": SimTypeFloat(size=32), "m12": SimTypeFloat(size=32), "m21": SimTypeFloat(size=32), "m22": SimTypeFloat(size=32), "dx": SimTypeFloat(size=32), "dy": SimTypeFloat(size=32)}, name="_Anonymous1_e__Struct", pack=False, align=None), "Anonymous2": SimStruct({"_11": SimTypeFloat(size=32), "_12": SimTypeFloat(size=32), "_21": SimTypeFloat(size=32), "_22": SimTypeFloat(size=32), "_31": SimTypeFloat(size=32), "_32": SimTypeFloat(size=32)}, name="_Anonymous2_e__Struct", pack=False, align=None), "m": SimTypeFixedSizeArray(SimTypeFloat(size=32), 6)}, name="<anon>", label="None")}, name="D2D_MATRIX_3X2_F", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["matrix"]),
        #
        'D2D1InvertMatrix': SimTypeFunction([SimTypePointer(SimStruct({"Anonymous": SimUnion({"Anonymous1": SimStruct({"m11": SimTypeFloat(size=32), "m12": SimTypeFloat(size=32), "m21": SimTypeFloat(size=32), "m22": SimTypeFloat(size=32), "dx": SimTypeFloat(size=32), "dy": SimTypeFloat(size=32)}, name="_Anonymous1_e__Struct", pack=False, align=None), "Anonymous2": SimStruct({"_11": SimTypeFloat(size=32), "_12": SimTypeFloat(size=32), "_21": SimTypeFloat(size=32), "_22": SimTypeFloat(size=32), "_31": SimTypeFloat(size=32), "_32": SimTypeFloat(size=32)}, name="_Anonymous2_e__Struct", pack=False, align=None), "m": SimTypeFixedSizeArray(SimTypeFloat(size=32), 6)}, name="<anon>", label="None")}, name="D2D_MATRIX_3X2_F", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["matrix"]),
        #
        'D2D1CreateDevice': SimTypeFunction([SimTypeBottom(label="IDXGIDevice"), SimTypePointer(SimStruct({"threadingMode": SimTypeInt(signed=False, label="D2D1_THREADING_MODE"), "debugLevel": SimTypeInt(signed=False, label="D2D1_DEBUG_LEVEL"), "options": SimTypeInt(signed=False, label="D2D1_DEVICE_CONTEXT_OPTIONS")}, name="D2D1_CREATION_PROPERTIES", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="ID2D1Device"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dxgiDevice", "creationProperties", "d2dDevice"]),
        #
        'D2D1CreateDeviceContext': SimTypeFunction([SimTypeBottom(label="IDXGISurface"), SimTypePointer(SimStruct({"threadingMode": SimTypeInt(signed=False, label="D2D1_THREADING_MODE"), "debugLevel": SimTypeInt(signed=False, label="D2D1_DEBUG_LEVEL"), "options": SimTypeInt(signed=False, label="D2D1_DEVICE_CONTEXT_OPTIONS")}, name="D2D1_CREATION_PROPERTIES", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="ID2D1DeviceContext"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dxgiSurface", "creationProperties", "d2dDeviceContext"]),
        #
        'D2D1ConvertColorSpace': SimTypeFunction([SimTypeInt(signed=False, label="D2D1_COLOR_SPACE"), SimTypeInt(signed=False, label="D2D1_COLOR_SPACE"), SimTypePointer(SimStruct({"r": SimTypeFloat(size=32), "g": SimTypeFloat(size=32), "b": SimTypeFloat(size=32), "a": SimTypeFloat(size=32)}, name="D2D1_COLOR_F", pack=False, align=None), offset=0)], SimStruct({"r": SimTypeFloat(size=32), "g": SimTypeFloat(size=32), "b": SimTypeFloat(size=32), "a": SimTypeFloat(size=32)}, name="D2D1_COLOR_F", pack=False, align=None), arg_names=["sourceColorSpace", "destinationColorSpace", "color"]),
        #
        'D2D1SinCos': SimTypeFunction([SimTypeFloat(size=32), SimTypePointer(SimTypeFloat(size=32), offset=0), SimTypePointer(SimTypeFloat(size=32), offset=0)], SimTypeBottom(label="Void"), arg_names=["angle", "s", "c"]),
        #
        'D2D1Tan': SimTypeFunction([SimTypeFloat(size=32)], SimTypeFloat(size=32), arg_names=["angle"]),
        #
        'D2D1Vec3Length': SimTypeFunction([SimTypeFloat(size=32), SimTypeFloat(size=32), SimTypeFloat(size=32)], SimTypeFloat(size=32), arg_names=["x", "y", "z"]),
        #
        'D2D1ComputeMaximumScaleFactor': SimTypeFunction([SimTypePointer(SimStruct({"Anonymous": SimUnion({"Anonymous1": SimStruct({"m11": SimTypeFloat(size=32), "m12": SimTypeFloat(size=32), "m21": SimTypeFloat(size=32), "m22": SimTypeFloat(size=32), "dx": SimTypeFloat(size=32), "dy": SimTypeFloat(size=32)}, name="_Anonymous1_e__Struct", pack=False, align=None), "Anonymous2": SimStruct({"_11": SimTypeFloat(size=32), "_12": SimTypeFloat(size=32), "_21": SimTypeFloat(size=32), "_22": SimTypeFloat(size=32), "_31": SimTypeFloat(size=32), "_32": SimTypeFloat(size=32)}, name="_Anonymous2_e__Struct", pack=False, align=None), "m": SimTypeFixedSizeArray(SimTypeFloat(size=32), 6)}, name="<anon>", label="None")}, name="D2D_MATRIX_3X2_F", pack=False, align=None), offset=0)], SimTypeFloat(size=32), arg_names=["matrix"]),
        #
        'D2D1GetGradientMeshInteriorPointsFromCoonsPatch': SimTypeFunction([SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"x": SimTypeFloat(size=32), "y": SimTypeFloat(size=32)}, name="D2D_POINT_2F", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["pPoint0", "pPoint1", "pPoint2", "pPoint3", "pPoint4", "pPoint5", "pPoint6", "pPoint7", "pPoint8", "pPoint9", "pPoint10", "pPoint11", "pTensorPoint11", "pTensorPoint12", "pTensorPoint21", "pTensorPoint22"]),
    }

lib.set_prototypes(prototypes)
