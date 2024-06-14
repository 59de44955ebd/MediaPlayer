# -*- coding: mbcs -*-
typelib_path = 'DirectShow.tlb'
#_lcid = 0 # change this if required

from ctypes import *
from ctypes.wintypes import (_FILETIME, _LARGE_INTEGER, _ULARGE_INTEGER, tagRECT, tagSIZE,
        BYTE, BOOL, WORD, DWORD, INT, UINT, FLOAT, COLORREF, LONG, ULONG, HWND, HDC, LPCOLESTR, LCID, LPVOID, RECT)
from dshow.comtypes import (BSTR, COMMETHOD, CoClass, GUID, IPersist, IUnknown, _COAUTHIDENTITY, _COAUTHINFO,
        _COSERVERINFO, dispid, helpstring, tagBIND_OPTS2, wireHWND)
from dshow.comtypes.automation import VARIANT, IDispatch
from dshow.comtypes.persist import IPropertyBag, IErrorLog
from dshow.comtypes.typeinfo import ULONG_PTR

WSTRING = c_wchar_p
LONG_PTR = c_int

# values for enumeration '_AM_INTF_SEARCH_FLAGS'
AM_INTF_SEARCH_INPUT_PIN = 1
AM_INTF_SEARCH_OUTPUT_PIN = 2
AM_INTF_SEARCH_FILTER = 4
_AM_INTF_SEARCH_FLAGS = c_int # enum

# values for enumeration '_AM_FILTER_FLAGS'
AM_FILTER_FLAGS_REMOVABLE = 1
_AM_FILTER_FLAGS = c_int # enum
class IFilterChain(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{DCFBDCF6-0DC2-45F5-9AB2-7C330EA09C29}')
    _idlflags_ = []
class IMediaFilter(IPersist):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86899-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IBaseFilter(IMediaFilter):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86895-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IFilterChain._methods_ = [
    COMMETHOD([], HRESULT, 'StartChain',
              ( ['in'], POINTER(IBaseFilter), 'pStartFilter' ),
              ( ['in'], POINTER(IBaseFilter), 'pEndFilter' )),
    COMMETHOD([], HRESULT, 'PauseChain',
              ( ['in'], POINTER(IBaseFilter), 'pStartFilter' ),
              ( ['in'], POINTER(IBaseFilter), 'pEndFilter' )),
    COMMETHOD([], HRESULT, 'StopChain',
              ( ['in'], POINTER(IBaseFilter), 'pStartFilter' ),
              ( ['in'], POINTER(IBaseFilter), 'pEndFilter' )),
    COMMETHOD([], HRESULT, 'RemoveChain',
              ( ['in'], POINTER(IBaseFilter), 'pStartFilter' ),
              ( ['in'], POINTER(IBaseFilter), 'pEndFilter' )),
]

class IDVEnc(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D18E17A0-AACB-11D0-AFB0-00AA00B67A42}')
    _idlflags_ = []
class __MIDL___MIDL_itf_DirectShow_0345_0001(Structure):
    pass
DVINFO = __MIDL___MIDL_itf_DirectShow_0345_0001
IDVEnc._methods_ = [
    COMMETHOD([], HRESULT, 'get_IFormatResolution',
              ( ['out'], POINTER(c_int), 'VideoFormat' ),
              ( ['out'], POINTER(c_int), 'DVFormat' ),
              ( ['out'], POINTER(c_int), 'Resolution' ),
              ( ['in'], c_ubyte, 'fDVInfo' ),
              ( ['out'], POINTER(DVINFO), 'sDVInfo' )),
    COMMETHOD([], HRESULT, 'put_IFormatResolution',
              ( ['in'], c_int, 'VideoFormat' ),
              ( ['in'], c_int, 'DVFormat' ),
              ( ['in'], c_int, 'Resolution' ),
              ( ['in'], c_ubyte, 'fDVInfo' ),
              ( ['in'], POINTER(DVINFO), 'sDVInfo' )),
]

class IRegisterServiceProvider(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7B3A2F01-0751-48DD-B556-004785171C54}')
    _idlflags_ = []
IRegisterServiceProvider._methods_ = [
    COMMETHOD([], HRESULT, 'RegisterService',
              ( ['in'], POINTER(GUID), 'guidService' ),
              ( ['in'], POINTER(IUnknown), 'punkObject' )),
]

# values for enumeration 'AMOVERLAYFX'
AMOVERFX_NOFX = 0
AMOVERFX_MIRRORLEFTRIGHT = 2
AMOVERFX_MIRRORUPDOWN = 4
AMOVERFX_DEINTERLACE = 8
AMOVERLAYFX = c_int # enum
class IBindCtx(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000E-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IRunningObjectTable(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000010-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IEnumString(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000101-0000-0000-C000-000000000046}')
    _idlflags_ = []
IBindCtx._methods_ = [
    COMMETHOD([], HRESULT, 'RegisterObjectBound',
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'RevokeObjectBound',
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'ReleaseBoundObjects'),
    COMMETHOD([], HRESULT, 'RemoteSetBindOptions',
              ( ['in'], POINTER(tagBIND_OPTS2), 'pbindopts' )),
    COMMETHOD([], HRESULT, 'RemoteGetBindOptions',
              ( ['in', 'out'], POINTER(tagBIND_OPTS2), 'pbindopts' )),
    COMMETHOD([], HRESULT, 'GetRunningObjectTable',
              ( ['out'], POINTER(POINTER(IRunningObjectTable)), 'pprot' )),
    COMMETHOD([], HRESULT, 'RegisterObjectParam',
              ( ['in'], WSTRING, 'pszKey' ),
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'GetObjectParam',
              ( ['in'], WSTRING, 'pszKey' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppunk' )),
    COMMETHOD([], HRESULT, 'EnumObjectParam',
              ( ['out'], POINTER(POINTER(IEnumString)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'RevokeObjectParam',
              ( ['in'], WSTRING, 'pszKey' )),
]

class IVMRAspectRatioControl(IUnknown):
    _case_insensitive_ = True
    'IVMRAspectRatioControl Interface'
    _iid_ = GUID('{EDE80B5C-BAD6-4623-B537-65586C9F8DFD}')
    _idlflags_ = []
IVMRAspectRatioControl._methods_ = [
    COMMETHOD([], HRESULT, 'GetAspectRatioMode',
              ( ['out'], POINTER(c_ulong), 'lpdwARMode' )),
    COMMETHOD([], HRESULT, 'SetAspectRatioMode',
              ( ['in'], c_ulong, 'dwARMode' )),
]

class IAMStreamConfig(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13340-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
class _AMMediaType(Structure):
    pass
IAMStreamConfig._methods_ = [
    COMMETHOD([], HRESULT, 'SetFormat',
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'GetFormat',
              ( ['out'], POINTER(POINTER(_AMMediaType)), 'ppmt' )),
    COMMETHOD([], HRESULT, 'GetNumberOfCapabilities',
              ( ['out'], POINTER(c_int), 'piCount' ),
              ( ['out'], POINTER(c_int), 'piSize' )),
    COMMETHOD([], HRESULT, 'GetStreamCaps',
              ( ['in'], c_int, 'iIndex' ),
              ( ['out'], POINTER(POINTER(_AMMediaType)), 'ppmt' ),
              ( ['out'], POINTER(c_ubyte), 'pSCC' )),
]

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0163_0001'
CompressionCaps_CanQuality = 1
CompressionCaps_CanCrunch = 2
CompressionCaps_CanKeyFrame = 4
CompressionCaps_CanBFrame = 8
CompressionCaps_CanWindow = 16
__MIDL___MIDL_itf_DirectShow_0163_0001 = c_int # enum
class tagVMRALLOCATIONINFO(Structure):
    pass
tagVMRALLOCATIONINFO._fields_ = [
    ('dwFlags', c_ulong),
    ('lpHdr', POINTER(c_ulong)),
    ('lpPixFmt', POINTER(c_ulong)),
    ('szAspectRatio', tagSIZE),
    ('dwMinBuffers', c_ulong),
    ('dwMaxBuffers', c_ulong),
    ('dwInterlaceFlags', c_ulong),
    ('szNativeSize', tagSIZE),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for tagVMRALLOCATIONINFO is skipped.
class tagAM_SAMPLE2_PROPERTIES(Structure):
    pass
tagAM_SAMPLE2_PROPERTIES._fields_ = [
    ('cbData', c_ulong),
    ('dwTypeSpecificFlags', c_ulong),
    ('dwSampleFlags', c_ulong),
    ('lActual', c_int),
    ('tStart', c_longlong),
    ('tStop', c_longlong),
    ('dwStreamId', c_ulong),
    ('pMediaType', POINTER(_AMMediaType)),
    ('pbBuffer', POINTER(c_ubyte)),
    ('cbBuffer', c_int),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for tagAM_SAMPLE2_PROPERTIES is skipped.
class __MIDL___MIDL_itf_DirectShow_0134_0003(Structure):
    pass
REGPINMEDIUM = __MIDL___MIDL_itf_DirectShow_0134_0003
class tagPALETTEENTRY(Structure):
    pass
tagPALETTEENTRY._fields_ = [
    ('peRed', c_ubyte),
    ('peGreen', c_ubyte),
    ('peBlue', c_ubyte),
    ('peFlags', c_ubyte),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for tagPALETTEENTRY is skipped.

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0181_0001'
AMPROPERTY_PIN_CATEGORY = 0
AMPROPERTY_PIN_MEDIUM = 1
__MIDL___MIDL_itf_DirectShow_0181_0001 = c_int # enum
AMPROPERTY_PIN = __MIDL___MIDL_itf_DirectShow_0181_0001
class IMediaSample(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A8689A-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IMediaSample2(IMediaSample):
    _case_insensitive_ = True
    _iid_ = GUID('{36B73884-C2C8-11CF-8B46-00805F6CEF60}')
    _idlflags_ = []
IMediaSample._methods_ = [
    COMMETHOD([], HRESULT, 'GetPointer',
              ( ['out'], POINTER(POINTER(c_ubyte)), 'ppBuffer' )),
    COMMETHOD([], c_int, 'GetSize'),
    COMMETHOD([], HRESULT, 'GetTime',
              ( ['out'], POINTER(c_longlong), 'pTimeStart' ),
              ( ['out'], POINTER(c_longlong), 'pTimeEnd' )),
    COMMETHOD([], HRESULT, 'SetTime',
              ( ['in'], POINTER(c_longlong), 'pTimeStart' ),
              ( ['in'], POINTER(c_longlong), 'pTimeEnd' )),
    COMMETHOD([], HRESULT, 'IsSyncPoint'),
    COMMETHOD([], HRESULT, 'SetSyncPoint',
              ( [], c_int, 'bIsSyncPoint' )),
    COMMETHOD([], HRESULT, 'IsPreroll'),
    COMMETHOD([], HRESULT, 'SetPreroll',
              ( [], c_int, 'bIsPreroll' )),
    COMMETHOD([], c_int, 'GetActualDataLength'),
    COMMETHOD([], HRESULT, 'SetActualDataLength',
              ( [], c_int, '__MIDL_0010' )),
    COMMETHOD([], HRESULT, 'GetMediaType',
              ( [], POINTER(POINTER(_AMMediaType)), 'ppMediaType' )),
    COMMETHOD([], HRESULT, 'SetMediaType',
              ( [], POINTER(_AMMediaType), 'pMediaType' )),
    COMMETHOD([], HRESULT, 'IsDiscontinuity'),
    COMMETHOD([], HRESULT, 'SetDiscontinuity',
              ( [], c_int, 'bDiscontinuity' )),
    COMMETHOD([], HRESULT, 'GetMediaTime',
              ( ['out'], POINTER(c_longlong), 'pTimeStart' ),
              ( ['out'], POINTER(c_longlong), 'pTimeEnd' )),
    COMMETHOD([], HRESULT, 'SetMediaTime',
              ( ['in'], POINTER(c_longlong), 'pTimeStart' ),
              ( ['in'], POINTER(c_longlong), 'pTimeEnd' )),
]

IMediaSample2._methods_ = [
    COMMETHOD([], HRESULT, 'GetProperties',
              ( ['in'], c_ulong, 'cbProperties' ),
              ( ['out'], POINTER(c_ubyte), 'pbProperties' )),
    COMMETHOD([], HRESULT, 'SetProperties',
              ( ['in'], c_ulong, 'cbProperties' ),
              ( ['in'], POINTER(c_ubyte), 'pbProperties' )),
]

class IConfigAviMux(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{5ACD6AA0-F482-11CE-8B67-00AA00A3F1A6}')
    _idlflags_ = []
IConfigAviMux._methods_ = [
    COMMETHOD([], HRESULT, 'SetMasterStream',
              ( ['in'], c_int, 'IStream' )),
    COMMETHOD([], HRESULT, 'GetMasterStream',
              ( ['out'], POINTER(c_int), 'pStream' )),
    COMMETHOD([], HRESULT, 'SetOutputCompatibilityIndex',
              ( ['in'], c_int, 'fOldIndex' )),
    COMMETHOD([], HRESULT, 'GetOutputCompatibilityIndex',
              ( ['out'], POINTER(c_int), 'pfOldIndex' )),
]

class IAMOverlayFX(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{62FAE250-7E65-4460-BFC9-6398B322073C}')
    _idlflags_ = []
IAMOverlayFX._methods_ = [
    COMMETHOD([], HRESULT, 'QueryOverlayFXCaps',
              ( ['out'], POINTER(c_ulong), 'lpdwOverlayFXCaps' )),
    COMMETHOD([], HRESULT, 'SetOverlayFX',
              ( ['in'], c_ulong, 'dwOverlayFX' )),
    COMMETHOD([], HRESULT, 'GetOverlayFX',
              ( ['out'], POINTER(c_ulong), 'lpdwOverlayFX' )),
]

class __MIDL___MIDL_itf_DirectShow_0370_0001(Structure):
    pass
__MIDL___MIDL_itf_DirectShow_0370_0001._fields_ = [
    ('dw1', c_ulong),
    ('dw2', c_ulong),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_DirectShow_0370_0001 is skipped.
class IReferenceClock(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86897-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IReferenceClock._methods_ = [
    COMMETHOD([], HRESULT, 'GetTime',
              ( ['out'], POINTER(c_longlong), 'pTime' )),
    COMMETHOD([], HRESULT, 'AdviseTime',
              ( ['in'], c_longlong, 'baseTime' ),
              ( ['in'], c_longlong, 'streamTime' ),
              ( ['in'], ULONG_PTR, 'hEvent' ),
              ( ['out'], POINTER(ULONG_PTR), 'pdwAdviseCookie' )),
    COMMETHOD([], HRESULT, 'AdvisePeriodic',
              ( ['in'], c_longlong, 'startTime' ),
              ( ['in'], c_longlong, 'periodTime' ),
              ( ['in'], ULONG_PTR, 'hSemaphore' ),
              ( ['out'], POINTER(ULONG_PTR), 'pdwAdviseCookie' )),
    COMMETHOD([], HRESULT, 'Unadvise',
              ( ['in'], ULONG_PTR, 'dwAdviseCookie' )),
]

class __MIDL___MIDL_itf_DirectShow_0134_0008(Structure):
    pass
class __MIDL___MIDL_itf_DirectShow_0134_0002(Structure):
    pass
REGFILTERPINS = __MIDL___MIDL_itf_DirectShow_0134_0002
__MIDL___MIDL_itf_DirectShow_0134_0008._fields_ = [
    ('cPins', c_ulong),
    ('rgPins', POINTER(REGFILTERPINS)),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_DirectShow_0134_0008 is skipped.
class IKsPropertySet(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{31EFAC30-515C-11D0-A9AA-00AA0061BE93}')
    _idlflags_ = []
IKsPropertySet._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteSet',
              ( ['in'], POINTER(GUID), 'guidPropSet' ),
              ( ['in'], c_ulong, 'dwPropID' ),
              ( ['in'], POINTER(c_ubyte), 'pInstanceData' ),
              ( ['in'], c_ulong, 'cbInstanceData' ),
              ( ['in'], POINTER(c_ubyte), 'pPropData' ),
              ( ['in'], c_ulong, 'cbPropData' )),
    COMMETHOD([], HRESULT, 'RemoteGet',
              ( ['in'], POINTER(GUID), 'guidPropSet' ),
              ( ['in'], c_ulong, 'dwPropID' ),
              ( ['in'], POINTER(c_ubyte), 'pInstanceData' ),
              ( ['in'], c_ulong, 'cbInstanceData' ),
              ( ['out'], POINTER(c_ubyte), 'pPropData' ),
              ( ['in'], c_ulong, 'cbPropData' ),
              ( ['out'], POINTER(c_ulong), 'pcbReturned' )),
    COMMETHOD([], HRESULT, 'QuerySupported',
              ( ['in'], POINTER(GUID), 'guidPropSet' ),
              ( ['in'], c_ulong, 'dwPropID' ),
              ( ['out'], POINTER(c_ulong), 'pTypeSupport' )),
]

class IPinConnection(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4A9A62D3-27D4-403D-91E9-89F540E55534}')
    _idlflags_ = []
IPinConnection._methods_ = [
    COMMETHOD([], HRESULT, 'DynamicQueryAccept',
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'NotifyEndOfStream',
              ( ['in'], c_void_p, 'hNotifyEvent' )),
    COMMETHOD([], HRESULT, 'IsEndPin'),
    COMMETHOD([], HRESULT, 'DynamicDisconnect'),
]

class IVPManager(IUnknown):
    _case_insensitive_ = True
    'IVPManager Interface'
    _iid_ = GUID('{AAC18C18-E186-46D2-825D-A1F8DC8E395A}')
    _idlflags_ = []
IVPManager._methods_ = [
    COMMETHOD([], HRESULT, 'SetVideoPortIndex',
              ( ['in'], c_ulong, 'dwVideoPortIndex' )),
    COMMETHOD([], HRESULT, 'GetVideoPortIndex',
              ( ['out'], POINTER(c_ulong), 'pdwVideoPortIndex' )),
]

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0164_0001'
VfwCaptureDialog_Source = 1
VfwCaptureDialog_Format = 2
VfwCaptureDialog_Display = 4
__MIDL___MIDL_itf_DirectShow_0164_0001 = c_int # enum
VfwCaptureDialogs = __MIDL___MIDL_itf_DirectShow_0164_0001
class IMediaPropertyBag(IPropertyBag):
    _case_insensitive_ = True
    _iid_ = GUID('{6025A880-C0D5-11D0-BD4E-00A0C911CE86}')
    _idlflags_ = []
IMediaPropertyBag._methods_ = [
    COMMETHOD([], HRESULT, 'EnumProperty',
              ( ['in'], c_ulong, 'iProperty' ),
              ( ['in', 'out'], POINTER(VARIANT), 'pvarPropertyName' ),
              ( ['in', 'out'], POINTER(VARIANT), 'pvarPropertyValue' )),
]

class CodecAPIEventData(Structure):
    pass
CodecAPIEventData._fields_ = [
    ('guid', GUID),
    ('dataLength', c_ulong),
    ('reserved', c_ulong * 3),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for CodecAPIEventData is skipped.

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0169_0001'
VideoCopyProtectionMacrovisionBasic = 0
VideoCopyProtectionMacrovisionCBI = 1
__MIDL___MIDL_itf_DirectShow_0169_0001 = c_int # enum
class __MIDL___MIDL_itf_DirectShow_0134_0001(Structure):
    pass
REGPINTYPES = __MIDL___MIDL_itf_DirectShow_0134_0001

# values for enumeration 'tagAMTunerModeType'
AMTUNER_MODE_DEFAULT = 0
AMTUNER_MODE_TV = 1
AMTUNER_MODE_FM_RADIO = 2
AMTUNER_MODE_AM_RADIO = 4
AMTUNER_MODE_DSS = 8
tagAMTunerModeType = c_int # enum
class __MIDL___MIDL_itf_DirectShow_0134_0005(Structure):
    pass
REGFILTERPINS2 = __MIDL___MIDL_itf_DirectShow_0134_0005
class tagTIMECODE_SAMPLE(Structure):
    pass
class tagTIMECODE(Structure):
    pass
tagTIMECODE._fields_ = [
    ('wFrameRate', c_ushort),
    ('wFrameFract', c_ushort),
    ('dwFrames', c_ulong),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for tagTIMECODE is skipped.
tagTIMECODE_SAMPLE._fields_ = [
    ('qwTick', c_longlong),
    ('timecode', tagTIMECODE),
    ('dwUser', c_ulong),
    ('dwFlags', c_ulong),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for tagTIMECODE_SAMPLE is skipped.
class IVMRVideoStreamControl(IUnknown):
    _case_insensitive_ = True
    'IVMRMixerStreamConfig Interface'
    _iid_ = GUID('{058D1F11-2A54-4BEF-BD54-DF706626B727}')
    _idlflags_ = []
DDCOLORKEY = __MIDL___MIDL_itf_DirectShow_0370_0001
IVMRVideoStreamControl._methods_ = [
    COMMETHOD([], HRESULT, 'SetColorKey',
              ( ['in'], POINTER(DDCOLORKEY), 'lpClrKey' )),
    COMMETHOD([], HRESULT, 'GetColorKey',
              ( ['out'], POINTER(DDCOLORKEY), 'lpClrKey' )),
    COMMETHOD([], HRESULT, 'SetStreamActiveState',
              ( ['in'], c_int, 'fActive' )),
    COMMETHOD([], HRESULT, 'GetStreamActiveState',
              ( ['out'], POINTER(c_int), 'lpfActive' )),
]

class CaptureGraphBuilder2(CoClass):
    _reg_clsid_ = GUID('{BF87B6E1-8C27-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
class ICaptureGraphBuilder2(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{93E5A4E0-2D50-11D2-ABFA-00A0C9C6E38D}')
    _idlflags_ = []
CaptureGraphBuilder2._com_interfaces_ = [ICaptureGraphBuilder2]

CompressionCaps = __MIDL___MIDL_itf_DirectShow_0163_0001
__MIDL___MIDL_itf_DirectShow_0134_0002._fields_ = [
    ('strName', WSTRING),
    ('bRendered', c_int),
    ('bOutput', c_int),
    ('bZero', c_int),
    ('bMany', c_int),
    ('clsConnectsToFilter', POINTER(GUID)),
    ('strConnectsToPin', POINTER(c_ushort)),
    ('nMediaTypes', c_uint),
    ('lpMediaType', POINTER(REGPINTYPES)),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_DirectShow_0134_0002 is skipped.
class IEncoderAPI(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{70423839-6ACC-4B23-B079-21DBF08156A5}')
    _idlflags_ = []
IEncoderAPI._methods_ = [
    COMMETHOD([], HRESULT, 'IsSupported',
              ( ['in'], POINTER(GUID), 'Api' )),
    COMMETHOD([], HRESULT, 'IsAvailable',
              ( ['in'], POINTER(GUID), 'Api' )),
    COMMETHOD([], HRESULT, 'GetParameterRange',
              ( ['in'], POINTER(GUID), 'Api' ),
              ( ['out'], POINTER(VARIANT), 'ValueMin' ),
              ( ['out'], POINTER(VARIANT), 'ValueMax' ),
              ( ['out'], POINTER(VARIANT), 'SteppingDelta' )),
    COMMETHOD([], HRESULT, 'GetParameterValues',
              ( ['in'], POINTER(GUID), 'Api' ),
              ( ['out'], POINTER(POINTER(VARIANT)), 'Values' ),
              ( ['out'], POINTER(c_ulong), 'ValuesCount' )),
    COMMETHOD([], HRESULT, 'GetDefaultValue',
              ( ['in'], POINTER(GUID), 'Api' ),
              ( ['out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([], HRESULT, 'GetValue',
              ( ['in'], POINTER(GUID), 'Api' ),
              ( ['out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([], HRESULT, 'SetValue',
              ( ['in'], POINTER(GUID), 'Api' ),
              ( ['in'], POINTER(VARIANT), 'Value' )),
]

class IAsyncReader(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868AA-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IMemAllocator(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A8689C-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class _AllocatorProperties(Structure):
    pass
IAsyncReader._methods_ = [
    COMMETHOD([], HRESULT, 'RequestAllocator',
              ( ['in'], POINTER(IMemAllocator), 'pPreferred' ),
              ( ['in'], POINTER(_AllocatorProperties), 'pProps' ),
              ( ['out'], POINTER(POINTER(IMemAllocator)), 'ppActual' )),
    COMMETHOD([], HRESULT, 'Request',
              ( ['in'], POINTER(IMediaSample), 'pSample' ),
              ( ['in'], ULONG_PTR, 'dwUser' )),
    COMMETHOD([], HRESULT, 'WaitForNext',
              ( ['in'], c_ulong, 'dwTimeout' ),
              ( ['out'], POINTER(POINTER(IMediaSample)), 'ppSample' ),
              ( ['out'], POINTER(ULONG_PTR), 'pdwUser' )),
    COMMETHOD([], HRESULT, 'SyncReadAligned',
              ( ['in'], POINTER(IMediaSample), 'pSample' )),
    COMMETHOD([], HRESULT, 'SyncRead',
              ( ['in'], c_longlong, 'llPosition' ),
              ( ['in'], c_int, 'lLength' ),
              ( ['out'], POINTER(c_ubyte), 'pBuffer' )),
    COMMETHOD([], HRESULT, 'Length',
              ( ['out'], POINTER(c_longlong), 'pTotal' ),
              ( ['out'], POINTER(c_longlong), 'pAvailable' )),
    COMMETHOD([], HRESULT, 'BeginFlush'),
    COMMETHOD([], HRESULT, 'EndFlush'),
]

class _RGNDATA(Structure):
    pass
class _RGNDATAHEADER(Structure):
    pass
_RGNDATAHEADER._fields_ = [
    ('dwSize', c_ulong),
    ('iType', c_ulong),
    ('nCount', c_ulong),
    ('nRgnSize', c_ulong),
    ('rcBound', tagRECT),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for _RGNDATAHEADER is skipped.
_RGNDATA._fields_ = [
    ('rdh', _RGNDATAHEADER),
    ('Buffer', c_char * 1),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for _RGNDATA is skipped.
class IAMTimecodeReader(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{9B496CE1-811B-11CF-8C77-00AA006B6814}')
    _idlflags_ = []
IAMTimecodeReader._methods_ = [
    COMMETHOD([], HRESULT, 'GetTCRMode',
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetTCRMode',
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([], HRESULT, 'put_VITCLine',
              ( ['in'], c_int, 'Line' )),
    COMMETHOD([], HRESULT, 'get_VITCLine',
              ( ['out'], POINTER(c_int), 'pLine' )),
    COMMETHOD([], HRESULT, 'GetTimecode',
              ( ['out'], POINTER(tagTIMECODE_SAMPLE), 'pTimecodeSample' )),
]

# values for enumeration 'tagAM_SAMPLE_PROPERTY_FLAGS'
AM_SAMPLE_SPLICEPOINT = 1
AM_SAMPLE_PREROLL = 2
AM_SAMPLE_DATADISCONTINUITY = 4
AM_SAMPLE_TYPECHANGED = 8
AM_SAMPLE_TIMEVALID = 16
AM_SAMPLE_TIMEDISCONTINUITY = 64
AM_SAMPLE_FLUSH_ON_PAUSE = 128
AM_SAMPLE_STOPVALID = 256
AM_SAMPLE_ENDOFSTREAM = 512
AM_STREAM_MEDIA = 0
AM_STREAM_CONTROL = 1
tagAM_SAMPLE_PROPERTY_FLAGS = c_int # enum
class IAMVideoCompression(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13343-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMVideoCompression._methods_ = [
    COMMETHOD([], HRESULT, 'put_KeyFrameRate',
              ( ['in'], c_int, 'KeyFrameRate' )),
    COMMETHOD([], HRESULT, 'get_KeyFrameRate',
              ( ['out'], POINTER(c_int), 'pKeyFrameRate' )),
    COMMETHOD([], HRESULT, 'put_PFramesPerKeyFrame',
              ( ['in'], c_int, 'PFramesPerKeyFrame' )),
    COMMETHOD([], HRESULT, 'get_PFramesPerKeyFrame',
              ( ['out'], POINTER(c_int), 'pPFramesPerKeyFrame' )),
    COMMETHOD([], HRESULT, 'put_Quality',
              ( ['in'], c_double, 'Quality' )),
    COMMETHOD([], HRESULT, 'get_Quality',
              ( ['out'], POINTER(c_double), 'pQuality' )),
    COMMETHOD([], HRESULT, 'put_WindowSize',
              ( ['in'], c_ulonglong, 'WindowSize' )),
    COMMETHOD([], HRESULT, 'get_WindowSize',
              ( ['out'], POINTER(c_ulonglong), 'pWindowSize' )),
    COMMETHOD([], HRESULT, 'GetInfo',
              ( ['out'], POINTER(c_ushort), 'pszVersion' ),
              ( ['in', 'out'], POINTER(c_int), 'pcbVersion' ),
              ( ['out'], WSTRING, 'pszDescription' ),
              ( ['in', 'out'], POINTER(c_int), 'pcbDescription' ),
              ( ['out'], POINTER(c_int), 'pDefaultKeyFrameRate' ),
              ( ['out'], POINTER(c_int), 'pDefaultPFramesPerKey' ),
              ( ['out'], POINTER(c_double), 'pDefaultQuality' ),
              ( ['out'], POINTER(c_int), 'pCapabilities' )),
    COMMETHOD([], HRESULT, 'OverrideKeyFrame',
              ( ['in'], c_int, 'FrameNumber' )),
    COMMETHOD([], HRESULT, 'OverrideFrameSize',
              ( ['in'], c_int, 'FrameNumber' ),
              ( ['in'], c_int, 'Size' )),
]

# values for enumeration '_AMRESCTL_RESERVEFLAGS'
AMRESCTL_RESERVEFLAGS_RESERVE = 0
AMRESCTL_RESERVEFLAGS_UNRESERVE = 1
_AMRESCTL_RESERVEFLAGS = c_int # enum
class _VMRVIDEOSTREAMINFO(Structure):
    pass
class _NORMALIZEDRECT(Structure):
    pass
_NORMALIZEDRECT._fields_ = [
    ('left', c_float),
    ('top', c_float),
    ('right', c_float),
    ('bottom', c_float),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for _NORMALIZEDRECT is skipped.
_VMRVIDEOSTREAMINFO._fields_ = [
    ('pddsVideoSurface', POINTER(c_ulong)),
    ('dwWidth', c_ulong),
    ('dwHeight', c_ulong),
    ('dwStrmID', c_ulong),
    ('fAlpha', c_float),
    ('ddClrKey', DDCOLORKEY),
    ('rNormal', _NORMALIZEDRECT),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for _VMRVIDEOSTREAMINFO is skipped.

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0371_0001'
AMAP_PIXELFORMAT_VALID = 1
AMAP_3D_TARGET = 2
AMAP_ALLOW_SYSMEM = 4
AMAP_FORCE_SYSMEM = 8
AMAP_DIRECTED_FLIP = 16
AMAP_DXVA_TARGET = 32
__MIDL___MIDL_itf_DirectShow_0371_0001 = c_int # enum
class IPersistStream(IPersist):
    _case_insensitive_ = True
    _iid_ = GUID('{00000109-0000-0000-C000-000000000046}')
    _idlflags_ = []
class ISequentialStream(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0C733A30-2A1C-11CE-ADE5-00AA0044773D}')
    _idlflags_ = []
class IStream(ISequentialStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000C-0000-0000-C000-000000000046}')
    _idlflags_ = []
IPersistStream._methods_ = [
    COMMETHOD([], HRESULT, 'IsDirty'),
    COMMETHOD([], HRESULT, 'Load',
              ( ['in'], POINTER(IStream), 'pstm' )),
    COMMETHOD([], HRESULT, 'Save',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], c_int, 'fClearDirty' )),
    COMMETHOD([], HRESULT, 'GetSizeMax',
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbSize' )),
]

# values for enumeration '_FilterState'
State_Stopped = 0
State_Paused = 1
State_Running = 2
_FilterState = c_int # enum
IMediaFilter._methods_ = [
    COMMETHOD([], HRESULT, 'Stop'),
    COMMETHOD([], HRESULT, 'Pause'),
    COMMETHOD([], HRESULT, 'Run',
              ( [], c_longlong, 'tStart' )),
    COMMETHOD([], HRESULT, 'GetState',
              ( ['in'], c_ulong, 'dwMilliSecsTimeout' ),
              ( ['out'], POINTER(_FilterState), 'State' )),
    COMMETHOD([], HRESULT, 'SetSyncSource',
              ( ['in'], POINTER(IReferenceClock), 'pClock' )),
    COMMETHOD([], HRESULT, 'GetSyncSource',
              ( ['out'], POINTER(POINTER(IReferenceClock)), 'pClock' )),
]

IMemAllocator._methods_ = [
    COMMETHOD([], HRESULT, 'SetProperties',
              ( ['in'], POINTER(_AllocatorProperties), 'pRequest' ),
              ( ['out'], POINTER(_AllocatorProperties), 'pActual' )),
    COMMETHOD([], HRESULT, 'GetProperties',
              ( ['out'], POINTER(_AllocatorProperties), 'pProps' )),
    COMMETHOD([], HRESULT, 'Commit'),
    COMMETHOD([], HRESULT, 'Decommit'),
    COMMETHOD([], HRESULT, 'GetBuffer',
              ( ['out'], POINTER(POINTER(IMediaSample)), 'ppBuffer' ),
              ( ['in'], POINTER(c_longlong), 'pStartTime' ),
              ( ['in'], POINTER(c_longlong), 'pEndTime' ),
              ( ['in'], c_ulong, 'dwFlags' )),
    COMMETHOD([], HRESULT, 'ReleaseBuffer',
              ( ['in'], POINTER(IMediaSample), 'pBuffer' )),
]

__MIDL___MIDL_itf_DirectShow_0134_0003._fields_ = [
    ('clsMedium', GUID),
    ('dw1', c_ulong),
    ('dw2', c_ulong),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_DirectShow_0134_0003 is skipped.
class IOverlay(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A1-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class tagCOLORKEY(Structure):
    pass
class IOverlayNotify(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A0-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IOverlay._methods_ = [
    COMMETHOD([], HRESULT, 'GetPalette',
              ( ['out'], POINTER(c_ulong), 'pdwColors' ),
              ( ['out'], POINTER(POINTER(tagPALETTEENTRY)), 'ppPalette' )),
    COMMETHOD([], HRESULT, 'SetPalette',
              ( ['in'], c_ulong, 'dwColors' ),
              ( ['in'], POINTER(tagPALETTEENTRY), 'pPalette' )),
    COMMETHOD([], HRESULT, 'GetDefaultColorKey',
              ( ['out'], POINTER(tagCOLORKEY), 'pColorKey' )),
    COMMETHOD([], HRESULT, 'GetColorKey',
              ( ['out'], POINTER(tagCOLORKEY), 'pColorKey' )),
    COMMETHOD([], HRESULT, 'SetColorKey',
              ( ['in', 'out'], POINTER(tagCOLORKEY), 'pColorKey' )),
    COMMETHOD([], HRESULT, 'GetWindowHandle',
              ( ['out'], POINTER(wireHWND), 'pHwnd' )),
    COMMETHOD([], HRESULT, 'GetClipList',
              ( ['out'], POINTER(tagRECT), 'pSourceRect' ),
              ( ['out'], POINTER(tagRECT), 'pDestinationRect' ),
              ( ['out'], POINTER(POINTER(_RGNDATA)), 'ppRgnData' )),
    COMMETHOD([], HRESULT, 'GetVideoPosition',
              ( ['out'], POINTER(tagRECT), 'pSourceRect' ),
              ( ['out'], POINTER(tagRECT), 'pDestinationRect' )),
    COMMETHOD([], HRESULT, 'Advise',
              ( ['in'], POINTER(IOverlayNotify), 'pOverlayNotify' ),
              ( ['in'], c_ulong, 'dwInterests' )),
    COMMETHOD([], HRESULT, 'Unadvise'),
]

class IVMRFilterConfig(IUnknown):
    _case_insensitive_ = True
    'IVMRFilterConfig Interface'
    _iid_ = GUID('{9E5530C5-7034-48B4-BB46-0B8A6EFC8E36}')
    _idlflags_ = []
class IVMRImageCompositor(IUnknown):
    _case_insensitive_ = True
    'IVMRImageCompositor Interface'
    _iid_ = GUID('{7A4FB5AF-479F-4074-BB40-CE6722E43C82}')
    _idlflags_ = []
IVMRFilterConfig._methods_ = [
    COMMETHOD([], HRESULT, 'SetImageCompositor',
              ( ['in'], POINTER(IVMRImageCompositor), 'lpVMRImgCompositor' )),
    COMMETHOD([], HRESULT, 'SetNumberOfStreams',
              ( ['in'], c_ulong, 'dwMaxStreams' )),
    COMMETHOD([], HRESULT, 'GetNumberOfStreams',
              ( ['out'], POINTER(c_ulong), 'pdwMaxStreams' )),
    COMMETHOD([], HRESULT, 'SetRenderingPrefs',
              ( ['in'], c_ulong, 'dwRenderFlags' )),
    COMMETHOD([], HRESULT, 'GetRenderingPrefs',
              ( ['out'], POINTER(c_ulong), 'pdwRenderFlags' )),
    COMMETHOD([], HRESULT, 'SetRenderingMode',
              ( ['in'], c_ulong, 'mode' )),
    COMMETHOD([], HRESULT, 'GetRenderingMode',
              ( ['out'], POINTER(c_ulong), 'pMode' )),
]

IVMRImageCompositor._methods_ = [
    COMMETHOD([], HRESULT, 'InitCompositionTarget',
              ( ['in'], POINTER(IUnknown), 'pD3DDevice' ),
              ( ['in'], POINTER(c_ulong), 'pddsRenderTarget' )),
    COMMETHOD([], HRESULT, 'TermCompositionTarget',
              ( ['in'], POINTER(IUnknown), 'pD3DDevice' ),
              ( ['in'], POINTER(c_ulong), 'pddsRenderTarget' )),
    COMMETHOD([], HRESULT, 'SetStreamMediaType',
              ( ['in'], c_ulong, 'dwStrmID' ),
              ( ['in'], POINTER(_AMMediaType), 'pmt' ),
              ( ['in'], c_int, 'fTexture' )),
    COMMETHOD([], HRESULT, 'CompositeImage',
              ( ['in'], POINTER(IUnknown), 'pD3DDevice' ),
              ( ['in'], POINTER(c_ulong), 'pddsRenderTarget' ),
              ( ['in'], POINTER(_AMMediaType), 'pmtRenderTarget' ),
              ( ['in'], c_longlong, 'rtStart' ),
              ( ['in'], c_longlong, 'rtEnd' ),
              ( ['in'], c_ulong, 'dwClrBkGnd' ),
              ( ['in'], POINTER(_VMRVIDEOSTREAMINFO), 'pVideoStreamInfo' ),
              ( ['in'], c_uint, 'cStreams' )),
]

class __MIDL___MIDL_itf_DirectShow_0134_0007(Union):
    pass
class __MIDL___MIDL_itf_DirectShow_0134_0009(Structure):
    pass
__MIDL___MIDL_itf_DirectShow_0134_0009._fields_ = [
    ('cPins2', c_ulong),
    ('rgPins2', POINTER(REGFILTERPINS2)),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_DirectShow_0134_0009 is skipped.
__MIDL___MIDL_itf_DirectShow_0134_0007._fields_ = [
    ('__MIDL_0011', __MIDL___MIDL_itf_DirectShow_0134_0008),
    ('__MIDL_0012', __MIDL___MIDL_itf_DirectShow_0134_0009),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_DirectShow_0134_0007 is skipped.
class IVMRMixerBitmap(IUnknown):
    _case_insensitive_ = True
    'IVMRMixerBitmap Interface'
    _iid_ = GUID('{1E673275-0257-40AA-AF20-7C608D4A0428}')
    _idlflags_ = []
class _VMRALPHABITMAP(Structure):
    pass
IVMRMixerBitmap._methods_ = [
    COMMETHOD([], HRESULT, 'SetAlphaBitmap',
              ( ['in'], POINTER(_VMRALPHABITMAP), 'pBmpParms' )),
    COMMETHOD([], HRESULT, 'UpdateAlphaBitmapParameters',
              ( ['in'], POINTER(_VMRALPHABITMAP), 'pBmpParms' )),
    COMMETHOD([], HRESULT, 'GetAlphaBitmapParameters',
              ( ['out'], POINTER(_VMRALPHABITMAP), 'pBmpParms' )),
]

class IMoniker(IPersistStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000F-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IEnumMoniker(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000102-0000-0000-C000-000000000046}')
    _idlflags_ = []
IRunningObjectTable._methods_ = [
    COMMETHOD([], HRESULT, 'Register',
              ( ['in'], c_ulong, 'grfFlags' ),
              ( ['in'], POINTER(IUnknown), 'punkObject' ),
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' ),
              ( ['out'], POINTER(c_ulong), 'pdwRegister' )),
    COMMETHOD([], HRESULT, 'Revoke',
              ( ['in'], c_ulong, 'dwRegister' )),
    COMMETHOD([], HRESULT, 'IsRunning',
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' )),
    COMMETHOD([], HRESULT, 'GetObject',
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppunkObject' )),
    COMMETHOD([], HRESULT, 'NoteChangeTime',
              ( ['in'], c_ulong, 'dwRegister' ),
              ( ['in'], POINTER(_FILETIME), 'pfiletime' )),
    COMMETHOD([], HRESULT, 'GetTimeOfLastChange',
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' ),
              ( ['out'], POINTER(_FILETIME), 'pfiletime' )),
    COMMETHOD([], HRESULT, 'EnumRunning',
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenumMoniker' )),
]

class __MIDL___MIDL_itf_DirectShow_0134_0006(Structure):
    pass
REGFILTER2 = __MIDL___MIDL_itf_DirectShow_0134_0006
class IAMTimecodeGenerator(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{9B496CE0-811B-11CF-8C77-00AA006B6814}')
    _idlflags_ = []
IAMTimecodeGenerator._methods_ = [
    COMMETHOD([], HRESULT, 'GetTCGMode',
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetTCGMode',
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([], HRESULT, 'put_VITCLine',
              ( ['in'], c_int, 'Line' )),
    COMMETHOD([], HRESULT, 'get_VITCLine',
              ( ['out'], POINTER(c_int), 'pLine' )),
    COMMETHOD([], HRESULT, 'SetTimecode',
              ( ['in'], POINTER(tagTIMECODE_SAMPLE), 'pTimecodeSample' )),
    COMMETHOD([], HRESULT, 'GetTimecode',
              ( ['out'], POINTER(tagTIMECODE_SAMPLE), 'pTimecodeSample' )),
]

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0164_0002'
VfwCompressDialog_Config = 1
VfwCompressDialog_About = 2
VfwCompressDialog_QueryConfig = 4
VfwCompressDialog_QueryAbout = 8
__MIDL___MIDL_itf_DirectShow_0164_0002 = c_int # enum
VfwCompressDialogs = __MIDL___MIDL_itf_DirectShow_0164_0002

# values for enumeration 'AM_SEEKING_SeekingFlags'
AM_SEEKING_NoPositioning = 0
AM_SEEKING_AbsolutePositioning = 1
AM_SEEKING_RelativePositioning = 2
AM_SEEKING_IncrementalPositioning = 3
AM_SEEKING_PositioningBitsMask = 3
AM_SEEKING_SeekToKeyFrame = 4
AM_SEEKING_ReturnTime = 8
AM_SEEKING_Segment = 16
AM_SEEKING_NoFlush = 32
AM_SEEKING_SeekingFlags = c_int # enum
class IAMDevMemoryControl(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6545BF1-E76B-11D0-BD52-00A0C911CE86}')
    _idlflags_ = []
IAMDevMemoryControl._methods_ = [
    COMMETHOD([], HRESULT, 'QueryWriteSync'),
    COMMETHOD([], HRESULT, 'WriteSync'),
    COMMETHOD([], HRESULT, 'GetDevId',
              ( ['out'], POINTER(c_ulong), 'pdwDevId' )),
]

class IMemAllocatorCallbackTemp(IMemAllocator):
    _case_insensitive_ = True
    _iid_ = GUID('{379A0CF0-C1DE-11D2-ABF5-00A0C905F375}')
    _idlflags_ = []
class IMemAllocatorNotifyCallbackTemp(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{92980B30-C1DE-11D2-ABF5-00A0C905F375}')
    _idlflags_ = []
IMemAllocatorCallbackTemp._methods_ = [
    COMMETHOD([], HRESULT, 'SetNotify',
              ( ['in'], POINTER(IMemAllocatorNotifyCallbackTemp), 'pNotify' )),
    COMMETHOD([], HRESULT, 'GetFreeCount',
              ( ['out'], POINTER(c_int), 'plBuffersFree' )),
]

# values for enumeration 'tagAnalogVideoStandard'
AnalogVideo_None = 0
AnalogVideo_NTSC_M = 1
AnalogVideo_NTSC_M_J = 2
AnalogVideo_NTSC_433 = 4
AnalogVideo_PAL_B = 16
AnalogVideo_PAL_D = 32
AnalogVideo_PAL_G = 64
AnalogVideo_PAL_H = 128
AnalogVideo_PAL_I = 256
AnalogVideo_PAL_M = 512
AnalogVideo_PAL_N = 1024
AnalogVideo_PAL_60 = 2048
AnalogVideo_SECAM_B = 4096
AnalogVideo_SECAM_D = 8192
AnalogVideo_SECAM_G = 16384
AnalogVideo_SECAM_H = 32768
AnalogVideo_SECAM_K = 65536
AnalogVideo_SECAM_K1 = 131072
AnalogVideo_SECAM_L = 262144
AnalogVideo_SECAM_L1 = 524288
AnalogVideo_PAL_N_COMBO = 1048576
tagAnalogVideoStandard = c_int # enum

# values for enumeration '_DVENCODERFORMAT'
DVENCODERFORMAT_DVSD = 2007
DVENCODERFORMAT_DVHD = 2008
DVENCODERFORMAT_DVSL = 2009
_DVENCODERFORMAT = c_int # enum
class IQualityControl(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A5-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class tagQuality(Structure):
    pass

# values for enumeration 'tagQualityMessageType'
Famine = 0
Flood = 1
tagQualityMessageType = c_int # enum
tagQuality._fields_ = [
    ('type', tagQualityMessageType),
    ('Proportion', c_int),
    ('Late', c_longlong),
    ('TimeStamp', c_longlong),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for tagQuality is skipped.
IQualityControl._methods_ = [
    COMMETHOD([], HRESULT, 'Notify',
              ( ['in'], POINTER(IBaseFilter), 'pSelf' ),
              ( ['in'], tagQuality, 'q' )),
    COMMETHOD([], HRESULT, 'SetSink',
              ( ['in'], POINTER(IQualityControl), 'piqc' )),
]

# values for enumeration 'tagPhysicalConnectorType'
PhysConn_Video_Tuner = 1
PhysConn_Video_Composite = 2
PhysConn_Video_SVideo = 3
PhysConn_Video_RGB = 4
PhysConn_Video_YRYBY = 5
PhysConn_Video_SerialDigital = 6
PhysConn_Video_ParallelDigital = 7
PhysConn_Video_SCSI = 8
PhysConn_Video_AUX = 9
PhysConn_Video_1394 = 10
PhysConn_Video_USB = 11
PhysConn_Video_VideoDecoder = 12
PhysConn_Video_VideoEncoder = 13
PhysConn_Video_SCART = 14
PhysConn_Video_Black = 15
PhysConn_Audio_Tuner = 4096
PhysConn_Audio_Line = 4097
PhysConn_Audio_Mic = 4098
PhysConn_Audio_AESDigital = 4099
PhysConn_Audio_SPDIFDigital = 4100
PhysConn_Audio_SCSI = 4101
PhysConn_Audio_AUX = 4102
PhysConn_Audio_1394 = 4103
PhysConn_Audio_USB = 4104
PhysConn_Audio_AudioDecoder = 4105
tagPhysicalConnectorType = c_int # enum
class _PinInfo(Structure):
    pass

# values for enumeration '_PinDirection'
PINDIR_INPUT = 0
PINDIR_OUTPUT = 1
_PinDirection = c_int # enum
_PinInfo._fields_ = [
    ('pFilter', POINTER(IBaseFilter)),
    ('dir', _PinDirection),
    ('achName', c_ushort * 128),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for _PinInfo is skipped.
class IAMTunerNotification(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{211A8760-03AC-11D1-8D13-00AA00BD8339}')
    _idlflags_ = []

# values for enumeration 'tagAMTunerEventType'
AMTUNER_EVENT_CHANGED = 1
tagAMTunerEventType = c_int # enum
IAMTunerNotification._methods_ = [
    COMMETHOD([], HRESULT, 'OnEvent',
              ( ['in'], tagAMTunerEventType, 'Event' )),
]

class IAMOpenProgress(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{8E1C39A1-DE53-11CF-AA63-0080C744528D}')
    _idlflags_ = []
IAMOpenProgress._methods_ = [
    COMMETHOD([], HRESULT, 'QueryProgress',
              ( ['out'], POINTER(c_longlong), 'pllTotal' ),
              ( ['out'], POINTER(c_longlong), 'pllCurrent' )),
    COMMETHOD([], HRESULT, 'AbortOperation'),
]

class IMPEG2StreamIdMap(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D0E04C47-25B8-4369-925A-362A01D95444}')
    _idlflags_ = []
class IEnumStreamIdMap(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{945C1566-6202-46FC-96C7-D87F289C6534}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

IMPEG2StreamIdMap._methods_ = [
    COMMETHOD([], HRESULT, 'MapStreamId',
              ( ['in'], c_ulong, 'ulStreamId' ),
              ( ['in'], c_ulong, 'MediaSampleContent' ),
              ( ['in'], c_ulong, 'ulSubstreamFilterValue' ),
              ( ['in'], c_int, 'iDataOffset' )),
    COMMETHOD([], HRESULT, 'UnmapStreamId',
              ( ['in'], c_ulong, 'culStreamId' ),
              ( ['in'], POINTER(c_ulong), 'pulStreamId' )),
    COMMETHOD([], HRESULT, 'EnumStreamIdMap',
              ( ['out'], POINTER(POINTER(IEnumStreamIdMap)), 'ppIEnumStreamIdMap' )),
]

# values for enumeration 'tagAMTunerSubChannel'
AMTUNER_SUBCHAN_NO_TUNE = -2
AMTUNER_SUBCHAN_DEFAULT = -1
tagAMTunerSubChannel = c_int # enum
class IVMRDeinterlaceControl(IUnknown):
    _case_insensitive_ = True
    'IVMRDeinterlaceControl Interface'
    _iid_ = GUID('{BB057577-0DB8-4E6A-87A7-1A8C9A505A0F}')
    _idlflags_ = []
class _VMRVideoDesc(Structure):
    pass
class _VMRDeinterlaceCaps(Structure):
    pass
IVMRDeinterlaceControl._methods_ = [
    COMMETHOD([], HRESULT, 'GetNumberOfDeinterlaceModes',
              ( ['in'], POINTER(_VMRVideoDesc), 'lpVideoDescription' ),
              ( ['in', 'out'], POINTER(c_ulong), 'lpdwNumDeinterlaceModes' ),
              ( ['out'], POINTER(GUID), 'lpDeinterlaceModes' )),
    COMMETHOD([], HRESULT, 'GetDeinterlaceModeCaps',
              ( ['in'], POINTER(GUID), 'lpDeinterlaceMode' ),
              ( ['in'], POINTER(_VMRVideoDesc), 'lpVideoDescription' ),
              ( ['in', 'out'], POINTER(_VMRDeinterlaceCaps), 'lpDeinterlaceCaps' )),
    COMMETHOD([], HRESULT, 'GetDeinterlaceMode',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['out'], POINTER(GUID), 'lpDeinterlaceMode' )),
    COMMETHOD([], HRESULT, 'SetDeinterlaceMode',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['in'], POINTER(GUID), 'lpDeinterlaceMode' )),
    COMMETHOD([], HRESULT, 'GetDeinterlacePrefs',
              ( ['out'], POINTER(c_ulong), 'lpdwDeinterlacePrefs' )),
    COMMETHOD([], HRESULT, 'SetDeinterlacePrefs',
              ( ['in'], c_ulong, 'dwDeinterlacePrefs' )),
    COMMETHOD([], HRESULT, 'GetActualDeinterlaceMode',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['out'], POINTER(GUID), 'lpDeinterlaceMode' )),
]

class FilterGraph(CoClass):
    _reg_clsid_ = GUID('{E436EBB3-524F-11CE-9F53-0020AF0BA770}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
class IFilterGraph(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A8689F-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IGraphBuilder(IFilterGraph):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A9-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
FilterGraph._com_interfaces_ = [IGraphBuilder]

class tagVMRMONITORINFO(Structure):
    pass
class tagVMRGUID(Structure):
    pass
tagVMRGUID._fields_ = [
    ('pGUID', POINTER(GUID)),
    ('guid', GUID),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for tagVMRGUID is skipped.
tagVMRMONITORINFO._fields_ = [
    ('guid', tagVMRGUID),
    ('rcMonitor', tagRECT),
    ('hMon', c_void_p),
    ('dwFlags', c_ulong),
    ('szDevice', c_ushort * 32),
    ('szDescription', c_ushort * 256),
    ('liDriverVersion', _LARGE_INTEGER),
    ('dwVendorId', c_ulong),
    ('dwDeviceId', c_ulong),
    ('dwSubSysId', c_ulong),
    ('dwRevision', c_ulong),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for tagVMRMONITORINFO is skipped.
class AviMux(CoClass):
    _reg_clsid_ = GUID('{E2510970-F137-11CE-8B67-00AA00A3F1A6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
AviMux._com_interfaces_ = [IConfigAviMux, IBaseFilter]

class ICreateDevEnum(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{29840822-5B84-11D0-BD3B-00A0C911CE86}')
    _idlflags_ = []
ICreateDevEnum._methods_ = [
    COMMETHOD([], HRESULT, 'CreateClassEnumerator',
              ( ['in'], POINTER(GUID), 'clsidDeviceClass' ),
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenumMoniker' ),
              ( ['in'], c_ulong, 'dwFlags' )),
]

class ICaptureGraphBuilder(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{BF87B6E0-8C27-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []
class IFileSinkFilter(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{A2104830-7C70-11CF-8BCE-00AA00A3F1A6}')
    _idlflags_ = []
class IAMCopyCaptureFileProgress(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{670D1D20-A068-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []
ICaptureGraphBuilder._methods_ = [
    COMMETHOD([], HRESULT, 'SetFiltergraph',
              ( ['in'], POINTER(IGraphBuilder), 'pfg' )),
    COMMETHOD([], HRESULT, 'GetFiltergraph',
              ( ['out'], POINTER(POINTER(IGraphBuilder)), 'ppfg' )),
    COMMETHOD([], HRESULT, 'SetOutputFileName',
              ( ['in'], POINTER(GUID), 'pType' ),
              ( ['in'], WSTRING, 'lpstrFile' ),
              ( ['out'], POINTER(POINTER(IBaseFilter)), 'ppf' ),
              ( ['out'], POINTER(POINTER(IFileSinkFilter)), 'ppSink' )),
    COMMETHOD([], HRESULT, 'RemoteFindInterface',
              ( ['in'], POINTER(GUID), 'pCategory' ),
              ( ['in'], POINTER(IBaseFilter), 'pf' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppint' )),
    COMMETHOD([], HRESULT, 'RenderStream',
              ( ['in'], POINTER(GUID), 'pCategory' ),
              ( ['in'], POINTER(IUnknown), 'pSource' ),
              ( ['in'], POINTER(IBaseFilter), 'pfCompressor' ),
              ( ['in'], POINTER(IBaseFilter), 'pfRenderer' )),
    COMMETHOD([], HRESULT, 'ControlStream',
              ( ['in'], POINTER(GUID), 'pCategory' ),
              ( ['in'], POINTER(IBaseFilter), 'pFilter' ),
              ( ['in'], POINTER(c_longlong), 'pstart' ),
              ( ['in'], POINTER(c_longlong), 'pStop' ),
              ( ['in'], c_ushort, 'wStartCookie' ),
              ( ['in'], c_ushort, 'wStopCookie' )),
    COMMETHOD([], HRESULT, 'AllocCapFile',
              ( ['in'], WSTRING, 'lpstr' ),
              ( ['in'], c_ulonglong, 'dwlSize' )),
    COMMETHOD([], HRESULT, 'CopyCaptureFile',
              ( ['in'], WSTRING, 'lpwstrOld' ),
              ( ['in'], WSTRING, 'lpwstrNew' ),
              ( ['in'], c_int, 'fAllowEscAbort' ),
              ( ['in'], POINTER(IAMCopyCaptureFileProgress), 'pCallback' )),
]

class IPinFlowControl(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C56E9858-DBF3-4F6B-8119-384AF2060DEB}')
    _idlflags_ = []
IPinFlowControl._methods_ = [
    COMMETHOD([], HRESULT, 'Block',
              ( ['in'], c_ulong, 'dwBlockFlags' ),
              ( ['in'], c_void_p, 'hEvent' )),
]

class _RemotableHandle(Structure):
    pass
wireHDC = POINTER(_RemotableHandle)
_VMRALPHABITMAP._fields_ = [
    ('dwFlags', c_ulong),
    ('hdc', wireHDC),
    ('pDDS', POINTER(c_ulong)),
    ('rSrc', tagRECT),
    ('rDest', _NORMALIZEDRECT),
    ('fAlpha', c_float),
    ('clrSrcKey', c_ulong),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for _VMRALPHABITMAP is skipped.
class IGraphVersion(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868AB-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IGraphVersion._methods_ = [
    COMMETHOD([], HRESULT, 'QueryVersion',
              ( [], POINTER(c_int), 'pVersion' )),
]

class FileWriter(CoClass):
    'http://msdn.microsoft.com/library/default.asp?url=/library/en-us/directshow/htm/filewriterfilter.asp'
    _reg_clsid_ = GUID('{8596E5F0-0DA5-11D0-BD21-00A0C911CE86}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
class IFileSinkFilter2(IFileSinkFilter):
    _case_insensitive_ = True
    _iid_ = GUID('{00855B90-CE1B-11D0-BD4F-00A0C911CE86}')
    _idlflags_ = []
FileWriter._com_interfaces_ = [IFileSinkFilter2, IBaseFilter]


# values for enumeration '_DVDECODERRESOLUTION'
DVDECODERRESOLUTION_720x480 = 1000
DVDECODERRESOLUTION_360x240 = 1001
DVDECODERRESOLUTION_180x120 = 1002
DVDECODERRESOLUTION_88x60 = 1003
_DVDECODERRESOLUTION = c_int # enum
class IVMRImagePresenter(IUnknown):
    _case_insensitive_ = True
    'IVMRImagePresenter Interface'
    _iid_ = GUID('{CE704FE7-E71E-41FB-BAA2-C4403E1182F5}')
    _idlflags_ = []
class tagVMRPRESENTATIONINFO(Structure):
    pass
IVMRImagePresenter._methods_ = [
    COMMETHOD([], HRESULT, 'StartPresenting',
              ( ['in'], ULONG_PTR, 'dwUserID' )),
    COMMETHOD([], HRESULT, 'StopPresenting',
              ( ['in'], ULONG_PTR, 'dwUserID' )),
    COMMETHOD([], HRESULT, 'PresentImage',
              ( ['in'], ULONG_PTR, 'dwUserID' ),
              ( ['in'], POINTER(tagVMRPRESENTATIONINFO), 'lpPresInfo' )),
]

class IVMRMonitorConfig(IUnknown):
    _case_insensitive_ = True
    'IVMRMonitorConfig Interface'
    _iid_ = GUID('{9CF0B1B6-FBAA-4B7F-88CF-CF1F130A0DCE}')
    _idlflags_ = []
IVMRMonitorConfig._methods_ = [
    COMMETHOD([], HRESULT, 'SetMonitor',
              ( ['in'], POINTER(tagVMRGUID), 'pGUID' )),
    COMMETHOD([], HRESULT, 'GetMonitor',
              ( ['out'], POINTER(tagVMRGUID), 'pGUID' )),
    COMMETHOD([], HRESULT, 'SetDefaultMonitor',
              ( ['in'], POINTER(tagVMRGUID), 'pGUID' )),
    COMMETHOD([], HRESULT, 'GetDefaultMonitor',
              ( ['out'], POINTER(tagVMRGUID), 'pGUID' )),
    COMMETHOD([], HRESULT, 'GetAvailableMonitors',
              ( ['out'], POINTER(tagVMRMONITORINFO), 'pInfo' ),
              ( ['in'], c_ulong, 'dwMaxInfoArraySize' ),
              ( ['out'], POINTER(c_ulong), 'pdwNumDevices' )),
]

class IMediaEventSink(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A2-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IMediaEventSink._methods_ = [
    COMMETHOD([], HRESULT, 'Notify',
              ( ['in'], c_int, 'EventCode' ),
              ( ['in'], LONG_PTR, 'EventParam1' ),
              ( ['in'], LONG_PTR, 'EventParam2' )),
]

class __MIDL___MIDL_itf_DirectShow_0130_0001(Structure):
    pass
REGFILTER = __MIDL___MIDL_itf_DirectShow_0130_0001
__MIDL___MIDL_itf_DirectShow_0134_0005._fields_ = [
    ('dwFlags', c_ulong),
    ('cInstances', c_uint),
    ('nMediaTypes', c_uint),
    ('lpMediaType', POINTER(REGPINTYPES)),
    ('nMediums', c_uint),
    ('lpMedium', POINTER(REGPINMEDIUM)),
    ('clsPinCategory', POINTER(GUID)),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_DirectShow_0134_0005 is skipped.

# values for enumeration '_REM_FILTER_FLAGS'
REMFILTERF_LEAVECONNECTED = 1
_REM_FILTER_FLAGS = c_int # enum
IFileSinkFilter._methods_ = [
    COMMETHOD([], HRESULT, 'SetFileName',
              ( ['in'], WSTRING, 'pszFileName' ),
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'GetCurFile',
              ( ['out'], POINTER(WSTRING), 'ppszFileName' ),
              ( ['out'], POINTER(_AMMediaType), 'pmt' )),
]

IFileSinkFilter2._methods_ = [
    COMMETHOD([], HRESULT, 'SetMode',
              ( ['in'], c_ulong, 'dwFlags' )),
    COMMETHOD([], HRESULT, 'GetMode',
              ( ['out'], POINTER(c_ulong), 'pdwFlags' )),
]

class _VMRFrequency(Structure):
    pass
_VMRFrequency._fields_ = [
    ('dwNumerator', c_ulong),
    ('dwDenominator', c_ulong),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for _VMRFrequency is skipped.
_VMRVideoDesc._fields_ = [
    ('dwSize', c_ulong),
    ('dwSampleWidth', c_ulong),
    ('dwSampleHeight', c_ulong),
    ('SingleFieldPerSample', c_int),
    ('dwFourCC', c_ulong),
    ('InputSampleFreq', _VMRFrequency),
    ('OutputFrameFreq', _VMRFrequency),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for _VMRVideoDesc is skipped.

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0370_0002'
VMRSample_SyncPoint = 1
VMRSample_Preroll = 2
VMRSample_Discontinuity = 4
VMRSample_TimeValid = 8
__MIDL___MIDL_itf_DirectShow_0370_0002 = c_int # enum
class IDVRGB219(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{58473A19-2BC8-4663-8012-25F81BABDDD1}')
    _idlflags_ = []
IDVRGB219._methods_ = [
    COMMETHOD([], HRESULT, 'SetRGB219',
              ( ['in'], c_int, 'bState' )),
]

class IAMAnalogVideoDecoder(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13350-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMAnalogVideoDecoder._methods_ = [
    COMMETHOD([], HRESULT, 'get_AvailableTVFormats',
              ( ['out'], POINTER(c_int), 'lAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'put_TVFormat',
              ( ['in'], c_int, 'lAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'get_TVFormat',
              ( ['out'], POINTER(c_int), 'plAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'get_HorizontalLocked',
              ( ['out'], POINTER(c_int), 'plLocked' )),
    COMMETHOD([], HRESULT, 'put_VCRHorizontalLocking',
              ( ['in'], c_int, 'lVCRHorizontalLocking' )),
    COMMETHOD([], HRESULT, 'get_VCRHorizontalLocking',
              ( ['out'], POINTER(c_int), 'plVCRHorizontalLocking' )),
    COMMETHOD([], HRESULT, 'get_NumberOfLines',
              ( ['out'], POINTER(c_int), 'plNumberOfLines' )),
    COMMETHOD([], HRESULT, 'put_OutputEnable',
              ( ['in'], c_int, 'lOutputEnable' )),
    COMMETHOD([], HRESULT, 'get_OutputEnable',
              ( ['out'], POINTER(c_int), 'plOutputEnable' )),
]

# values for enumeration '_DVRESOLUTION'
DVRESOLUTION_FULL = 1000
DVRESOLUTION_HALF = 1001
DVRESOLUTION_QUARTER = 1002
DVRESOLUTION_DC = 1003
_DVRESOLUTION = c_int # enum

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0374_0001'
MixerPref_NoDecimation = 1
MixerPref_DecimateOutput = 2
MixerPref_DecimateMask = 15
MixerPref_BiLinearFiltering = 16
MixerPref_PointFiltering = 32
MixerPref_FilteringMask = 240
MixerPref_RenderTargetRGB = 256
MixerPref_RenderTargetYUV420 = 512
MixerPref_RenderTargetYUV422 = 1024
MixerPref_RenderTargetYUV444 = 2048
MixerPref_RenderTargetReserved = 61440
MixerPref_RenderTargetMask = 65280
__MIDL___MIDL_itf_DirectShow_0374_0001 = c_int # enum
class IEnumFilters(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86893-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

class IPin(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86891-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IFilterGraph._methods_ = [
    COMMETHOD([], HRESULT, 'AddFilter',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' ),
              ( ['in'], WSTRING, 'pName' )),
    COMMETHOD([], HRESULT, 'RemoveFilter',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' )),
    COMMETHOD([], HRESULT, 'EnumFilters',
              ( ['out'], POINTER(POINTER(IEnumFilters)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'FindFilterByName',
              ( ['in'], WSTRING, 'pName' ),
              ( ['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter' )),
    COMMETHOD([], HRESULT, 'ConnectDirect',
              ( ['in'], POINTER(IPin), 'ppinOut' ),
              ( ['in'], POINTER(IPin), 'ppinIn' ),
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'Reconnect',
              ( ['in'], POINTER(IPin), 'pPin' )),
    COMMETHOD([], HRESULT, 'Disconnect',
              ( ['in'], POINTER(IPin), 'pPin' )),
    COMMETHOD([], HRESULT, 'SetDefaultSyncSource'),
]

IGraphBuilder._methods_ = [
    COMMETHOD([], HRESULT, 'Connect',
              ( ['in'], POINTER(IPin), 'ppinOut' ),
              ( ['in'], POINTER(IPin), 'ppinIn' )),
    COMMETHOD([], HRESULT, 'Render',
              ( ['in'], POINTER(IPin), 'ppinOut' )),
    COMMETHOD([], HRESULT, 'RenderFile',
              ( ['in'], WSTRING, 'lpcwstrFile' ),
              ( ['in'], WSTRING, 'lpcwstrPlayList' )),
    COMMETHOD([], HRESULT, 'AddSourceFilter',
              ( ['in'], WSTRING, 'lpcwstrFileName' ),
              ( ['in'], WSTRING, 'lpcwstrFilterName' ),
              ( ['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter' )),
    COMMETHOD([], HRESULT, 'SetLogFile',
              ( ['in'], ULONG_PTR, 'hFile' )),
    COMMETHOD([], HRESULT, 'Abort'),
    COMMETHOD([], HRESULT, 'ShouldOperationContinue'),
]

class DvVideoDecoder(CoClass):
    'http://msdn.microsoft.com/library/default.asp?url=/library/en-us/directshow/htm/dvvideodecoderfilter.asp'
    _reg_clsid_ = GUID('{B1B77C00-C3E4-11CF-AF79-00AA00B67A42}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
class IIPDVDec(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B8E8BD60-0BFE-11D0-AF91-00AA00B67A42}')
    _idlflags_ = []
DvVideoDecoder._com_interfaces_ = [IIPDVDec, IDVRGB219, IBaseFilter]


# values for enumeration '__MIDL___MIDL_itf_DirectShow_0376_0003'
MAX_NUMBER_OF_STREAMS = 16
__MIDL___MIDL_itf_DirectShow_0376_0003 = c_int # enum
class IVMRSurfaceAllocatorNotify(IUnknown):
    _case_insensitive_ = True
    'IVMRSurfaceAllocatorNotify Interface'
    _iid_ = GUID('{AADA05A8-5A4E-4729-AF0B-CEA27AED51E2}')
    _idlflags_ = []
class IVMRSurfaceAllocator(IUnknown):
    _case_insensitive_ = True
    'IVMRSurfaceAllocator Interface'
    _iid_ = GUID('{31CE832E-4484-458B-8CCA-F4D7E3DB0B52}')
    _idlflags_ = []
IVMRSurfaceAllocatorNotify._methods_ = [
    COMMETHOD([], HRESULT, 'AdviseSurfaceAllocator',
              ( ['in'], ULONG_PTR, 'dwUserID' ),
              ( ['in'], POINTER(IVMRSurfaceAllocator), 'lpIVRMSurfaceAllocator' )),
    COMMETHOD([], HRESULT, 'SetDDrawDevice',
              ( ['in'], POINTER(c_ulong), 'lpDDrawDevice' ),
              ( ['in'], c_void_p, 'hMonitor' )),
    COMMETHOD([], HRESULT, 'ChangeDDrawDevice',
              ( ['in'], POINTER(c_ulong), 'lpDDrawDevice' ),
              ( ['in'], c_void_p, 'hMonitor' )),
    COMMETHOD([], HRESULT, 'RestoreDDrawSurfaces'),
    COMMETHOD([], HRESULT, 'NotifyEvent',
              ( ['in'], c_int, 'EventCode' ),
              ( ['in'], LONG_PTR, 'Param1' ),
              ( ['in'], LONG_PTR, 'Param2' )),
    COMMETHOD([], HRESULT, 'SetBorderColor',
              ( ['in'], c_ulong, 'clrBorder' )),
]

VMRSurfaceAllocationFlags = __MIDL___MIDL_itf_DirectShow_0371_0001
class IAMResourceControl(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{8389D2D0-77D7-11D1-ABE6-00A0C905F375}')
    _idlflags_ = []
IAMResourceControl._methods_ = [
    COMMETHOD([], HRESULT, 'Reserve',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], c_void_p, 'pvReserved' )),
]

# values for enumeration '_AM_AUDIO_RENDERER_STAT_PARAM'
AM_AUDREND_STAT_PARAM_BREAK_COUNT = 1
AM_AUDREND_STAT_PARAM_SLAVE_MODE = 2
AM_AUDREND_STAT_PARAM_SILENCE_DUR = 3
AM_AUDREND_STAT_PARAM_LAST_BUFFER_DUR = 4
AM_AUDREND_STAT_PARAM_DISCONTINUITIES = 5
AM_AUDREND_STAT_PARAM_SLAVE_RATE = 6
AM_AUDREND_STAT_PARAM_SLAVE_DROPWRITE_DUR = 7
AM_AUDREND_STAT_PARAM_SLAVE_HIGHLOWERROR = 8
AM_AUDREND_STAT_PARAM_SLAVE_LASTHIGHLOWERROR = 9
AM_AUDREND_STAT_PARAM_SLAVE_ACCUMERROR = 10
AM_AUDREND_STAT_PARAM_BUFFERFULLNESS = 11
AM_AUDREND_STAT_PARAM_JITTER = 12
_AM_AUDIO_RENDERER_STAT_PARAM = c_int # enum
IVMRSurfaceAllocator._methods_ = [
    COMMETHOD([], HRESULT, 'AllocateSurface',
              ( ['in'], ULONG_PTR, 'dwUserID' ),
              ( ['in'], POINTER(tagVMRALLOCATIONINFO), 'lpAllocInfo' ),
              ( ['in', 'out'], POINTER(c_ulong), 'lpdwActualBuffers' ),
              ( ['out'], POINTER(POINTER(c_ulong)), 'lplpSurface' )),
    COMMETHOD([], HRESULT, 'FreeSurface',
              ( ['in'], ULONG_PTR, 'dwID' )),
    COMMETHOD([], HRESULT, 'PrepareSurface',
              ( ['in'], ULONG_PTR, 'dwUserID' ),
              ( ['in'], POINTER(c_ulong), 'lpSurface' ),
              ( ['in'], c_ulong, 'dwSurfaceFlags' )),
    COMMETHOD([], HRESULT, 'AdviseNotify',
              ( ['in'], POINTER(IVMRSurfaceAllocatorNotify), 'lpIVMRSurfAllocNotify' )),
]

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0373_0001'
VMR_ARMODE_NONE = 0
VMR_ARMODE_LETTER_BOX = 1
__MIDL___MIDL_itf_DirectShow_0373_0001 = c_int # enum

# values for enumeration '_AM_GRAPH_CONFIG_RECONNECT_FLAGS'
AM_GRAPH_CONFIG_RECONNECT_DIRECTCONNECT = 1
AM_GRAPH_CONFIG_RECONNECT_CACHE_REMOVED_FILTERS = 2
AM_GRAPH_CONFIG_RECONNECT_USE_ONLY_CACHED_FILTERS = 4
_AM_GRAPH_CONFIG_RECONNECT_FLAGS = c_int # enum
VMRPresentationFlags = __MIDL___MIDL_itf_DirectShow_0370_0002
VideoCopyProtectionType = __MIDL___MIDL_itf_DirectShow_0169_0001
VMR_ASPECT_RATIO_MODE = __MIDL___MIDL_itf_DirectShow_0373_0001
class DvSplitter(CoClass):
    'http://msdn.microsoft.com/library/default.asp?url=/library/en-us/directshow/htm/dvsplitterfilter.asp'
    _reg_clsid_ = GUID('{4EB31670-9FC6-11CF-AF6E-00AA00B67A42}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
class IDVSplitter(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{92A3A302-DA7C-4A1F-BA7E-1802BB5D2D02}')
    _idlflags_ = []
DvSplitter._com_interfaces_ = [IDVSplitter, IBaseFilter]


# values for enumeration '_DVENCODERVIDEOFORMAT'
DVENCODERVIDEOFORMAT_NTSC = 2000
DVENCODERVIDEOFORMAT_PAL = 2001
_DVENCODERVIDEOFORMAT = c_int # enum
class IGraphConfig(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{03A1EB8E-32BF-4245-8502-114D08A9CB88}')
    _idlflags_ = []
class IGraphConfigCallback(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{ADE0FD60-D19D-11D2-ABF6-00A0C905F375}')
    _idlflags_ = []
IGraphConfig._methods_ = [
    COMMETHOD([], HRESULT, 'Reconnect',
              ( ['in'], POINTER(IPin), 'pOutputPin' ),
              ( ['in'], POINTER(IPin), 'pInputPin' ),
              ( ['in'], POINTER(_AMMediaType), 'pmtFirstConnection' ),
              ( ['in'], POINTER(IBaseFilter), 'pUsingFilter' ),
              ( ['in'], c_void_p, 'hAbortEvent' ),
              ( ['in'], c_ulong, 'dwFlags' )),
    COMMETHOD([], HRESULT, 'Reconfigure',
              ( ['in'], POINTER(IGraphConfigCallback), 'pCallback' ),
              ( ['in'], c_void_p, 'pvContext' ),
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], c_void_p, 'hAbortEvent' )),
    COMMETHOD([], HRESULT, 'AddFilterToCache',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' )),
    COMMETHOD([], HRESULT, 'EnumCacheFilter',
              ( ['out'], POINTER(POINTER(IEnumFilters)), 'pEnum' )),
    COMMETHOD([], HRESULT, 'RemoveFilterFromCache',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' )),
    COMMETHOD([], HRESULT, 'GetStartTime',
              ( ['out'], POINTER(c_longlong), 'prtStart' )),
    COMMETHOD([], HRESULT, 'PushThroughData',
              ( ['in'], POINTER(IPin), 'pOutputPin' ),
              ( ['in'], POINTER(IPinConnection), 'pConnection' ),
              ( ['in'], c_void_p, 'hEventAbort' )),
    COMMETHOD([], HRESULT, 'SetFilterFlags',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' ),
              ( ['in'], c_ulong, 'dwFlags' )),
    COMMETHOD([], HRESULT, 'GetFilterFlags',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' ),
              ( ['out'], POINTER(c_ulong), 'pdwFlags' )),
    COMMETHOD([], HRESULT, 'RemoveFilterEx',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' ),
              ( [], c_ulong, 'Flags' )),
]

class IFilterMapper(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A3-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IEnumRegFilters(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A4-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

IFilterMapper._methods_ = [
    COMMETHOD([], HRESULT, 'RegisterFilter',
              ( ['in'], GUID, 'clsid' ),
              ( ['in'], WSTRING, 'Name' ),
              ( ['in'], c_ulong, 'dwMerit' )),
    COMMETHOD([], HRESULT, 'RegisterFilterInstance',
              ( ['in'], GUID, 'clsid' ),
              ( ['in'], WSTRING, 'Name' ),
              ( ['out'], POINTER(GUID), 'MRId' )),
    COMMETHOD([], HRESULT, 'RegisterPin',
              ( ['in'], GUID, 'Filter' ),
              ( ['in'], WSTRING, 'Name' ),
              ( ['in'], c_int, 'bRendered' ),
              ( ['in'], c_int, 'bOutput' ),
              ( ['in'], c_int, 'bZero' ),
              ( ['in'], c_int, 'bMany' ),
              ( ['in'], GUID, 'ConnectsToFilter' ),
              ( ['in'], WSTRING, 'ConnectsToPin' )),
    COMMETHOD([], HRESULT, 'RegisterPinType',
              ( ['in'], GUID, 'clsFilter' ),
              ( ['in'], WSTRING, 'strName' ),
              ( ['in'], GUID, 'clsMajorType' ),
              ( ['in'], GUID, 'clsSubType' )),
    COMMETHOD([], HRESULT, 'UnregisterFilter',
              ( ['in'], GUID, 'Filter' )),
    COMMETHOD([], HRESULT, 'UnregisterFilterInstance',
              ( ['in'], GUID, 'MRId' )),
    COMMETHOD([], HRESULT, 'UnregisterPin',
              ( ['in'], GUID, 'Filter' ),
              ( ['in'], WSTRING, 'Name' )),
    COMMETHOD([], HRESULT, 'EnumMatchingFilters',
              ( ['out'], POINTER(POINTER(IEnumRegFilters)), 'ppenum' ),
              ( ['in'], c_ulong, 'dwMerit' ),
              ( ['in'], c_int, 'bInputNeeded' ),
              ( ['in'], GUID, 'clsInMaj' ),
              ( ['in'], GUID, 'clsInSub' ),
              ( ['in'], c_int, 'bRender' ),
              ( ['in'], c_int, 'bOututNeeded' ),
              ( ['in'], GUID, 'clsOutMaj' ),
              ( ['in'], GUID, 'clsOutSub' )),
]

__MIDL___MIDL_itf_DirectShow_0134_0006._fields_ = [
    ('dwVersion', c_ulong),
    ('dwMerit', c_ulong),
    ('__MIDL_0014', __MIDL___MIDL_itf_DirectShow_0134_0007),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_DirectShow_0134_0006 is skipped.
tagCOLORKEY._fields_ = [
    ('KeyType', c_ulong),
    ('PaletteIndex', c_ulong),
    ('LowColorValue', c_ulong),
    ('HighColorValue', c_ulong),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for tagCOLORKEY is skipped.
IOverlayNotify._methods_ = [
    COMMETHOD([], HRESULT, 'OnPaletteChange',
              ( ['in'], c_ulong, 'dwColors' ),
              ( ['in'], POINTER(tagPALETTEENTRY), 'pPalette' )),
    COMMETHOD([], HRESULT, 'OnClipChange',
              ( ['in'], POINTER(tagRECT), 'pSourceRect' ),
              ( ['in'], POINTER(tagRECT), 'pDestinationRect' ),
              ( ['in'], POINTER(_RGNDATA), 'pRgnData' )),
    COMMETHOD([], HRESULT, 'OnColorKeyChange',
              ( ['in'], POINTER(tagCOLORKEY), 'pColorKey' )),
    COMMETHOD([], HRESULT, 'OnPositionChange',
              ( ['in'], POINTER(tagRECT), 'pSourceRect' ),
              ( ['in'], POINTER(tagRECT), 'pDestinationRect' )),
]

# values for enumeration '_AM_PIN_FLOW_CONTROL_BLOCK_FLAGS'
AM_PIN_FLOW_CONTROL_BLOCK = 1
_AM_PIN_FLOW_CONTROL_BLOCK_FLAGS = c_int # enum
class ICodecAPI(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{901DB4C7-31CE-41A2-85DC-8FA0BF41B8DA}')
    _idlflags_ = []
ICodecAPI._methods_ = [
    COMMETHOD([], HRESULT, 'IsSupported',
              ( ['in'], POINTER(GUID), 'Api' )),
    COMMETHOD([], HRESULT, 'IsModifiable',
              ( ['in'], POINTER(GUID), 'Api' )),
    COMMETHOD([], HRESULT, 'GetParameterRange',
              ( ['in'], POINTER(GUID), 'Api' ),
              ( ['out'], POINTER(VARIANT), 'ValueMin' ),
              ( ['out'], POINTER(VARIANT), 'ValueMax' ),
              ( ['out'], POINTER(VARIANT), 'SteppingDelta' )),
    COMMETHOD([], HRESULT, 'GetParameterValues',
              ( ['in'], POINTER(GUID), 'Api' ),
              ( ['out'], POINTER(POINTER(VARIANT)), 'Values' ),
              ( ['out'], POINTER(c_ulong), 'ValuesCount' )),
    COMMETHOD([], HRESULT, 'GetDefaultValue',
              ( ['in'], POINTER(GUID), 'Api' ),
              ( ['out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([], HRESULT, 'GetValue',
              ( ['in'], POINTER(GUID), 'Api' ),
              ( ['out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([], HRESULT, 'SetValue',
              ( ['in'], POINTER(GUID), 'Api' ),
              ( ['in'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([], HRESULT, 'RegisterForEvent',
              ( ['in'], POINTER(GUID), 'Api' ),
              ( ['in'], LONG_PTR, 'userData' )),
    COMMETHOD([], HRESULT, 'UnregisterForEvent',
              ( ['in'], POINTER(GUID), 'Api' )),
    COMMETHOD([], HRESULT, 'SetAllDefaults'),
    COMMETHOD([], HRESULT, 'SetValueWithNotify',
              ( ['in'], POINTER(GUID), 'Api' ),
              ( ['in'], POINTER(VARIANT), 'Value' ),
              ( ['out'], POINTER(POINTER(GUID)), 'ChangedParam' ),
              ( ['out'], POINTER(c_ulong), 'ChangedParamCount' )),
    COMMETHOD([], HRESULT, 'SetAllDefaultsWithNotify',
              ( ['out'], POINTER(POINTER(GUID)), 'ChangedParam' ),
              ( ['out'], POINTER(c_ulong), 'ChangedParamCount' )),
    COMMETHOD([], HRESULT, 'GetAllSettings',
              ( ['in'], POINTER(IStream), '__MIDL_0016' )),
    COMMETHOD([], HRESULT, 'SetAllSettings',
              ( ['in'], POINTER(IStream), '__MIDL_0017' )),
    COMMETHOD([], HRESULT, 'SetAllSettingsWithNotify',
              ( [], POINTER(IStream), '__MIDL_0018' ),
              ( ['out'], POINTER(POINTER(GUID)), 'ChangedParam' ),
              ( ['out'], POINTER(c_ulong), 'ChangedParamCount' )),
]

class IVMRSurface(IUnknown):
    _case_insensitive_ = True
    'IVMRSurface Interface'
    _iid_ = GUID('{A9849BBE-9EC8-4263-B764-62730F0D15D0}')
    _idlflags_ = []
IVMRSurface._methods_ = [
    COMMETHOD([], HRESULT, 'IsSurfaceLocked'),
    COMMETHOD([], HRESULT, 'LockSurface',
              ( ['out'], POINTER(POINTER(c_ubyte)), 'lpSurface' )),
    COMMETHOD([], HRESULT, 'UnlockSurface'),
    COMMETHOD([], HRESULT, 'GetSurface',
              ( ['out'], POINTER(POINTER(c_ulong)), 'lplpSurface' )),
]

class IAMVfwCompressDialogs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D8D715A3-6E5E-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []
IAMVfwCompressDialogs._methods_ = [
    COMMETHOD([], HRESULT, 'ShowDialog',
              ( ['in'], c_int, 'iDialog' ),
              ( ['in'], wireHWND, 'hwnd' )),
    COMMETHOD([], HRESULT, 'GetState',
              ( ['out'], c_void_p, 'pState' ),
              ( ['in', 'out'], POINTER(c_int), 'pcbState' )),
    COMMETHOD([], HRESULT, 'SetState',
              ( ['in'], c_void_p, 'pState' ),
              ( ['in'], c_int, 'cbState' )),
    COMMETHOD([], HRESULT, 'SendDriverMessage',
              ( ['in'], c_int, 'uMsg' ),
              ( ['in'], c_int, 'dw1' ),
              ( ['in'], c_int, 'dw2' )),
]

# values for enumeration 'tagVideoProcAmpProperty'
VideoProcAmp_Brightness = 0
VideoProcAmp_Contrast = 1
VideoProcAmp_Hue = 2
VideoProcAmp_Saturation = 3
VideoProcAmp_Sharpness = 4
VideoProcAmp_Gamma = 5
VideoProcAmp_ColorEnable = 6
VideoProcAmp_WhiteBalance = 7
VideoProcAmp_BacklightCompensation = 8
VideoProcAmp_Gain = 9
tagVideoProcAmpProperty = c_int # enum

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0376_0001'
RenderPrefs_RestrictToInitialMonitor = 0
RenderPrefs_ForceOffscreen = 1
RenderPrefs_ForceOverlays = 2
RenderPrefs_AllowOverlays = 0
RenderPrefs_AllowOffscreen = 0
RenderPrefs_DoNotRenderColorKeyAndBorder = 8
RenderPrefs_Reserved = 16
RenderPrefs_PreferAGPMemWhenMixing = 32
RenderPrefs_Mask = 63
__MIDL___MIDL_itf_DirectShow_0376_0001 = c_int # enum
class IAMVideoProcAmp(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13360-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMVideoProcAmp._methods_ = [
    COMMETHOD([], HRESULT, 'GetRange',
              ( ['in'], c_int, 'Property' ),
              ( ['out'], POINTER(c_int), 'pMin' ),
              ( ['out'], POINTER(c_int), 'pMax' ),
              ( ['out'], POINTER(c_int), 'pSteppingDelta' ),
              ( ['out'], POINTER(c_int), 'pDefault' ),
              ( ['out'], POINTER(c_int), 'pCapsFlags' )),
    COMMETHOD([], HRESULT, 'Set',
              ( ['in'], c_int, 'Property' ),
              ( ['in'], c_int, 'lValue' ),
              ( ['in'], c_int, 'Flags' )),
    COMMETHOD([], HRESULT, 'Get',
              ( ['in'], c_int, 'Property' ),
              ( ['out'], POINTER(c_int), 'lValue' ),
              ( ['out'], POINTER(c_int), 'Flags' )),
]

# values for enumeration 'tagVideoProcAmpFlags'
VideoProcAmp_Flags_Auto = 1
VideoProcAmp_Flags_Manual = 2
tagVideoProcAmpFlags = c_int # enum
IIPDVDec._methods_ = [
    COMMETHOD([], HRESULT, 'get_IPDisplay',
              ( ['out'], POINTER(c_int), 'displayPix' )),
    COMMETHOD([], HRESULT, 'put_IPDisplay',
              ( ['in'], c_int, 'displayPix' )),
]

_AllocatorProperties._fields_ = [
    ('cBuffers', c_int),
    ('cbBuffer', c_int),
    ('cbAlign', c_int),
    ('cbPrefix', c_int),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for _AllocatorProperties is skipped.
class IOverlayNotify2(IOverlayNotify):
    _case_insensitive_ = True
    _iid_ = GUID('{680EFA10-D535-11D1-87C8-00A0C9223196}')
    _idlflags_ = []
IOverlayNotify2._methods_ = [
    COMMETHOD([], HRESULT, 'OnDisplayChange',
              ( [], c_void_p, 'hMonitor' )),
]

VMRMixerPrefs = __MIDL___MIDL_itf_DirectShow_0374_0001
class IEnumMediaTypes(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{89C31040-846B-11CE-97D3-00AA0055595A}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

IPin._methods_ = [
    COMMETHOD([], HRESULT, 'Connect',
              ( ['in'], POINTER(IPin), 'pReceivePin' ),
              ( ['in'], c_ulong, 'pmt' )),
    COMMETHOD([], HRESULT, 'ReceiveConnection',
              ( ['in'], POINTER(IPin), 'pConnector' ),
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'Disconnect'),
    COMMETHOD([], HRESULT, 'ConnectedTo',
              ( ['out', 'retval'], POINTER(POINTER(IPin)), 'pPin' )),
    COMMETHOD([], HRESULT, 'ConnectionMediaType',
              ( ['out'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'QueryPinInfo',
              ( ['out', 'retval'], POINTER(_PinInfo), 'pInfo' )),
    COMMETHOD([], HRESULT, 'QueryDirection',
              ( ['out', 'retval'], POINTER(_PinDirection), 'pPinDir' )),
    COMMETHOD([], HRESULT, 'QueryId',
              ( ['out', 'retval'], POINTER(WSTRING), 'Id' )),
    COMMETHOD([], HRESULT, 'QueryAccept',
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'EnumMediaTypes',
              ( ['out', 'retval'], POINTER(POINTER(IEnumMediaTypes)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'QueryInternalConnections',
              ( ['out'], POINTER(POINTER(IPin)), 'apPin' ),
              ( ['in', 'out'], POINTER(c_ulong), 'nPin' )),
    COMMETHOD([], HRESULT, 'EndOfStream'),
    COMMETHOD([], HRESULT, 'BeginFlush'),
    COMMETHOD([], HRESULT, 'EndFlush'),
    COMMETHOD([], HRESULT, 'NewSegment',
              ( ['in'], c_longlong, 'tStart' ),
              ( ['in'], c_longlong, 'tStop' ),
              ( ['in'], c_double, 'dRate' )),
]

# values for enumeration '_DECIMATION_USAGE'
DECIMATION_LEGACY = 0
DECIMATION_USE_DECODER_ONLY = 1
DECIMATION_USE_VIDEOPORT_ONLY = 2
DECIMATION_USE_OVERLAY_ONLY = 3
DECIMATION_DEFAULT = 4
_DECIMATION_USAGE = c_int # enum
IMoniker._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteBindToObject',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], POINTER(GUID), 'riidResult' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppvResult' )),
    COMMETHOD([], HRESULT, 'RemoteBindToStorage',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppvObj' )),
    COMMETHOD([], HRESULT, 'Reduce',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], c_ulong, 'dwReduceHowFar' ),
              ( ['in', 'out'], POINTER(POINTER(IMoniker)), 'ppmkToLeft' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkReduced' )),
    COMMETHOD([], HRESULT, 'ComposeWith',
              ( ['in'], POINTER(IMoniker), 'pmkRight' ),
              ( ['in'], c_int, 'fOnlyIfNotGeneric' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkComposite' )),
    COMMETHOD([], HRESULT, 'Enum',
              ( ['in'], c_int, 'fForward' ),
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenumMoniker' )),
    COMMETHOD([], HRESULT, 'IsEqual',
              ( ['in'], POINTER(IMoniker), 'pmkOtherMoniker' )),
    COMMETHOD([], HRESULT, 'Hash',
              ( ['out'], POINTER(c_ulong), 'pdwHash' )),
    COMMETHOD([], HRESULT, 'IsRunning',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], POINTER(IMoniker), 'pmkNewlyRunning' )),
    COMMETHOD([], HRESULT, 'GetTimeOfLastChange',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['out'], POINTER(_FILETIME), 'pfiletime' )),
    COMMETHOD([], HRESULT, 'Inverse',
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmk' )),
    COMMETHOD([], HRESULT, 'CommonPrefixWith',
              ( ['in'], POINTER(IMoniker), 'pmkOther' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkPrefix' )),
    COMMETHOD([], HRESULT, 'RelativePathTo',
              ( ['in'], POINTER(IMoniker), 'pmkOther' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkRelPath' )),
    COMMETHOD([], HRESULT, 'GetDisplayName',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['out'], POINTER(WSTRING), 'ppszDisplayName' )),
    COMMETHOD([], HRESULT, 'ParseDisplayName',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], WSTRING, 'pszDisplayName' ),
              ( ['out'], POINTER(c_ulong), 'pchEaten' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkOut' )),
    COMMETHOD([], HRESULT, 'IsSystemMoniker',
              ( ['out'], POINTER(c_ulong), 'pdwMksys' )),
]

class IVideoEncoder(IEncoderAPI):
    _case_insensitive_ = True
    _iid_ = GUID('{02997C3B-8E1B-460E-9270-545E0DE9563E}')
    _idlflags_ = []
IVideoEncoder._methods_ = [
]
################################################################
## code template for IVideoEncoder implementation
##class IVideoEncoder_Impl(object):

class __MIDL___MIDL_itf_DirectShow_0355_0001(Structure):
    pass
STREAM_ID_MAP = __MIDL___MIDL_itf_DirectShow_0355_0001
IEnumStreamIdMap._methods_ = [
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'cRequest' ),
              ( ['in', 'out'], POINTER(STREAM_ID_MAP), 'pStreamIdMap' ),
              ( ['out'], POINTER(c_ulong), 'pcReceived' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'cRecords' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumStreamIdMap)), 'ppIEnumStreamIdMap' )),
]

class IAMClockAdjust(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4D5466B0-A49C-11D1-ABE8-00A0C905F375}')
    _idlflags_ = []
IAMClockAdjust._methods_ = [
    COMMETHOD([], HRESULT, 'SetClockDelta',
              ( ['in'], c_longlong, 'rtDelta' )),
]

class __MIDL_IWinTypes_0009(Union):
    pass
__MIDL_IWinTypes_0009._fields_ = [
    ('hInproc', c_int),
    ('hRemote', c_int),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL_IWinTypes_0009 is skipped.
class IDrawVideoImage(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{48EFB120-AB49-11D2-AED2-00A0C995E8D5}')
    _idlflags_ = []
IDrawVideoImage._methods_ = [
    COMMETHOD([], HRESULT, 'DrawVideoImageBegin'),
    COMMETHOD([], HRESULT, 'DrawVideoImageEnd'),
    COMMETHOD([], HRESULT, 'DrawVideoImageDraw',
              ( ['in'], wireHDC, 'hdc' ),
              ( ['in'], POINTER(tagRECT), 'lprcSrc' ),
              ( ['in'], POINTER(tagRECT), 'lprcDst' )),
]

class AviSplitter(CoClass):
    'http://msdn.microsoft.com/library/default.asp?url=/library/en-us/directshow/htm/avisplitterfilter.asp'
    _reg_clsid_ = GUID('{1B544C20-FD0B-11CE-8C63-00AA0044B51E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
class IPersistMediaPropertyBag(IPersist):
    _case_insensitive_ = True
    _iid_ = GUID('{5738E040-B67F-11D0-BD4D-00A0C911CE86}')
    _idlflags_ = []
AviSplitter._com_interfaces_ = [IBaseFilter, IPersistMediaPropertyBag]

_RemotableHandle._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0009),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for _RemotableHandle is skipped.
class IAMGraphBuilderCallback(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4995F511-9DDB-4F12-BD3B-F04611807B79}')
    _idlflags_ = []
IAMGraphBuilderCallback._methods_ = [
    COMMETHOD([], HRESULT, 'SelectedFilter',
              ( ['in'], POINTER(IMoniker), 'pMon' )),
    COMMETHOD([], HRESULT, 'CreatedFilter',
              ( ['in'], POINTER(IBaseFilter), 'pFil' )),
]

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0156_0001'
AM_STREAM_INFO_START_DEFINED = 1
AM_STREAM_INFO_STOP_DEFINED = 2
AM_STREAM_INFO_DISCARDING = 4
AM_STREAM_INFO_STOP_SEND_EXTRA = 16
__MIDL___MIDL_itf_DirectShow_0156_0001 = c_int # enum
ISequentialStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteRead',
              ( ['out'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbRead' )),
    COMMETHOD([], HRESULT, 'RemoteWrite',
              ( ['in'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbWritten' )),
]

_AMMediaType._fields_ = [
    ('majortype', GUID),
    ('subtype', GUID),
    ('bFixedSizeSamples', c_int),
    ('bTemporalCompression', c_int),
    ('lSampleSize', c_ulong),
    ('formattype', GUID),
    ('punk', POINTER(IUnknown)),
    ('cbFormat', c_ulong),
    ('pbFormat', POINTER(c_ubyte)),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for _AMMediaType is skipped.
IEnumRegFilters._methods_ = [
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'cFilters' ),
              ( ['out'], POINTER(POINTER(REGFILTER)), 'apRegFilter' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'cFilters' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumRegFilters)), 'ppenum' )),
]

class ISeekingPassThru(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{36B73883-C2C8-11CF-8B46-00805F6CEF60}')
    _idlflags_ = []
ISeekingPassThru._methods_ = [
    COMMETHOD([], HRESULT, 'Init',
              ( ['in'], c_int, 'bSupportRendering' ),
              ( ['in'], POINTER(IPin), 'pPin' )),
]

# values for enumeration '__MIDL_IConfigInterleaving_0001'
INTERLEAVE_NONE = 0
INTERLEAVE_CAPTURE = 1
INTERLEAVE_FULL = 2
INTERLEAVE_NONE_BUFFERED = 3
__MIDL_IConfigInterleaving_0001 = c_int # enum
InterleavingMode = __MIDL_IConfigInterleaving_0001
class IFileSourceFilter(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A6-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IFileSourceFilter._methods_ = [
    COMMETHOD([], HRESULT, 'Load',
              ( ['in'], WSTRING, 'pszFileName' ),
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'GetCurFile',
              ( ['out'], POINTER(WSTRING), 'ppszFileName' ),
              ( ['out'], POINTER(_AMMediaType), 'pmt' )),
]

class IAMLatency(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{62EA93BA-EC62-11D2-B770-00C04FB6BD3D}')
    _idlflags_ = []
IAMLatency._methods_ = [
    COMMETHOD([], HRESULT, 'GetLatency',
              ( ['in'], POINTER(c_longlong), 'prtLatency' )),
]

class IMediaSeeking(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{36B73880-C2C8-11CF-8B46-00805F6CEF60}')
    _idlflags_ = []
IMediaSeeking._methods_ = [
    COMMETHOD([], HRESULT, 'GetCapabilities',
              ( ['out'], POINTER(c_ulong), 'pCapabilities' )),
    COMMETHOD([], HRESULT, 'CheckCapabilities',
              ( ['in', 'out'], POINTER(c_ulong), 'pCapabilities' )),
    COMMETHOD([], HRESULT, 'IsFormatSupported',
              ( ['in'], POINTER(GUID), 'pFormat' )),
    COMMETHOD([], HRESULT, 'QueryPreferredFormat',
              ( ['out'], POINTER(GUID), 'pFormat' )),
    COMMETHOD([], HRESULT, 'GetTimeFormat',
              ( ['out'], POINTER(GUID), 'pFormat' )),
    COMMETHOD([], HRESULT, 'IsUsingTimeFormat',
              ( ['in'], POINTER(GUID), 'pFormat' )),
    COMMETHOD([], HRESULT, 'SetTimeFormat',
              ( ['in'], POINTER(GUID), 'pFormat' )),
    COMMETHOD([], HRESULT, 'GetDuration',
              ( ['out'], POINTER(c_longlong), 'pDuration' )),
    COMMETHOD([], HRESULT, 'GetStopPosition',
              ( ['out'], POINTER(c_longlong), 'pStop' )),
    COMMETHOD([], HRESULT, 'GetCurrentPosition',
              ( ['out'], POINTER(c_longlong), 'pCurrent' )),
    COMMETHOD([], HRESULT, 'ConvertTimeFormat',
              ( ['out'], POINTER(c_longlong), 'pTarget' ),
              ( ['in'], POINTER(GUID), 'pTargetFormat' ),
              ( ['in'], c_longlong, 'Source' ),
              ( ['in'], POINTER(GUID), 'pSourceFormat' )),
    COMMETHOD([], HRESULT, 'SetPositions',
              ( ['in', 'out'], POINTER(c_longlong), 'pCurrent' ),
              ( ['in'], c_ulong, 'dwCurrentFlags' ),
              ( ['in', 'out'], POINTER(c_longlong), 'pStop' ),
              ( ['in'], c_ulong, 'dwStopFlags' )),
    COMMETHOD([], HRESULT, 'GetPositions',
              ( ['out'], POINTER(c_longlong), 'pCurrent' ),
              ( ['out'], POINTER(c_longlong), 'pStop' )),
    COMMETHOD([], HRESULT, 'GetAvailable',
              ( ['out'], POINTER(c_longlong), 'pEarliest' ),
              ( ['out'], POINTER(c_longlong), 'pLatest' )),
    COMMETHOD([], HRESULT, 'SetRate',
              ( ['in'], c_double, 'dRate' )),
    COMMETHOD([], HRESULT, 'GetRate',
              ( ['out'], POINTER(c_double), 'pdRate' )),
    COMMETHOD([], HRESULT, 'GetPreroll',
              ( ['out'], POINTER(c_longlong), 'pllPreroll' )),
]

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0145_0001'
AM_FILE_OVERWRITE = 1
__MIDL___MIDL_itf_DirectShow_0145_0001 = c_int # enum
AM_STREAM_INFO_FLAGS = __MIDL___MIDL_itf_DirectShow_0156_0001
class IAMTuner(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{211A8761-03AC-11D1-8D13-00AA00BD8339}')
    _idlflags_ = []
class IAMTVTuner(IAMTuner):
    _case_insensitive_ = True
    _iid_ = GUID('{211A8766-03AC-11D1-8D13-00AA00BD8339}')
    _idlflags_ = []
IAMTuner._methods_ = [
    COMMETHOD([], HRESULT, 'put_Channel',
              ( ['in'], c_int, 'lChannel' ),
              ( ['in'], c_int, 'lVideoSubChannel' ),
              ( ['in'], c_int, 'lAudioSubChannel' )),
    COMMETHOD([], HRESULT, 'get_Channel',
              ( ['out'], POINTER(c_int), 'plChannel' ),
              ( ['out'], POINTER(c_int), 'plVideoSubChannel' ),
              ( ['out'], POINTER(c_int), 'plAudioSubChannel' )),
    COMMETHOD([], HRESULT, 'ChannelMinMax',
              ( ['out'], POINTER(c_int), 'lChannelMin' ),
              ( ['out'], POINTER(c_int), 'lChannelMax' )),
    COMMETHOD([], HRESULT, 'put_CountryCode',
              ( ['in'], c_int, 'lCountryCode' )),
    COMMETHOD([], HRESULT, 'get_CountryCode',
              ( ['out'], POINTER(c_int), 'plCountryCode' )),
    COMMETHOD([], HRESULT, 'put_TuningSpace',
              ( ['in'], c_int, 'lTuningSpace' )),
    COMMETHOD([], HRESULT, 'get_TuningSpace',
              ( ['out'], POINTER(c_int), 'plTuningSpace' )),
    COMMETHOD([], HRESULT, 'Logon',
              ( ['in'], c_void_p, 'hCurrentUser' )),
    COMMETHOD([], HRESULT, 'Logout'),
    COMMETHOD([], HRESULT, 'SignalPresent',
              ( ['out'], POINTER(c_int), 'plSignalStrength' )),
    COMMETHOD([], HRESULT, 'put_Mode',
              ( ['in'], tagAMTunerModeType, 'lMode' )),
    COMMETHOD([], HRESULT, 'get_Mode',
              ( ['out'], POINTER(tagAMTunerModeType), 'plMode' )),
    COMMETHOD([], HRESULT, 'GetAvailableModes',
              ( ['out'], POINTER(c_int), 'plModes' )),
    COMMETHOD([], HRESULT, 'RegisterNotificationCallBack',
              ( ['in'], POINTER(IAMTunerNotification), 'pNotify' ),
              ( ['in'], c_int, 'lEvents' )),
    COMMETHOD([], HRESULT, 'UnRegisterNotificationCallBack',
              ( ['in'], POINTER(IAMTunerNotification), 'pNotify' )),
]

# values for enumeration 'tagTunerInputType'
TunerInputCable = 0
TunerInputAntenna = 1
tagTunerInputType = c_int # enum
IAMTVTuner._methods_ = [
    COMMETHOD([], HRESULT, 'get_AvailableTVFormats',
              ( ['out'], POINTER(c_int), 'lAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'get_TVFormat',
              ( ['out'], POINTER(c_int), 'plAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'AutoTune',
              ( ['in'], c_int, 'lChannel' ),
              ( ['out'], POINTER(c_int), 'plFoundSignal' )),
    COMMETHOD([], HRESULT, 'StoreAutoTune'),
    COMMETHOD([], HRESULT, 'get_NumInputConnections',
              ( ['out'], POINTER(c_int), 'plNumInputConnections' )),
    COMMETHOD([], HRESULT, 'put_InputType',
              ( ['in'], c_int, 'lIndex' ),
              ( ['in'], tagTunerInputType, 'InputType' )),
    COMMETHOD([], HRESULT, 'get_InputType',
              ( ['in'], c_int, 'lIndex' ),
              ( ['out'], POINTER(tagTunerInputType), 'pInputType' )),
    COMMETHOD([], HRESULT, 'put_ConnectInput',
              ( ['in'], c_int, 'lIndex' )),
    COMMETHOD([], HRESULT, 'get_ConnectInput',
              ( ['out'], POINTER(c_int), 'plIndex' )),
    COMMETHOD([], HRESULT, 'get_VideoFrequency',
              ( ['out'], POINTER(c_int), 'lFreq' )),
    COMMETHOD([], HRESULT, 'get_AudioFrequency',
              ( ['out'], POINTER(c_int), 'lFreq' )),
]

IGraphConfigCallback._methods_ = [
    COMMETHOD([], HRESULT, 'Reconfigure',
              ( [], c_void_p, 'pvContext' ),
              ( [], c_ulong, 'dwFlags' )),
]

class IAMDeviceRemoval(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{F90A6130-B658-11D2-AE49-0000F8754B99}')
    _idlflags_ = []
IAMDeviceRemoval._methods_ = [
    COMMETHOD([], HRESULT, 'DeviceInfo',
              ( ['out'], POINTER(GUID), 'pclsidInterfaceClass' ),
              ( ['out'], POINTER(POINTER(c_ushort)), 'pwszSymbolicLink' )),
    COMMETHOD([], HRESULT, 'Reassociate'),
    COMMETHOD([], HRESULT, 'Disassociate'),
]

class IResourceManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868AC-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IResourceConsumer(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868AD-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IResourceManager._methods_ = [
    COMMETHOD([], HRESULT, 'Register',
              ( ['in'], WSTRING, 'pName' ),
              ( ['in'], c_int, 'cResource' ),
              ( ['out'], POINTER(c_int), 'plToken' )),
    COMMETHOD([], HRESULT, 'RegisterGroup',
              ( ['in'], WSTRING, 'pName' ),
              ( ['in'], c_int, 'cResource' ),
              ( ['in'], POINTER(c_int), 'palTokens' ),
              ( ['out'], POINTER(c_int), 'plToken' )),
    COMMETHOD([], HRESULT, 'RequestResource',
              ( ['in'], c_int, 'idResource' ),
              ( ['in'], POINTER(IUnknown), 'pFocusObject' ),
              ( ['in'], POINTER(IResourceConsumer), 'pConsumer' )),
    COMMETHOD([], HRESULT, 'NotifyAcquire',
              ( ['in'], c_int, 'idResource' ),
              ( ['in'], POINTER(IResourceConsumer), 'pConsumer' ),
              ( ['in'], HRESULT, 'hr' )),
    COMMETHOD([], HRESULT, 'NotifyRelease',
              ( ['in'], c_int, 'idResource' ),
              ( ['in'], POINTER(IResourceConsumer), 'pConsumer' ),
              ( ['in'], c_int, 'bStillWant' )),
    COMMETHOD([], HRESULT, 'CancelRequest',
              ( ['in'], c_int, 'idResource' ),
              ( ['in'], POINTER(IResourceConsumer), 'pConsumer' )),
    COMMETHOD([], HRESULT, 'SetFocus',
              ( ['in'], POINTER(IUnknown), 'pFocusObject' )),
    COMMETHOD([], HRESULT, 'ReleaseFocus',
              ( ['in'], POINTER(IUnknown), 'pFocusObject' )),
]

# values for enumeration 'tagAMTunerSignalStrength'
AMTUNER_HASNOSIGNALSTRENGTH = -1
AMTUNER_NOSIGNAL = 0
AMTUNER_SIGNALPRESENT = 1
tagAMTunerSignalStrength = c_int # enum
VMRRenderPrefs = __MIDL___MIDL_itf_DirectShow_0376_0001
tagVMRPRESENTATIONINFO._fields_ = [
    ('dwFlags', c_ulong),
    ('lpSurf', POINTER(c_ulong)),
    ('rtStart', c_longlong),
    ('rtEnd', c_longlong),
    ('szAspectRatio', tagSIZE),
    ('rcSrc', tagRECT),
    ('rcDst', tagRECT),
    ('dwTypeSpecificFlags', c_ulong),
    ('dwInterlaceFlags', c_ulong),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for tagVMRPRESENTATIONINFO is skipped.
__MIDL___MIDL_itf_DirectShow_0130_0001._fields_ = [
    ('clsid', GUID),
    ('Name', WSTRING),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_DirectShow_0130_0001 is skipped.

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0376_0002'
VMRMode_Windowed = 1
VMRMode_Windowless = 2
VMRMode_Renderless = 4
VMRMode_Mask = 7
__MIDL___MIDL_itf_DirectShow_0376_0002 = c_int # enum
class IAMVfwCaptureDialogs(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D8D715A0-6E5E-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []
IAMVfwCaptureDialogs._methods_ = [
    COMMETHOD([], HRESULT, 'HasDialog',
              ( ['in'], c_int, 'iDialog' )),
    COMMETHOD([], HRESULT, 'ShowDialog',
              ( ['in'], c_int, 'iDialog' ),
              ( ['in'], wireHWND, 'hwnd' )),
    COMMETHOD([], HRESULT, 'SendDriverMessage',
              ( ['in'], c_int, 'iDialog' ),
              ( ['in'], c_int, 'uMsg' ),
              ( ['in'], c_int, 'dw1' ),
              ( ['in'], c_int, 'dw2' )),
]

class IAMAudioInputMixer(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{54C39221-8380-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []
IAMAudioInputMixer._methods_ = [
    COMMETHOD([], HRESULT, 'put_Enable',
              ( ['in'], c_int, 'fEnable' )),
    COMMETHOD([], HRESULT, 'get_Enable',
              ( ['out'], POINTER(c_int), 'pfEnable' )),
    COMMETHOD([], HRESULT, 'put_Mono',
              ( ['in'], c_int, 'fMono' )),
    COMMETHOD([], HRESULT, 'get_Mono',
              ( ['out'], POINTER(c_int), 'pfMono' )),
    COMMETHOD([], HRESULT, 'put_MixLevel',
              ( ['in'], c_double, 'Level' )),
    COMMETHOD([], HRESULT, 'get_MixLevel',
              ( ['out'], POINTER(c_double), 'pLevel' )),
    COMMETHOD([], HRESULT, 'put_Pan',
              ( ['in'], c_double, 'Pan' )),
    COMMETHOD([], HRESULT, 'get_Pan',
              ( ['out'], POINTER(c_double), 'pPan' )),
    COMMETHOD([], HRESULT, 'put_Loudness',
              ( ['in'], c_int, 'fLoudness' )),
    COMMETHOD([], HRESULT, 'get_Loudness',
              ( ['out'], POINTER(c_int), 'pfLoudness' )),
    COMMETHOD([], HRESULT, 'put_Treble',
              ( ['in'], c_double, 'Treble' )),
    COMMETHOD([], HRESULT, 'get_Treble',
              ( ['out'], POINTER(c_double), 'pTreble' )),
    COMMETHOD([], HRESULT, 'get_TrebleRange',
              ( ['out'], POINTER(c_double), 'pRange' )),
    COMMETHOD([], HRESULT, 'put_Bass',
              ( ['in'], c_double, 'Bass' )),
    COMMETHOD([], HRESULT, 'get_Bass',
              ( ['out'], POINTER(c_double), 'pBass' )),
    COMMETHOD([], HRESULT, 'get_BassRange',
              ( ['out'], POINTER(c_double), 'pRange' )),
]

class IDistributorNotify(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868AF-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IDistributorNotify._methods_ = [
    COMMETHOD([], HRESULT, 'Stop'),
    COMMETHOD([], HRESULT, 'Pause'),
    COMMETHOD([], HRESULT, 'Run',
              ( [], c_longlong, 'tStart' )),
    COMMETHOD([], HRESULT, 'SetSyncSource',
              ( ['in'], POINTER(IReferenceClock), 'pClock' )),
    COMMETHOD([], HRESULT, 'NotifyGraphChange'),
]

class IAMTVAudio(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{83EC1C30-23D1-11D1-99E6-00A0C9560266}')
    _idlflags_ = []
IAMTVAudio._methods_ = [
    COMMETHOD([], HRESULT, 'GetHardwareSupportedTVAudioModes',
              ( ['out'], POINTER(c_int), 'plModes' )),
    COMMETHOD([], HRESULT, 'GetAvailableTVAudioModes',
              ( ['out'], POINTER(c_int), 'plModes' )),
    COMMETHOD([], HRESULT, 'get_TVAudioMode',
              ( ['out'], POINTER(c_int), 'plMode' )),
    COMMETHOD([], HRESULT, 'put_TVAudioMode',
              ( ['in'], c_int, 'lMode' )),
    COMMETHOD([], HRESULT, 'RegisterNotificationCallBack',
              ( ['in'], POINTER(IAMTunerNotification), 'pNotify' ),
              ( ['in'], c_int, 'lEvents' )),
    COMMETHOD([], HRESULT, 'UnRegisterNotificationCallBack',
              ( [], POINTER(IAMTunerNotification), 'pNotify' )),
]

IPersistMediaPropertyBag._methods_ = [
    COMMETHOD([], HRESULT, 'InitNew'),
    COMMETHOD([], HRESULT, 'Load',
              ( ['in'], POINTER(IMediaPropertyBag), 'pPropBag' ),
              ( ['in'], POINTER(IErrorLog), 'pErrorLog' )),
    COMMETHOD([], HRESULT, 'Save',
              ( ['in'], POINTER(IMediaPropertyBag), 'pPropBag' ),
              ( ['in'], c_int, 'fClearDirty' ),
              ( ['in'], c_int, 'fSaveAllProperties' )),
]

class IFilterMapper2(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B79BB0B0-33C1-11D1-ABE1-00A0C905F375}')
    _idlflags_ = []
class IFilterMapper3(IFilterMapper2):
    _case_insensitive_ = True
    _iid_ = GUID('{B79BB0B1-33C1-11D1-ABE1-00A0C905F375}')
    _idlflags_ = []
IFilterMapper2._methods_ = [
    COMMETHOD([], HRESULT, 'CreateCategory',
              ( ['in'], POINTER(GUID), 'clsidCategory' ),
              ( ['in'], c_ulong, 'dwCategoryMerit' ),
              ( ['in'], WSTRING, 'Description' )),
    COMMETHOD([], HRESULT, 'UnregisterFilter',
              ( ['in'], POINTER(GUID), 'pclsidCategory' ),
              ( ['in'], POINTER(c_ushort), 'szInstance' ),
              ( ['in'], POINTER(GUID), 'Filter' )),
    COMMETHOD([], HRESULT, 'RegisterFilter',
              ( ['in'], POINTER(GUID), 'clsidFilter' ),
              ( ['in'], WSTRING, 'Name' ),
              ( ['in', 'out'], POINTER(POINTER(IMoniker)), 'ppMoniker' ),
              ( ['in'], POINTER(GUID), 'pclsidCategory' ),
              ( ['in'], POINTER(c_ushort), 'szInstance' ),
              ( ['in'], POINTER(REGFILTER2), 'prf2' )),
    COMMETHOD([], HRESULT, 'EnumMatchingFilters',
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenum' ),
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], c_int, 'bExactMatch' ),
              ( ['in'], c_ulong, 'dwMerit' ),
              ( ['in'], c_int, 'bInputNeeded' ),
              ( ['in'], c_ulong, 'cInputTypes' ),
              ( [], POINTER(GUID), 'pInputTypes' ),
              ( ['in'], POINTER(REGPINMEDIUM), 'pMedIn' ),
              ( ['in'], POINTER(GUID), 'pPinCategoryIn' ),
              ( ['in'], c_int, 'bRender' ),
              ( ['in'], c_int, 'bOutputNeeded' ),
              ( ['in'], c_ulong, 'cOutputTypes' ),
              ( [], POINTER(GUID), 'pOutputTypes' ),
              ( ['in'], POINTER(REGPINMEDIUM), 'pMedOut' ),
              ( ['in'], POINTER(GUID), 'pPinCategoryOut' )),
]

IFilterMapper3._methods_ = [
    COMMETHOD([], HRESULT, 'GetICreateDevEnum',
              ( ['out'], POINTER(POINTER(ICreateDevEnum)), 'ppenum' )),
]

class __MIDL___MIDL_itf_DirectShow_0156_0002(Structure):
    pass
__MIDL___MIDL_itf_DirectShow_0156_0002._fields_ = [
    ('tStart', c_longlong),
    ('tStop', c_longlong),
    ('dwStartCookie', c_ulong),
    ('dwStopCookie', c_ulong),
    ('dwFlags', c_ulong),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_DirectShow_0156_0002 is skipped.
IAMCopyCaptureFileProgress._methods_ = [
    COMMETHOD([], HRESULT, 'Progress',
              ( ['in'], c_int, 'iProgress' )),
]

__MIDL___MIDL_itf_DirectShow_0355_0001._fields_ = [
    ('stream_id', c_ulong),
    ('dwMediaSampleContent', c_ulong),
    ('ulSubstreamFilterValue', c_ulong),
    ('iDataOffset', c_int),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_DirectShow_0355_0001 is skipped.
class IAMovieSetup(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{A3D8CEC0-7E5A-11CF-BBC5-00805F6CEF20}')
    _idlflags_ = []
IAMovieSetup._methods_ = [
    COMMETHOD([], HRESULT, 'Register'),
    COMMETHOD([], HRESULT, 'Unregister'),
]

class IAMPushSource(IAMLatency):
    _case_insensitive_ = True
    _iid_ = GUID('{F185FE76-E64E-11D2-B76E-00C04FB6BD3D}')
    _idlflags_ = []
IAMPushSource._methods_ = [
    COMMETHOD([], HRESULT, 'GetPushSourceFlags',
              ( ['out'], POINTER(c_ulong), 'pFlags' )),
    COMMETHOD([], HRESULT, 'SetPushSourceFlags',
              ( ['in'], c_ulong, 'Flags' )),
    COMMETHOD([], HRESULT, 'SetStreamOffset',
              ( ['in'], c_longlong, 'rtOffset' )),
    COMMETHOD([], HRESULT, 'GetStreamOffset',
              ( ['out'], POINTER(c_longlong), 'prtOffset' )),
    COMMETHOD([], HRESULT, 'GetMaxStreamOffset',
              ( ['out'], POINTER(c_longlong), 'prtMaxOffset' )),
    COMMETHOD([], HRESULT, 'SetMaxStreamOffset',
              ( ['in'], c_longlong, 'rtMaxOffset' )),
]

AM_STREAM_INFO = __MIDL___MIDL_itf_DirectShow_0156_0002

# values for enumeration '_AM_FILTER_MISC_FLAGS'
AM_FILTER_MISC_FLAGS_IS_RENDERER = 1
AM_FILTER_MISC_FLAGS_IS_SOURCE = 2
_AM_FILTER_MISC_FLAGS = c_int # enum
class IAMBufferNegotiation(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56ED71A0-AF5F-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []
IAMBufferNegotiation._methods_ = [
    COMMETHOD([], HRESULT, 'SuggestAllocatorProperties',
              ( ['in'], POINTER(_AllocatorProperties), 'pprop' )),
    COMMETHOD([], HRESULT, 'GetAllocatorProperties',
              ( ['out'], POINTER(_AllocatorProperties), 'pprop' )),
]

class IAMTimecodeDisplay(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{9B496CE2-811B-11CF-8C77-00AA006B6814}')
    _idlflags_ = []
IAMTimecodeDisplay._methods_ = [
    COMMETHOD([], HRESULT, 'GetTCDisplayEnable',
              ( ['out'], POINTER(c_int), 'pState' )),
    COMMETHOD([], HRESULT, 'SetTCDisplayEnable',
              ( ['in'], c_int, 'State' )),
    COMMETHOD([], HRESULT, 'GetTCDisplay',
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetTCDisplay',
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' )),
]

class IDecimateVideoImage(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2E5EA3E0-E924-11D2-B6DA-00A0C995E8DF}')
    _idlflags_ = []
IDecimateVideoImage._methods_ = [
    COMMETHOD([], HRESULT, 'SetDecimationImageSize',
              ( ['in'], c_int, 'lWidth' ),
              ( ['in'], c_int, 'lHeight' )),
    COMMETHOD([], HRESULT, 'ResetDecimationImageSize'),
]

class IAMAnalogVideoEncoder(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E133B0-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMAnalogVideoEncoder._methods_ = [
    COMMETHOD([], HRESULT, 'get_AvailableTVFormats',
              ( ['out'], POINTER(c_int), 'lAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'put_TVFormat',
              ( ['in'], c_int, 'lAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'get_TVFormat',
              ( ['out'], POINTER(c_int), 'plAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'put_CopyProtection',
              ( ['in'], c_int, 'lVideoCopyProtection' )),
    COMMETHOD([], HRESULT, 'get_CopyProtection',
              ( ['out'], POINTER(c_int), 'lVideoCopyProtection' )),
    COMMETHOD([], HRESULT, 'put_CCEnable',
              ( ['in'], c_int, 'lCCEnable' )),
    COMMETHOD([], HRESULT, 'get_CCEnable',
              ( ['out'], POINTER(c_int), 'lCCEnable' )),
]

# values for enumeration 'tagCameraControlProperty'
CameraControl_Pan = 0
CameraControl_Tilt = 1
CameraControl_Roll = 2
CameraControl_Zoom = 3
CameraControl_Exposure = 4
CameraControl_Iris = 5
CameraControl_Focus = 6
tagCameraControlProperty = c_int # enum
class IBPCSatelliteTuner(IAMTuner):
    _case_insensitive_ = True
    _iid_ = GUID('{211A8765-03AC-11D1-8D13-00AA00BD8339}')
    _idlflags_ = []
IBPCSatelliteTuner._methods_ = [
    COMMETHOD([], HRESULT, 'get_DefaultSubChannelTypes',
              ( ['out'], POINTER(c_int), 'plDefaultVideoType' ),
              ( ['out'], POINTER(c_int), 'plDefaultAudioType' )),
    COMMETHOD([], HRESULT, 'put_DefaultSubChannelTypes',
              ( ['in'], c_int, 'lDefaultVideoType' ),
              ( ['in'], c_int, 'lDefaultAudioType' )),
    COMMETHOD([], HRESULT, 'IsTapingPermitted'),
]

class IGetCapabilitiesKey(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{A8809222-07BB-48EA-951C-33158100625B}')
    _idlflags_ = []
IGetCapabilitiesKey._methods_ = [
    COMMETHOD([], HRESULT, 'GetCapabilitiesKey',
              ( ['out'], POINTER(c_void_p), 'pHKey' )),
]

class tagSTATSTG(Structure):
    pass
IStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteSeek',
              ( ['in'], _LARGE_INTEGER, 'dlibMove' ),
              ( ['in'], c_ulong, 'dwOrigin' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'plibNewPosition' )),
    COMMETHOD([], HRESULT, 'SetSize',
              ( ['in'], _ULARGE_INTEGER, 'libNewSize' )),
    COMMETHOD([], HRESULT, 'RemoteCopyTo',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbRead' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbWritten' )),
    COMMETHOD([], HRESULT, 'Commit',
              ( ['in'], c_ulong, 'grfCommitFlags' )),
    COMMETHOD([], HRESULT, 'Revert'),
    COMMETHOD([], HRESULT, 'LockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'UnlockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'Stat',
              ( ['out'], POINTER(tagSTATSTG), 'pstatstg' ),
              ( ['in'], c_ulong, 'grfStatFlag' )),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
]

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0378_0001'
DeinterlacePref_NextBest = 1
DeinterlacePref_BOB = 2
DeinterlacePref_Weave = 4
DeinterlacePref_Mask = 7
__MIDL___MIDL_itf_DirectShow_0378_0001 = c_int # enum
class IAMFilterMiscFlags(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2DD74950-A890-11D1-ABE8-00A0C905F375}')
    _idlflags_ = []
IAMFilterMiscFlags._methods_ = [
    COMMETHOD([], c_ulong, 'GetMiscFlags'),
]

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0134_0004'
REG_PINFLAG_B_ZERO = 1
REG_PINFLAG_B_RENDERER = 2
REG_PINFLAG_B_MANY = 4
REG_PINFLAG_B_OUTPUT = 8
__MIDL___MIDL_itf_DirectShow_0134_0004 = c_int # enum
class IAMGraphStreams(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{632105FA-072E-11D3-8AF9-00C04FB6BD3D}')
    _idlflags_ = []
IAMGraphStreams._methods_ = [
    COMMETHOD([], HRESULT, 'FindUpstreamInterface',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppvInterface' ),
              ( ['in'], c_ulong, 'dwFlags' )),
    COMMETHOD([], HRESULT, 'SyncUsingStreamOffset',
              ( ['in'], c_int, 'bUseStreamOffset' )),
    COMMETHOD([], HRESULT, 'SetMaxGraphLatency',
              ( ['in'], c_longlong, 'rtMaxGraphLatency' )),
]

VMRMode = __MIDL___MIDL_itf_DirectShow_0376_0002
class IAMAudioRendererStats(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{22320CB2-D41A-11D2-BF7C-D7CB9DF0BF93}')
    _idlflags_ = []
IAMAudioRendererStats._methods_ = [
    COMMETHOD([], HRESULT, 'GetStatParam',
              ( ['in'], c_ulong, 'dwParam' ),
              ( ['out'], POINTER(c_ulong), 'pdwParam1' ),
              ( ['out'], POINTER(c_ulong), 'pdwParam2' )),
]

class AsyncFileReader(CoClass):
    'http://msdn.microsoft.com/library/default.asp?url=/library/en-us/directshow/htm/filesourceasyncfilter.asp'
    _reg_clsid_ = GUID('{E436EBB5-524F-11CE-9F53-0020AF0BA770}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
AsyncFileReader._com_interfaces_ = [IFileSourceFilter, IBaseFilter]

class IEnumPins(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86892-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

class _FilterInfo(Structure):
    pass
IBaseFilter._methods_ = [
    COMMETHOD([], HRESULT, 'EnumPins',
              ( ['out', 'retval'], POINTER(POINTER(IEnumPins)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'FindPin',
              ( ['in'], WSTRING, 'Id' ),
              ( ['out', 'retval'], POINTER(POINTER(IPin)), 'ppPin' )),
    COMMETHOD([], HRESULT, 'QueryFilterInfo',
              ( ['out', 'retval'], POINTER(_FilterInfo), 'pInfo' )),
    COMMETHOD([], HRESULT, 'JoinFilterGraph',
              ( ['in'], POINTER(IFilterGraph), 'pGraph' ),
              ( ['in'], WSTRING, 'pName' )),
    COMMETHOD([], HRESULT, 'QueryVendorInfo',
              ( ['out', 'retval'], POINTER(WSTRING), 'pVendorInfo' )),
]

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0378_0002'
DeinterlaceTech_Unknown = 0
DeinterlaceTech_BOBLineReplicate = 1
DeinterlaceTech_BOBVerticalStretch = 2
DeinterlaceTech_MedianFiltering = 4
DeinterlaceTech_EdgeFiltering = 16
DeinterlaceTech_FieldAdaptive = 32
DeinterlaceTech_PixelAdaptive = 64
DeinterlaceTech_MotionVectorSteered = 128
__MIDL___MIDL_itf_DirectShow_0378_0002 = c_int # enum
VMRDeinterlaceTech = __MIDL___MIDL_itf_DirectShow_0378_0002
_VMRDeinterlaceCaps._fields_ = [
    ('dwSize', c_ulong),
    ('dwNumPreviousOutputFrames', c_ulong),
    ('dwNumForwardRefSamples', c_ulong),
    ('dwNumBackwardRefSamples', c_ulong),
    ('DeinterlaceTechnology', VMRDeinterlaceTech),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for _VMRDeinterlaceCaps is skipped.
class IAMVideoControl(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{6A2E0670-28E4-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMVideoControl._methods_ = [
    COMMETHOD([], HRESULT, 'GetCaps',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['out'], POINTER(c_int), 'pCapsFlags' )),
    COMMETHOD([], HRESULT, 'SetMode',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['in'], c_int, 'mode' )),
    COMMETHOD([], HRESULT, 'GetMode',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['out'], POINTER(c_int), 'mode' )),
    COMMETHOD([], HRESULT, 'GetCurrentActualFrameRate',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['out'], POINTER(c_longlong), 'ActualFrameRate' )),
    COMMETHOD([], HRESULT, 'GetMaxAvailableFrameRate',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['in'], c_int, 'iIndex' ),
              ( ['in'], tagSIZE, 'Dimensions' ),
              ( ['out'], POINTER(c_longlong), 'MaxAvailableFrameRate' )),
    COMMETHOD([], HRESULT, 'GetFrameRateList',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['in'], c_int, 'iIndex' ),
              ( ['in'], tagSIZE, 'Dimensions' ),
              ( ['out'], POINTER(c_int), 'ListSize' ),
              ( ['out'], POINTER(POINTER(c_longlong)), 'FrameRates' )),
]

VMRDeinterlacePrefs = __MIDL___MIDL_itf_DirectShow_0378_0001
tagSTATSTG._fields_ = [
    ('pwcsName', WSTRING),
    ('type', c_ulong),
    ('cbSize', _ULARGE_INTEGER),
    ('mtime', _FILETIME),
    ('ctime', _FILETIME),
    ('atime', _FILETIME),
    ('grfMode', c_ulong),
    ('grfLocksSupported', c_ulong),
    ('clsid', GUID),
    ('grfStateBits', c_ulong),
    ('reserved', c_ulong),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for tagSTATSTG is skipped.
IEnumString._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(WSTRING), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumString)), 'ppenum' )),
]

IMemAllocatorNotifyCallbackTemp._methods_ = [
    COMMETHOD([], HRESULT, 'NotifyRelease'),
]

class IAMStreamControl(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{36B73881-C2C8-11CF-8B46-00805F6CEF60}')
    _idlflags_ = []
IAMStreamControl._methods_ = [
    COMMETHOD([], HRESULT, 'StartAt',
              ( ['in'], POINTER(c_longlong), 'ptStart' ),
              ( ['in'], c_ulong, 'dwCookie' )),
    COMMETHOD([], HRESULT, 'StopAt',
              ( ['in'], POINTER(c_longlong), 'ptStop' ),
              ( ['in'], c_int, 'bSendExtra' ),
              ( ['in'], c_ulong, 'dwCookie' )),
    COMMETHOD([], HRESULT, 'GetInfo',
              ( ['out'], POINTER(AM_STREAM_INFO), 'pInfo' )),
]

class IMpeg2Demultiplexer(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{436EEE9C-264F-4242-90E1-4E330C107512}')
    _idlflags_ = []
IMpeg2Demultiplexer._methods_ = [
    COMMETHOD([], HRESULT, 'CreateOutputPin',
              ( ['in'], POINTER(_AMMediaType), 'pMediaType' ),
              ( ['in'], WSTRING, 'pszPinName' ),
              ( ['out'], POINTER(POINTER(IPin)), 'ppIPin' )),
    COMMETHOD([], HRESULT, 'SetOutputPinMediaType',
              ( ['in'], WSTRING, 'pszPinName' ),
              ( ['in'], POINTER(_AMMediaType), 'pMediaType' )),
    COMMETHOD([], HRESULT, 'DeleteOutputPin',
              ( ['in'], WSTRING, 'pszPinName' )),
]

IDVSplitter._methods_ = [
    COMMETHOD([], HRESULT, 'DiscardAlternateVideoFrames',
              ( ['in'], c_int, 'nDiscard' )),
]

class IVMRImagePresenterConfig(IUnknown):
    _case_insensitive_ = True
    'IVMRImagePresenterConfig Interface'
    _iid_ = GUID('{9F3A1C85-8555-49BA-935F-BE5B5B29D178}')
    _idlflags_ = []
class IVMRImagePresenterExclModeConfig(IVMRImagePresenterConfig):
    _case_insensitive_ = True
    'IVMRImagePresenterExclModeConfig Interface'
    _iid_ = GUID('{E6F7CE40-4673-44F1-8F77-5499D68CB4EA}')
    _idlflags_ = []
IVMRImagePresenterConfig._methods_ = [
    COMMETHOD([], HRESULT, 'SetRenderingPrefs',
              ( ['in'], c_ulong, 'dwRenderFlags' )),
    COMMETHOD([], HRESULT, 'GetRenderingPrefs',
              ( ['out'], POINTER(c_ulong), 'dwRenderFlags' )),
]

IVMRImagePresenterExclModeConfig._methods_ = [
    COMMETHOD([], HRESULT, 'SetXlcModeDDObjAndPrimarySurface',
              ( ['in'], POINTER(c_ulong), 'lpDDObj' ),
              ( ['in'], POINTER(c_ulong), 'lpPrimarySurf' )),
    COMMETHOD([], HRESULT, 'GetXlcModeDDObjAndPrimarySurface',
              ( ['out'], POINTER(POINTER(c_ulong)), 'lpDDObj' ),
              ( ['out'], POINTER(POINTER(c_ulong)), 'lpPrimarySurf' )),
]

IEnumFilters._methods_ = [
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'cFilters' ),
              ( ['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'cFilters' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumFilters)), 'ppenum' )),
]

class IMemInputPin(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A8689D-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IMemInputPin._methods_ = [
    COMMETHOD([], HRESULT, 'GetAllocator',
              ( ['out'], POINTER(POINTER(IMemAllocator)), 'ppAllocator' )),
    COMMETHOD([], HRESULT, 'NotifyAllocator',
              ( ['in'], POINTER(IMemAllocator), 'pAllocator' ),
              ( ['in'], c_int, 'bReadOnly' )),
    COMMETHOD([], HRESULT, 'GetAllocatorRequirements',
              ( ['out'], POINTER(_AllocatorProperties), 'pProps' )),
    COMMETHOD([], HRESULT, 'Receive',
              ( ['in'], POINTER(IMediaSample), 'pSample' )),
    COMMETHOD([], HRESULT, 'ReceiveMultiple',
              ( ['in'], POINTER(POINTER(IMediaSample)), 'pSamples' ),
              ( ['in'], c_int, 'nSamples' ),
              ( ['out'], POINTER(c_int), 'nSamplesProcessed' )),
    COMMETHOD([], HRESULT, 'ReceiveCanBlock'),
]

# values for enumeration 'AM_SEEKING_SeekingCapabilities'
AM_SEEKING_CanSeekAbsolute = 1
AM_SEEKING_CanSeekForwards = 2
AM_SEEKING_CanSeekBackwards = 4
AM_SEEKING_CanGetCurrentPos = 8
AM_SEEKING_CanGetStopPos = 16
AM_SEEKING_CanGetDuration = 32
AM_SEEKING_CanPlayBackwards = 64
AM_SEEKING_CanDoSegments = 128
AM_SEEKING_Source = 256
AM_SEEKING_SeekingCapabilities = c_int # enum
class IAMDevMemoryAllocator(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6545BF0-E76B-11D0-BD52-00A0C911CE86}')
    _idlflags_ = []
IAMDevMemoryAllocator._methods_ = [
    COMMETHOD([], HRESULT, 'GetInfo',
              ( ['out'], POINTER(c_ulong), 'pdwcbTotalFree' ),
              ( ['out'], POINTER(c_ulong), 'pdwcbLargestFree' ),
              ( ['out'], POINTER(c_ulong), 'pdwcbTotalMemory' ),
              ( ['out'], POINTER(c_ulong), 'pdwcbMinimumChunk' )),
    COMMETHOD([], HRESULT, 'CheckMemory',
              ( ['in'], POINTER(c_ubyte), 'pBuffer' )),
    COMMETHOD([], HRESULT, 'Alloc',
              ( ['out'], POINTER(POINTER(c_ubyte)), 'ppBuffer' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pdwcbBuffer' )),
    COMMETHOD([], HRESULT, 'Free',
              ( ['in'], POINTER(c_ubyte), 'pBuffer' )),
    COMMETHOD([], HRESULT, 'GetDevMemoryObject',
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppUnkInnner' ),
              ( ['in'], POINTER(IUnknown), 'pUnkOuter' )),
]

class IAMExtDevice(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B5730A90-1A2C-11CF-8C23-00AA006B6814}')
    _idlflags_ = []
IAMExtDevice._methods_ = [
    COMMETHOD([], HRESULT, 'GetCapability',
              ( ['in'], c_int, 'Capability' ),
              ( ['out'], POINTER(c_int), 'pValue' ),
              ( ['out'], POINTER(c_double), 'pdblValue' )),
    COMMETHOD([], HRESULT, 'get_ExternalDeviceID',
              ( ['out'], POINTER(WSTRING), 'ppszData' )),
    COMMETHOD([], HRESULT, 'get_ExternalDeviceVersion',
              ( ['out'], POINTER(WSTRING), 'ppszData' )),
    COMMETHOD([], HRESULT, 'put_DevicePower',
              ( ['in'], c_int, 'PowerMode' )),
    COMMETHOD([], HRESULT, 'get_DevicePower',
              ( ['out'], POINTER(c_int), 'pPowerMode' )),
    COMMETHOD([], HRESULT, 'Calibrate',
              ( ['in'], ULONG_PTR, 'hEvent' ),
              ( ['in'], c_int, 'mode' ),
              ( ['out'], POINTER(c_int), 'pStatus' )),
    COMMETHOD([], HRESULT, 'put_DevicePort',
              ( ['in'], c_int, 'DevicePort' )),
    COMMETHOD([], HRESULT, 'get_DevicePort',
              ( ['out'], POINTER(c_int), 'pDevicePort' )),
]

class IConfigInterleaving(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{BEE3D220-157B-11D0-BD23-00A0C911CE86}')
    _idlflags_ = []
IConfigInterleaving._methods_ = [
    COMMETHOD([], HRESULT, 'put_Mode',
              ( ['in'], InterleavingMode, 'mode' )),
    COMMETHOD([], HRESULT, 'get_Mode',
              ( ['out'], POINTER(InterleavingMode), 'pMode' )),
    COMMETHOD([], HRESULT, 'put_Interleaving',
              ( ['in'], POINTER(c_longlong), 'prtInterleave' ),
              ( ['in'], POINTER(c_longlong), 'prtPreroll' )),
    COMMETHOD([], HRESULT, 'get_Interleaving',
              ( ['out'], POINTER(c_longlong), 'prtInterleave' ),
              ( ['out'], POINTER(c_longlong), 'prtPreroll' )),
]

IResourceConsumer._methods_ = [
    COMMETHOD([], HRESULT, 'AcquireResource',
              ( ['in'], c_int, 'idResource' )),
    COMMETHOD([], HRESULT, 'ReleaseResource',
              ( ['in'], c_int, 'idResource' )),
]

# values for enumeration 'tagCameraControlFlags'
CameraControl_Flags_Auto = 1
CameraControl_Flags_Manual = 2
tagCameraControlFlags = c_int # enum

# values for enumeration '_AMSTREAMSELECTENABLEFLAGS'
AMSTREAMSELECTENABLE_ENABLE = 1
AMSTREAMSELECTENABLE_ENABLEALL = 2
_AMSTREAMSELECTENABLEFLAGS = c_int # enum
class IReferenceClock2(IReferenceClock):
    _case_insensitive_ = True
    _iid_ = GUID('{36B73885-C2C8-11CF-8B46-00805F6CEF60}')
    _idlflags_ = []
IReferenceClock2._methods_ = [
]

# values for enumeration '_AM_RENSDEREXFLAGS'
AM_RENDEREX_RENDERTOEXISTINGRENDERERS = 1
_AM_RENSDEREXFLAGS = c_int # enum
class IAMDroppedFrames(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13344-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMDroppedFrames._methods_ = [
    COMMETHOD([], HRESULT, 'GetNumDropped',
              ( ['out'], POINTER(c_int), 'plDropped' )),
    COMMETHOD([], HRESULT, 'GetNumNotDropped',
              ( ['out'], POINTER(c_int), 'plNotDropped' )),
    COMMETHOD([], HRESULT, 'GetDroppedInfo',
              ( ['in'], c_int, 'lSize' ),
              ( ['out'], POINTER(c_int), 'plArray' ),
              ( ['out'], POINTER(c_int), 'plNumCopied' )),
    COMMETHOD([], HRESULT, 'GetAverageFrameSize',
              ( ['out'], POINTER(c_int), 'plAverageSize' )),
]

IEnumMoniker._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenum' )),
]

AM_FILESINK_FLAGS = __MIDL___MIDL_itf_DirectShow_0145_0001

# values for enumeration '_DVENCODERRESOLUTION'
DVENCODERRESOLUTION_720x480 = 2012
DVENCODERRESOLUTION_360x240 = 2013
DVENCODERRESOLUTION_180x120 = 2014
DVENCODERRESOLUTION_88x60 = 2015
_DVENCODERRESOLUTION = c_int # enum

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0364_0001'
ConstantBitRate = 0
VariableBitRateAverage = 1
VariableBitRatePeak = 2
__MIDL___MIDL_itf_DirectShow_0364_0001 = c_int # enum
class IAMVideoDecimationProperties(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{60D32930-13DA-11D3-9EC6-C4FCAEF5C7BE}')
    _idlflags_ = []
IAMVideoDecimationProperties._methods_ = [
    COMMETHOD([], HRESULT, 'QueryDecimationUsage',
              ( ['out'], POINTER(_DECIMATION_USAGE), 'lpUsage' )),
    COMMETHOD([], HRESULT, 'SetDecimationUsage',
              ( ['in'], _DECIMATION_USAGE, 'Usage' )),
]

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0138_0002'
ADVISE_NONE = 0
ADVISE_CLIPPING = 1
ADVISE_PALETTE = 2
ADVISE_COLORKEY = 4
ADVISE_POSITION = 8
ADVISE_DISPLAY_CHANGE = 16
__MIDL___MIDL_itf_DirectShow_0138_0002 = c_int # enum
VIDEOENCODER_BITRATE_MODE = __MIDL___MIDL_itf_DirectShow_0364_0001
IEnumPins._methods_ = [
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'cPins' ),
              ( ['out'], POINTER(POINTER(IPin)), 'ppPins' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'cPins' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out', 'retval'], POINTER(POINTER(IEnumPins)), 'ppenum' )),
]

class IVideoFrameStep(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{E46A9787-2B71-444D-A4B5-1FAB7B708D6A}')
    _idlflags_ = []
IVideoFrameStep._methods_ = [
    COMMETHOD([], HRESULT, 'Step',
              ( [], c_ulong, 'dwFrames' ),
              ( [], POINTER(IUnknown), 'pStepObject' )),
    COMMETHOD([], HRESULT, 'CanStep',
              ( [], c_int, 'bMultiple' ),
              ( [], POINTER(IUnknown), 'pStepObject' )),
    COMMETHOD([], HRESULT, 'CancelStep'),
]

ICaptureGraphBuilder2._methods_ = [
    COMMETHOD([], HRESULT, 'SetFiltergraph',
              ( ['in'], POINTER(IGraphBuilder), 'pfg' )),
    COMMETHOD([], HRESULT, 'GetFiltergraph',
              ( ['out', 'retval'], POINTER(POINTER(IGraphBuilder)), 'ppfg' )),
    COMMETHOD([], HRESULT, 'SetOutputFileName',
              ( ['in'], POINTER(GUID), 'pType' ),
              ( ['in'], WSTRING, 'lpstrFile' ),
              ( ['out'], POINTER(POINTER(IBaseFilter)), 'ppf' ),
              ( ['out'], POINTER(POINTER(IFileSinkFilter)), 'ppSink' )),
    COMMETHOD([], HRESULT, 'RemoteFindInterface',
              ( ['in'], POINTER(GUID), 'pCategory' ),
              ( ['in'], POINTER(GUID), 'pType' ),
              ( ['in'], POINTER(IBaseFilter), 'pf' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppint' )),
    COMMETHOD([], HRESULT, 'RenderStream',
              ( ['in'], POINTER(GUID), 'pCategory' ),
              ( ['in'], POINTER(GUID), 'pType' ),
              ( ['in'], POINTER(IUnknown), 'pSource' ),
              ( ['in'], POINTER(IBaseFilter), 'pfCompressor' ),
              ( ['in'], POINTER(IBaseFilter), 'pfRenderer' )),
    COMMETHOD([], HRESULT, 'ControlStream',
              ( ['in'], POINTER(GUID), 'pCategory' ),
              ( ['in'], POINTER(GUID), 'pType' ),
              ( ['in'], POINTER(IBaseFilter), 'pFilter' ),
              ( ['in'], POINTER(c_longlong), 'pstart' ),
              ( ['in'], POINTER(c_longlong), 'pStop' ),
              ( ['in'], c_ushort, 'wStartCookie' ),
              ( ['in'], c_ushort, 'wStopCookie' )),
    COMMETHOD([], HRESULT, 'AllocCapFile',
              ( ['in'], WSTRING, 'lpstr' ),
              ( ['in'], c_ulonglong, 'dwlSize' )),
    COMMETHOD([], HRESULT, 'CopyCaptureFile',
              ( ['in'], WSTRING, 'lpwstrOld' ),
              ( ['in'], WSTRING, 'lpwstrNew' ),
              ( ['in'], c_int, 'fAllowEscAbort' ),
              ( ['in'], POINTER(IAMCopyCaptureFileProgress), 'pCallback' )),
    COMMETHOD([], HRESULT, 'FindPin',
              ( ['in'], POINTER(IUnknown), 'pSource' ),
              ( ['in'], _PinDirection, 'pindir' ),
              ( ['in'], POINTER(GUID), 'pCategory' ),
              ( ['in'], POINTER(GUID), 'pType' ),
              ( ['in'], c_int, 'fUnconnected' ),
              ( ['in'], c_int, 'num' ),
              ( ['out'], POINTER(POINTER(IPin)), 'ppPin' )),
]

class IAMExtTransport(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{A03CD5F0-3045-11CF-8C44-00AA006B6814}')
    _idlflags_ = []
IAMExtTransport._methods_ = [
    COMMETHOD([], HRESULT, 'GetCapability',
              ( ['in'], c_int, 'Capability' ),
              ( ['out'], POINTER(c_int), 'pValue' ),
              ( ['out'], POINTER(c_double), 'pdblValue' )),
    COMMETHOD([], HRESULT, 'put_MediaState',
              ( ['in'], c_int, 'State' )),
    COMMETHOD([], HRESULT, 'get_MediaState',
              ( ['out'], POINTER(c_int), 'pState' )),
    COMMETHOD([], HRESULT, 'put_LocalControl',
              ( ['in'], c_int, 'State' )),
    COMMETHOD([], HRESULT, 'get_LocalControl',
              ( ['out'], POINTER(c_int), 'pState' )),
    COMMETHOD([], HRESULT, 'GetStatus',
              ( ['in'], c_int, 'StatusItem' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'GetTransportBasicParameters',
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' ),
              ( ['out'], POINTER(WSTRING), 'ppszData' )),
    COMMETHOD([], HRESULT, 'SetTransportBasicParameters',
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' ),
              ( ['in'], WSTRING, 'pszData' )),
    COMMETHOD([], HRESULT, 'GetTransportVideoParameters',
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetTransportVideoParameters',
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([], HRESULT, 'GetTransportAudioParameters',
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetTransportAudioParameters',
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([], HRESULT, 'put_Mode',
              ( ['in'], c_int, 'mode' )),
    COMMETHOD([], HRESULT, 'get_Mode',
              ( ['out'], POINTER(c_int), 'pMode' )),
    COMMETHOD([], HRESULT, 'put_Rate',
              ( ['in'], c_double, 'dblRate' )),
    COMMETHOD([], HRESULT, 'get_Rate',
              ( ['out'], POINTER(c_double), 'pdblRate' )),
    COMMETHOD([], HRESULT, 'GetChase',
              ( ['out'], POINTER(c_int), 'pEnabled' ),
              ( ['out'], POINTER(c_int), 'pOffset' ),
              ( ['out'], POINTER(ULONG_PTR), 'phEvent' )),
    COMMETHOD([], HRESULT, 'SetChase',
              ( ['in'], c_int, 'Enable' ),
              ( ['in'], c_int, 'Offset' ),
              ( ['in'], ULONG_PTR, 'hEvent' )),
    COMMETHOD([], HRESULT, 'GetBump',
              ( ['out'], POINTER(c_int), 'pSpeed' ),
              ( ['out'], POINTER(c_int), 'pDuration' )),
    COMMETHOD([], HRESULT, 'SetBump',
              ( ['in'], c_int, 'Speed' ),
              ( ['in'], c_int, 'Duration' )),
    COMMETHOD([], HRESULT, 'get_AntiClogControl',
              ( ['out'], POINTER(c_int), 'pEnabled' )),
    COMMETHOD([], HRESULT, 'put_AntiClogControl',
              ( ['in'], c_int, 'Enable' )),
    COMMETHOD([], HRESULT, 'GetEditPropertySet',
              ( ['in'], c_int, 'EditID' ),
              ( ['out'], POINTER(c_int), 'pState' )),
    COMMETHOD([], HRESULT, 'SetEditPropertySet',
              ( ['in', 'out'], POINTER(c_int), 'pEditID' ),
              ( ['in'], c_int, 'State' )),
    COMMETHOD([], HRESULT, 'GetEditProperty',
              ( ['in'], c_int, 'EditID' ),
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetEditProperty',
              ( ['in'], c_int, 'EditID' ),
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([], HRESULT, 'get_EditStart',
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'put_EditStart',
              ( ['in'], c_int, 'Value' )),
]

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0138_0001'
CK_NOCOLORKEY = 0
CK_INDEX = 1
CK_RGB = 2
__MIDL___MIDL_itf_DirectShow_0138_0001 = c_int # enum

# values for enumeration 'tagVideoControlFlags'
VideoControlFlag_FlipHorizontal = 1
VideoControlFlag_FlipVertical = 2
VideoControlFlag_ExternalTriggerEnable = 4
VideoControlFlag_Trigger = 8
tagVideoControlFlags = c_int # enum
_FilterInfo._fields_ = [
    ('achName', c_ushort * 128),
    ('pGraph', POINTER(IFilterGraph)),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for _FilterInfo is skipped.
class IStreamBuilder(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868BF-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IStreamBuilder._methods_ = [
    COMMETHOD([], HRESULT, 'Render',
              ( ['in'], POINTER(IPin), 'ppinOut' ),
              ( ['in'], POINTER(IGraphBuilder), 'pGraph' )),
    COMMETHOD([], HRESULT, 'Backout',
              ( ['in'], POINTER(IPin), 'ppinOut' ),
              ( ['in'], POINTER(IGraphBuilder), 'pGraph' )),
]

__MIDL___MIDL_itf_DirectShow_0345_0001._fields_ = [
    ('dwDVAAuxSrc', c_ulong),
    ('dwDVAAuxCtl', c_ulong),
    ('dwDVAAuxSrc1', c_ulong),
    ('dwDVAAuxCtl1', c_ulong),
    ('dwDVVAuxSrc', c_ulong),
    ('dwDVVAuxCtl', c_ulong),
    ('dwDVReserved', c_ulong * 2),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_DirectShow_0345_0001 is skipped.

# values for enumeration 'tagTVAudioMode'
AMTVAUDIO_MODE_MONO = 1
AMTVAUDIO_MODE_STEREO = 2
AMTVAUDIO_MODE_LANG_A = 16
AMTVAUDIO_MODE_LANG_B = 32
AMTVAUDIO_MODE_LANG_C = 64
tagTVAudioMode = c_int # enum

# values for enumeration '_AM_PUSHSOURCE_FLAGS'
AM_PUSHSOURCECAPS_INTERNAL_RM = 1
AM_PUSHSOURCECAPS_NOT_LIVE = 2
AM_PUSHSOURCECAPS_PRIVATE_CLOCK = 4
AM_PUSHSOURCEREQS_USE_STREAM_CLOCK = 65536
_AM_PUSHSOURCE_FLAGS = c_int # enum

# values for enumeration 'tagAMTVAudioEventType'
AMTVAUDIO_EVENT_CHANGED = 1
tagAMTVAudioEventType = c_int # enum

# values for enumeration '_AMSTREAMSELECTINFOFLAGS'
AMSTREAMSELECTINFO_ENABLED = 1
AMSTREAMSELECTINFO_EXCLUSIVE = 2
_AMSTREAMSELECTINFOFLAGS = c_int # enum
class IVMRMixerControl(IUnknown):
    _case_insensitive_ = True
    'IVMRMixerControl Interface'
    _iid_ = GUID('{1C1A17B0-BED0-415D-974B-DC6696131599}')
    _idlflags_ = []
IVMRMixerControl._methods_ = [
    COMMETHOD([], HRESULT, 'SetAlpha',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['in'], c_float, 'Alpha' )),
    COMMETHOD([], HRESULT, 'GetAlpha',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['out'], POINTER(c_float), 'pAlpha' )),
    COMMETHOD([], HRESULT, 'SetZOrder',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['in'], c_ulong, 'dwZ' )),
    COMMETHOD([], HRESULT, 'GetZOrder',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['out'], POINTER(c_ulong), 'pZ' )),
    COMMETHOD([], HRESULT, 'SetOutputRect',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['in'], POINTER(_NORMALIZEDRECT), 'pRect' )),
    COMMETHOD([], HRESULT, 'GetOutputRect',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['out'], POINTER(_NORMALIZEDRECT), 'pRect' )),
    COMMETHOD([], HRESULT, 'SetBackgroundClr',
              ( ['in'], c_ulong, 'ClrBkg' )),
    COMMETHOD([], HRESULT, 'GetBackgroundClr',
              ( ['in'], POINTER(c_ulong), 'lpClrBkg' )),
    COMMETHOD([], HRESULT, 'SetMixingPrefs',
              ( ['in'], c_ulong, 'dwMixerPrefs' )),
    COMMETHOD([], HRESULT, 'GetMixingPrefs',
              ( ['out'], POINTER(c_ulong), 'pdwMixerPrefs' )),
]

IEnumMediaTypes._methods_ = [
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'cMediaTypes' ),
              ( ['out'], POINTER(POINTER(_AMMediaType)), 'ppMediaTypes' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'cMediaTypes' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumMediaTypes)), 'ppenum' )),
]

class IAMTVAudioNotification(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{83EC1C33-23D1-11D1-99E6-00A0C9560266}')
    _idlflags_ = []
IAMTVAudioNotification._methods_ = [
    COMMETHOD([], HRESULT, 'OnEvent',
              ( ['in'], tagAMTVAudioEventType, 'Event' )),
]

class IAMPhysicalPinInfo(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{F938C991-3029-11CF-8C44-00AA006B6814}')
    _idlflags_ = []
IAMPhysicalPinInfo._methods_ = [
    COMMETHOD([], HRESULT, 'GetPhysicalType',
              ( ['out'], POINTER(c_int), 'pType' ),
              ( ['out'], POINTER(WSTRING), 'ppszType' )),
]

class IAMStreamSelect(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C1960960-17F5-11D1-ABE1-00A0C905F375}')
    _idlflags_ = []
IAMStreamSelect._methods_ = [
    COMMETHOD([], HRESULT, 'Count',
              ( ['out'], POINTER(c_ulong), 'pcStreams' )),
    COMMETHOD([], HRESULT, 'Info',
              ( ['in'], c_int, 'lIndex' ),
              ( ['out'], POINTER(POINTER(_AMMediaType)), 'ppmt' ),
              ( ['out'], POINTER(c_ulong), 'pdwFlags' ),
              ( ['out'], POINTER(c_ulong), 'plcid' ),
              ( ['out'], POINTER(c_ulong), 'pdwGroup' ),
              ( ['out'], POINTER(POINTER(c_ushort)), 'ppszName' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppObject' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppunk' )),
    COMMETHOD([], HRESULT, 'Enable',
              ( ['in'], c_int, 'lIndex' ),
              ( ['in'], c_ulong, 'dwFlags' )),
]

class IFilterGraph2(IGraphBuilder):
    _case_insensitive_ = True
    _iid_ = GUID('{36B73882-C2C8-11CF-8B46-00805F6CEF60}')
    _idlflags_ = []
IFilterGraph2._methods_ = [
    COMMETHOD([], HRESULT, 'AddSourceFilterForMoniker',
              ( ['in'], POINTER(IMoniker), 'pMoniker' ),
              ( ['in'], POINTER(IBindCtx), 'pCtx' ),
              ( ['in'], WSTRING, 'lpcwstrFilterName' ),
              ( ['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter' )),
    COMMETHOD([], HRESULT, 'ReconnectEx',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'RenderEx',
              ( ['in'], POINTER(IPin), 'ppinOut' ),
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pvContext' )),
]

class IAMCameraControl(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13370-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMCameraControl._methods_ = [
    COMMETHOD([], HRESULT, 'GetRange',
              ( ['in'], c_int, 'Property' ),
              ( ['out'], POINTER(c_int), 'pMin' ),
              ( ['out'], POINTER(c_int), 'pMax' ),
              ( ['out'], POINTER(c_int), 'pSteppingDelta' ),
              ( ['out'], POINTER(c_int), 'pDefault' ),
              ( ['out'], POINTER(c_int), 'pCapsFlags' )),
    COMMETHOD([], HRESULT, 'Set',
              ( ['in'], c_int, 'Property' ),
              ( ['in'], c_int, 'lValue' ),
              ( ['in'], c_int, 'Flags' )),
    COMMETHOD([], HRESULT, 'Get',
              ( ['in'], c_int, 'Property' ),
              ( ['out'], POINTER(c_int), 'lValue' ),
              ( ['out'], POINTER(c_int), 'Flags' )),
]

class IAMDecoderCaps(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C0DFF467-D499-4986-972B-E1D9090FA941}')
    _idlflags_ = []
IAMDecoderCaps._methods_ = [
    COMMETHOD([], HRESULT, 'GetDecoderCaps',
              ( ['in'], c_ulong, 'dwCapIndex' ),
              ( ['out'], POINTER(c_ulong), 'lpdwCap' )),
]

class IAMClockSlave(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{9FD52741-176D-4B36-8F51-CA8F933223BE}')
    _idlflags_ = []
IAMClockSlave._methods_ = [
    COMMETHOD([], HRESULT, 'SetErrorTolerance',
              ( ['in'], c_ulong, 'dwTolerance' )),
    COMMETHOD([], HRESULT, 'GetErrorTolerance',
              ( ['out'], POINTER(c_ulong), 'pdwTolerance' )),
]

__MIDL___MIDL_itf_DirectShow_0134_0001._fields_ = [
    ('clsMajorType', POINTER(GUID)),
    ('clsMinorType', POINTER(GUID)),
]
# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_DirectShow_0134_0001 is skipped.
class IAMCrossbar(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13380-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMCrossbar._methods_ = [
    COMMETHOD([], HRESULT, 'get_PinCounts',
              ( ['out'], POINTER(c_int), 'OutputPinCount' ),
              ( ['out'], POINTER(c_int), 'InputPinCount' )),
    COMMETHOD([], HRESULT, 'CanRoute',
              ( ['in'], c_int, 'OutputPinIndex' ),
              ( ['in'], c_int, 'InputPinIndex' )),
    COMMETHOD([], HRESULT, 'Route',
              ( ['in'], c_int, 'OutputPinIndex' ),
              ( ['in'], c_int, 'InputPinIndex' )),
    COMMETHOD([], HRESULT, 'get_IsRoutedTo',
              ( ['in'], c_int, 'OutputPinIndex' ),
              ( ['out'], POINTER(c_int), 'InputPinIndex' )),
    COMMETHOD([], HRESULT, 'get_CrossbarPinInfo',
              ( ['in'], c_int, 'IsInputPin' ),
              ( ['in'], c_int, 'PinIndex' ),
              ( ['out'], POINTER(c_int), 'PinIndexRelated' ),
              ( ['out'], POINTER(c_int), 'PhysicalType' )),
]

class IVMRWindowlessControl(IUnknown):
    _case_insensitive_ = True
    'IVMRWindowlessControl Interface'
    _iid_ = GUID('{0EB1088C-4DCD-46F0-878F-39DAE86A51B7}')
    _idlflags_ = []
IVMRWindowlessControl._methods_ = [
    COMMETHOD([], HRESULT, 'GetNativeVideoSize',
              ( ['out'], POINTER(c_int), 'lpWidth' ),
              ( ['out'], POINTER(c_int), 'lpHeight' ),
              ( ['out'], POINTER(c_int), 'lpARWidth' ),
              ( ['out'], POINTER(c_int), 'lpARHeight' )),
    COMMETHOD([], HRESULT, 'GetMinIdealVideoSize',
              ( ['out'], POINTER(c_int), 'lpWidth' ),
              ( ['out'], POINTER(c_int), 'lpHeight' )),
    COMMETHOD([], HRESULT, 'GetMaxIdealVideoSize',
              ( ['out'], POINTER(c_int), 'lpWidth' ),
              ( ['out'], POINTER(c_int), 'lpHeight' )),
    COMMETHOD([], HRESULT, 'SetVideoPosition',
              ( ['in'], POINTER(tagRECT), 'lpSRCRect' ),
              ( ['in'], POINTER(tagRECT), 'lpDSTRect' )),
    COMMETHOD([], HRESULT, 'GetVideoPosition',
              ( ['out'], POINTER(tagRECT), 'lpSRCRect' ),
              ( ['out'], POINTER(tagRECT), 'lpDSTRect' )),
    COMMETHOD([], HRESULT, 'GetAspectRatioMode',
              ( ['out'], POINTER(c_ulong), 'lpAspectRatioMode' )),
    COMMETHOD([], HRESULT, 'SetAspectRatioMode',
              ( ['in'], c_ulong, 'AspectRatioMode' )),
    COMMETHOD([], HRESULT, 'SetVideoClippingWindow',
              ( ['in'], wireHWND, 'hwnd' )),
    COMMETHOD([], HRESULT, 'RepaintVideo',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], wireHDC, 'hdc' )),
    COMMETHOD([], HRESULT, 'DisplayModeChanged'),
    COMMETHOD([], HRESULT, 'GetCurrentImage',
              ( ['out'], POINTER(POINTER(c_ubyte)), 'lpDib' )),
    COMMETHOD([], HRESULT, 'SetBorderColor',
              ( ['in'], c_ulong, 'Clr' )),
    COMMETHOD([], HRESULT, 'GetBorderColor',
              ( ['out'], POINTER(c_ulong), 'lpClr' )),
    COMMETHOD([], HRESULT, 'SetColorKey',
              ( ['in'], c_ulong, 'Clr' )),
    COMMETHOD([], HRESULT, 'GetColorKey',
              ( ['out'], POINTER(c_ulong), 'lpClr' )),
]

class Library(object):
    'DirectShow type library (Kohsuke private build)'
    name = 'DirectShowLib'
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)

# QUARTZ
typelib_path = 'quartz.dll'

class IMediaEvent(IDispatch):
    _case_insensitive_ = True
    'IMediaEvent interface'
    _iid_ = GUID('{56A868B6-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = ['dual', 'oleautomation']
class IMediaEventEx(IMediaEvent):
    _case_insensitive_ = True
    'IMediaEventEx interface'
    _iid_ = GUID('{56A868C0-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IMediaEvent._methods_ = [
    COMMETHOD([dispid(1610743808)], HRESULT, 'GetEventHandle',
              ( ['out'], POINTER(LONG_PTR), 'hEvent' )),
    COMMETHOD([dispid(1610743809)], HRESULT, 'GetEvent',
              ( ['out'], POINTER(c_int), 'lEventCode' ),
              ( ['out'], POINTER(LONG_PTR), 'lParam1' ),
              ( ['out'], POINTER(LONG_PTR), 'lParam2' ),
              ( ['in'], c_int, 'msTimeout' )),
    COMMETHOD([dispid(1610743810)], HRESULT, 'WaitForCompletion',
              ( ['in'], c_int, 'msTimeout' ),
              ( ['out'], POINTER(c_int), 'pEvCode' )),
    COMMETHOD([dispid(1610743811)], HRESULT, 'CancelDefaultHandling',
              ( ['in'], c_int, 'lEvCode' )),
    COMMETHOD([dispid(1610743812)], HRESULT, 'RestoreDefaultHandling',
              ( ['in'], c_int, 'lEvCode' )),
    COMMETHOD([dispid(1610743813)], HRESULT, 'FreeEventParams',
              ( ['in'], c_int, 'lEvCode' ),
              ( ['in'], LONG_PTR, 'lParam1' ),
              ( ['in'], LONG_PTR, 'lParam2' )),
]

IMediaEventEx._methods_ = [
    COMMETHOD([], HRESULT, 'SetNotifyWindow',
              ( ['in'], LONG_PTR, 'hwnd' ),
              ( ['in'], c_int, 'lMsg' ),
              ( ['in'], LONG_PTR, 'lInstanceData' )),
    COMMETHOD([], HRESULT, 'SetNotifyFlags',
              ( ['in'], c_int, 'lNoNotifyFlags' )),
    COMMETHOD([], HRESULT, 'GetNotifyFlags',
              ( ['out'], POINTER(c_int), 'lplNoNotifyFlags' )),
]

class IPinInfo(IDispatch):
    _case_insensitive_ = True
    'Pin Info'
    _iid_ = GUID('{56A868BD-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = ['dual', 'oleautomation']
IPinInfo._methods_ = [
    COMMETHOD([dispid(1610743808), 'propget'], HRESULT, 'Pin',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk' )),
    COMMETHOD([dispid(1610743809), 'propget'], HRESULT, 'ConnectedTo',
              ( ['out', 'retval'], POINTER(POINTER(IDispatch)), 'ppUnk' )),
    COMMETHOD([dispid(1610743810), 'propget'], HRESULT, 'ConnectionMediaType',
              ( ['out', 'retval'], POINTER(POINTER(IDispatch)), 'ppUnk' )),
    COMMETHOD([dispid(1610743811), 'propget'], HRESULT, 'FilterInfo',
              ( ['out', 'retval'], POINTER(POINTER(IDispatch)), 'ppUnk' )),
    COMMETHOD([dispid(1610743812), 'propget'], HRESULT, 'Name',
              ( ['out', 'retval'], POINTER(BSTR), 'ppUnk' )),
    COMMETHOD([dispid(1610743813), 'propget'], HRESULT, 'Direction',
              ( ['out', 'retval'], POINTER(c_int), 'ppDirection' )),
    COMMETHOD([dispid(1610743814), 'propget'], HRESULT, 'PinID',
              ( ['out', 'retval'], POINTER(BSTR), 'strPinID' )),
    COMMETHOD([dispid(1610743815), 'propget'], HRESULT, 'MediaTypes',
              ( ['out', 'retval'], POINTER(POINTER(IDispatch)), 'ppUnk' )),
    COMMETHOD([dispid(1610743816)], HRESULT, 'Connect',
              ( ['in'], POINTER(IUnknown), 'pPin' )),
    COMMETHOD([dispid(1610743817)], HRESULT, 'ConnectDirect',
              ( ['in'], POINTER(IUnknown), 'pPin' )),
    COMMETHOD([dispid(1610743818)], HRESULT, 'ConnectWithType',
              ( ['in'], POINTER(IUnknown), 'pPin' ),
              ( ['in'], POINTER(IDispatch), 'pMediaType' )),
    COMMETHOD([dispid(1610743819)], HRESULT, 'Disconnect'),
    COMMETHOD([dispid(1610743820)], HRESULT, 'Render'),
]

class IVideoWindow(IDispatch):
    _case_insensitive_ = True
    'IVideoWindow interface'
    _iid_ = GUID('{56A868B4-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = ['dual', 'oleautomation']
IVideoWindow._methods_ = [
    COMMETHOD([dispid(1610743808), 'propput'], HRESULT, 'Caption',
              ( ['in'], BSTR, 'strCaption' )),
    COMMETHOD([dispid(1610743808), 'propget'], HRESULT, 'Caption',
              ( ['out', 'retval'], POINTER(BSTR), 'strCaption' )),
    COMMETHOD([dispid(1610743810), 'propput'], HRESULT, 'WindowStyle',
              ( ['in'], c_int, 'WindowStyle' )),
    COMMETHOD([dispid(1610743810), 'propget'], HRESULT, 'WindowStyle',
              ( ['out', 'retval'], POINTER(c_int), 'WindowStyle' )),
    COMMETHOD([dispid(1610743812), 'propput'], HRESULT, 'WindowStyleEx',
              ( ['in'], c_int, 'WindowStyleEx' )),
    COMMETHOD([dispid(1610743812), 'propget'], HRESULT, 'WindowStyleEx',
              ( ['out', 'retval'], POINTER(c_int), 'WindowStyleEx' )),
    COMMETHOD([dispid(1610743814), 'propput'], HRESULT, 'AutoShow',
              ( ['in'], c_int, 'AutoShow' )),
    COMMETHOD([dispid(1610743814), 'propget'], HRESULT, 'AutoShow',
              ( ['out', 'retval'], POINTER(c_int), 'AutoShow' )),
    COMMETHOD([dispid(1610743816), 'propput'], HRESULT, 'WindowState',
              ( ['in'], c_int, 'WindowState' )),
    COMMETHOD([dispid(1610743816), 'propget'], HRESULT, 'WindowState',
              ( ['out', 'retval'], POINTER(c_int), 'WindowState' )),
    COMMETHOD([dispid(1610743818), 'propput'], HRESULT, 'BackgroundPalette',
              ( ['in'], c_int, 'pBackgroundPalette' )),
    COMMETHOD([dispid(1610743818), 'propget'], HRESULT, 'BackgroundPalette',
              ( ['out', 'retval'], POINTER(c_int), 'pBackgroundPalette' )),
    COMMETHOD([dispid(1610743820), 'propput'], HRESULT, 'Visible',
              ( ['in'], c_int, 'pVisible' )),
    COMMETHOD([dispid(1610743820), 'propget'], HRESULT, 'Visible',
              ( ['out', 'retval'], POINTER(c_int), 'pVisible' )),
    COMMETHOD([dispid(1610743822), 'propput'], HRESULT, 'Left',
              ( ['in'], c_int, 'pLeft' )),
    COMMETHOD([dispid(1610743822), 'propget'], HRESULT, 'Left',
              ( ['out', 'retval'], POINTER(c_int), 'pLeft' )),
    COMMETHOD([dispid(1610743824), 'propput'], HRESULT, 'Width',
              ( ['in'], c_int, 'pWidth' )),
    COMMETHOD([dispid(1610743824), 'propget'], HRESULT, 'Width',
              ( ['out', 'retval'], POINTER(c_int), 'pWidth' )),
    COMMETHOD([dispid(1610743826), 'propput'], HRESULT, 'Top',
              ( ['in'], c_int, 'pTop' )),
    COMMETHOD([dispid(1610743826), 'propget'], HRESULT, 'Top',
              ( ['out', 'retval'], POINTER(c_int), 'pTop' )),
    COMMETHOD([dispid(1610743828), 'propput'], HRESULT, 'Height',
              ( ['in'], c_int, 'pHeight' )),
    COMMETHOD([dispid(1610743828), 'propget'], HRESULT, 'Height',
              ( ['out', 'retval'], POINTER(c_int), 'pHeight' )),
    COMMETHOD([dispid(1610743830), 'propput'], HRESULT, 'Owner',
              ( ['in'], LONG_PTR, 'Owner' )),
    COMMETHOD([dispid(1610743830), 'propget'], HRESULT, 'Owner',
              ( ['out', 'retval'], POINTER(LONG_PTR), 'Owner' )),
    COMMETHOD([dispid(1610743832), 'propput'], HRESULT, 'MessageDrain',
              ( ['in'], LONG_PTR, 'Drain' )),
    COMMETHOD([dispid(1610743832), 'propget'], HRESULT, 'MessageDrain',
              ( ['out', 'retval'], POINTER(LONG_PTR), 'Drain' )),
    COMMETHOD([dispid(1610743834), 'propget'], HRESULT, 'BorderColor',
              ( ['out', 'retval'], POINTER(c_int), 'Color' )),
    COMMETHOD([dispid(1610743834), 'propput'], HRESULT, 'BorderColor',
              ( ['in'], c_int, 'Color' )),
    COMMETHOD([dispid(1610743836), 'propget'], HRESULT, 'FullScreenMode',
              ( ['out', 'retval'], POINTER(c_int), 'FullScreenMode' )),
    COMMETHOD([dispid(1610743836), 'propput'], HRESULT, 'FullScreenMode',
              ( ['in'], c_int, 'FullScreenMode' )),
    COMMETHOD([dispid(1610743838)], HRESULT, 'SetWindowForeground',
              ( ['in'], c_int, 'Focus' )),
    COMMETHOD([dispid(1610743839)], HRESULT, 'NotifyOwnerMessage',
              ( ['in'], LONG_PTR, 'hwnd' ),
              ( ['in'], c_int, 'uMsg' ),
              ( ['in'], LONG_PTR, 'wParam' ),
              ( ['in'], LONG_PTR, 'lParam' )),
    COMMETHOD([dispid(1610743840)], HRESULT, 'SetWindowPosition',
              ( ['in'], c_int, 'Left' ),
              ( ['in'], c_int, 'Top' ),
              ( ['in'], c_int, 'Width' ),
              ( ['in'], c_int, 'Height' )),
    COMMETHOD([dispid(1610743841)], HRESULT, 'GetWindowPosition',
              ( ['out'], POINTER(c_int), 'pLeft' ),
              ( ['out'], POINTER(c_int), 'pTop' ),
              ( ['out'], POINTER(c_int), 'pWidth' ),
              ( ['out'], POINTER(c_int), 'pHeight' )),
    COMMETHOD([dispid(1610743842)], HRESULT, 'GetMinIdealImageSize',
              ( ['out'], POINTER(c_int), 'pWidth' ),
              ( ['out'], POINTER(c_int), 'pHeight' )),
    COMMETHOD([dispid(1610743843)], HRESULT, 'GetMaxIdealImageSize',
              ( ['out'], POINTER(c_int), 'pWidth' ),
              ( ['out'], POINTER(c_int), 'pHeight' )),
    COMMETHOD([dispid(1610743844)], HRESULT, 'GetRestorePosition',
              ( ['out'], POINTER(c_int), 'pLeft' ),
              ( ['out'], POINTER(c_int), 'pTop' ),
              ( ['out'], POINTER(c_int), 'pWidth' ),
              ( ['out'], POINTER(c_int), 'pHeight' )),
    COMMETHOD([dispid(1610743845)], HRESULT, 'HideCursor',
              ( ['in'], c_int, 'HideCursor' )),
    COMMETHOD([dispid(1610743846)], HRESULT, 'IsCursorHidden',
              ( ['out'], POINTER(c_int), 'CursorHidden' )),
]

class Library(object):
    'ActiveMovie control type library'
    name = 'QuartzTypeLib'
    _reg_typelib_ = ('{56A868B0-0AD4-11CE-B03A-0020AF0BA770}', 1, 0)

class IBasicVideo(IDispatch):
    _case_insensitive_ = True
    'IBasicVideo interface'
    _iid_ = GUID('{56A868B5-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = ['dual', 'oleautomation']
class IBasicVideo2(IBasicVideo):
    _case_insensitive_ = True
    'IBasicVideo2'
    _iid_ = GUID('{329BB360-F6EA-11D1-9038-00A0C9697298}')
    _idlflags_ = []
IBasicVideo._methods_ = [
    COMMETHOD([dispid(1610743808), 'propget'], HRESULT, 'AvgTimePerFrame',
              ( ['out', 'retval'], POINTER(c_double), 'pAvgTimePerFrame' )),
    COMMETHOD([dispid(1610743809), 'propget'], HRESULT, 'BitRate',
              ( ['out', 'retval'], POINTER(c_int), 'pBitRate' )),
    COMMETHOD([dispid(1610743810), 'propget'], HRESULT, 'BitErrorRate',
              ( ['out', 'retval'], POINTER(c_int), 'pBitErrorRate' )),
    COMMETHOD([dispid(1610743811), 'propget'], HRESULT, 'VideoWidth',
              ( ['out', 'retval'], POINTER(c_int), 'pVideoWidth' )),
    COMMETHOD([dispid(1610743812), 'propget'], HRESULT, 'VideoHeight',
              ( ['out', 'retval'], POINTER(c_int), 'pVideoHeight' )),
    COMMETHOD([dispid(1610743813), 'propput'], HRESULT, 'SourceLeft',
              ( ['in'], c_int, 'pSourceLeft' )),
    COMMETHOD([dispid(1610743813), 'propget'], HRESULT, 'SourceLeft',
              ( ['out', 'retval'], POINTER(c_int), 'pSourceLeft' )),
    COMMETHOD([dispid(1610743815), 'propput'], HRESULT, 'SourceWidth',
              ( ['in'], c_int, 'pSourceWidth' )),
    COMMETHOD([dispid(1610743815), 'propget'], HRESULT, 'SourceWidth',
              ( ['out', 'retval'], POINTER(c_int), 'pSourceWidth' )),
    COMMETHOD([dispid(1610743817), 'propput'], HRESULT, 'SourceTop',
              ( ['in'], c_int, 'pSourceTop' )),
    COMMETHOD([dispid(1610743817), 'propget'], HRESULT, 'SourceTop',
              ( ['out', 'retval'], POINTER(c_int), 'pSourceTop' )),
    COMMETHOD([dispid(1610743819), 'propput'], HRESULT, 'SourceHeight',
              ( ['in'], c_int, 'pSourceHeight' )),
    COMMETHOD([dispid(1610743819), 'propget'], HRESULT, 'SourceHeight',
              ( ['out', 'retval'], POINTER(c_int), 'pSourceHeight' )),
    COMMETHOD([dispid(1610743821), 'propput'], HRESULT, 'DestinationLeft',
              ( ['in'], c_int, 'pDestinationLeft' )),
    COMMETHOD([dispid(1610743821), 'propget'], HRESULT, 'DestinationLeft',
              ( ['out', 'retval'], POINTER(c_int), 'pDestinationLeft' )),
    COMMETHOD([dispid(1610743823), 'propput'], HRESULT, 'DestinationWidth',
              ( ['in'], c_int, 'pDestinationWidth' )),
    COMMETHOD([dispid(1610743823), 'propget'], HRESULT, 'DestinationWidth',
              ( ['out', 'retval'], POINTER(c_int), 'pDestinationWidth' )),
    COMMETHOD([dispid(1610743825), 'propput'], HRESULT, 'DestinationTop',
              ( ['in'], c_int, 'pDestinationTop' )),
    COMMETHOD([dispid(1610743825), 'propget'], HRESULT, 'DestinationTop',
              ( ['out', 'retval'], POINTER(c_int), 'pDestinationTop' )),
    COMMETHOD([dispid(1610743827), 'propput'], HRESULT, 'DestinationHeight',
              ( ['in'], c_int, 'pDestinationHeight' )),
    COMMETHOD([dispid(1610743827), 'propget'], HRESULT, 'DestinationHeight',
              ( ['out', 'retval'], POINTER(c_int), 'pDestinationHeight' )),
    COMMETHOD([dispid(1610743829)], HRESULT, 'SetSourcePosition',
              ( ['in'], c_int, 'Left' ),
              ( ['in'], c_int, 'Top' ),
              ( ['in'], c_int, 'Width' ),
              ( ['in'], c_int, 'Height' )),
    COMMETHOD([dispid(1610743830)], HRESULT, 'GetSourcePosition',
              ( ['out'], POINTER(c_int), 'pLeft' ),
              ( ['out'], POINTER(c_int), 'pTop' ),
              ( ['out'], POINTER(c_int), 'pWidth' ),
              ( ['out'], POINTER(c_int), 'pHeight' )),
    COMMETHOD([dispid(1610743831)], HRESULT, 'SetDefaultSourcePosition'),
    COMMETHOD([dispid(1610743832)], HRESULT, 'SetDestinationPosition',
              ( ['in'], c_int, 'Left' ),
              ( ['in'], c_int, 'Top' ),
              ( ['in'], c_int, 'Width' ),
              ( ['in'], c_int, 'Height' )),
    COMMETHOD([dispid(1610743833)], HRESULT, 'GetDestinationPosition',
              ( ['out'], POINTER(c_int), 'pLeft' ),
              ( ['out'], POINTER(c_int), 'pTop' ),
              ( ['out'], POINTER(c_int), 'pWidth' ),
              ( ['out'], POINTER(c_int), 'pHeight' )),
    COMMETHOD([dispid(1610743834)], HRESULT, 'SetDefaultDestinationPosition'),
    COMMETHOD([dispid(1610743835)], HRESULT, 'GetVideoSize',
              ( ['out'], POINTER(c_int), 'pWidth' ),
              ( ['out'], POINTER(c_int), 'pHeight' )),
    COMMETHOD([dispid(1610743836)], HRESULT, 'GetVideoPaletteEntries',
              ( ['in'], c_int, 'StartIndex' ),
              ( ['in'], c_int, 'Entries' ),
              ( ['out'], POINTER(c_int), 'pRetrieved' ),
              ( ['out'], POINTER(c_int), 'pPalette' )),
    COMMETHOD([dispid(1610743837)], HRESULT, 'GetCurrentImage',
              ( ['in', 'out'], POINTER(c_int), 'pBufferSize' ),
              ( ['out'], POINTER(c_int), 'pDIBImage' )),
    COMMETHOD([dispid(1610743838)], HRESULT, 'IsUsingDefaultSource'),
    COMMETHOD([dispid(1610743839)], HRESULT, 'IsUsingDefaultDestination'),
]

IBasicVideo2._methods_ = [
    COMMETHOD([], HRESULT, 'GetPreferredAspectRatio',
              ( ['out'], POINTER(c_int), 'plAspectX' ),
              ( ['out'], POINTER(c_int), 'plAspectY' )),
]

class IAMCollection(IDispatch):
    _case_insensitive_ = True
    'Collection'
    _iid_ = GUID('{56A868B9-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = ['dual', 'oleautomation']
IAMCollection._methods_ = [
    COMMETHOD([dispid(1610743808), 'propget'], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'plCount' )),
    COMMETHOD([dispid(1610743809)], HRESULT, 'Item',
              ( ['in'], c_int, 'lItem' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppUnk' )),
    COMMETHOD([dispid(1610743810), 'propget'], HRESULT, '_NewEnum',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk' )),
]

class IMediaPosition(IDispatch):
    _case_insensitive_ = True
    'IMediaPosition interface'
    _iid_ = GUID('{56A868B2-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = ['dual', 'oleautomation']
IMediaPosition._methods_ = [
    COMMETHOD([dispid(1610743808), 'propget'], HRESULT, 'Duration',
              ( ['out', 'retval'], POINTER(c_double), 'plength' )),
    COMMETHOD([dispid(1610743809), 'propput'], HRESULT, 'CurrentPosition',
              ( ['in'], c_double, 'pllTime' )),
    COMMETHOD([dispid(1610743809), 'propget'], HRESULT, 'CurrentPosition',
              ( ['out', 'retval'], POINTER(c_double), 'pllTime' )),
    COMMETHOD([dispid(1610743811), 'propget'], HRESULT, 'StopTime',
              ( ['out', 'retval'], POINTER(c_double), 'pllTime' )),
    COMMETHOD([dispid(1610743811), 'propput'], HRESULT, 'StopTime',
              ( ['in'], c_double, 'pllTime' )),
    COMMETHOD([dispid(1610743813), 'propget'], HRESULT, 'PrerollTime',
              ( ['out', 'retval'], POINTER(c_double), 'pllTime' )),
    COMMETHOD([dispid(1610743813), 'propput'], HRESULT, 'PrerollTime',
              ( ['in'], c_double, 'pllTime' )),
    COMMETHOD([dispid(1610743815), 'propput'], HRESULT, 'Rate',
              ( ['in'], c_double, 'pdRate' )),
    COMMETHOD([dispid(1610743815), 'propget'], HRESULT, 'Rate',
              ( ['out', 'retval'], POINTER(c_double), 'pdRate' )),
    COMMETHOD([dispid(1610743817)], HRESULT, 'CanSeekForward',
              ( ['out', 'retval'], POINTER(c_int), 'pCanSeekForward' )),
    COMMETHOD([dispid(1610743818)], HRESULT, 'CanSeekBackward',
              ( ['out', 'retval'], POINTER(c_int), 'pCanSeekBackward' )),
]

class IMediaControl(IDispatch):
    _case_insensitive_ = True
    'IMediaControl interface'
    _iid_ = GUID('{56A868B1-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = ['dual', 'oleautomation']
IMediaControl._methods_ = [
    COMMETHOD([dispid(1610743808)], HRESULT, 'Run'),
    COMMETHOD([dispid(1610743809)], HRESULT, 'Pause'),
    COMMETHOD([dispid(1610743810)], HRESULT, 'Stop'),
    COMMETHOD([dispid(1610743811)], HRESULT, 'GetState',
              ( ['in'], c_int, 'msTimeout' ),
              ( ['out'], POINTER(c_int), 'pfs' )),
    COMMETHOD([dispid(1610743812)], HRESULT, 'RenderFile',
              ( ['in'], BSTR, 'strFilename' )),
    COMMETHOD([dispid(1610743813)], HRESULT, 'AddSourceFilter',
              ( ['in'], BSTR, 'strFilename' ),
              ( ['out'], POINTER(POINTER(IDispatch)), 'ppUnk' )),
    COMMETHOD([dispid(1610743814), 'propget'], HRESULT, 'FilterCollection',
              ( ['out', 'retval'], POINTER(POINTER(IDispatch)), 'ppUnk' )),
    COMMETHOD([dispid(1610743815), 'propget'], HRESULT, 'RegFilterCollection',
              ( ['out', 'retval'], POINTER(POINTER(IDispatch)), 'ppUnk' )),
    COMMETHOD([dispid(1610743816)], HRESULT, 'StopWhenReady'),
]

class IBasicAudio(IDispatch):
    _case_insensitive_ = True
    'IBasicAudio interface'
    _iid_ = GUID('{56A868B3-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = ['dual', 'oleautomation']
IBasicAudio._methods_ = [
    COMMETHOD([dispid(1610743808), 'propput'], HRESULT, 'Volume',
              ( ['in'], c_int, 'plVolume' )),
    COMMETHOD([dispid(1610743808), 'propget'], HRESULT, 'Volume',
              ( ['out', 'retval'], POINTER(c_int), 'plVolume' )),
    COMMETHOD([dispid(1610743810), 'propput'], HRESULT, 'Balance',
              ( ['in'], c_int, 'plBalance' )),
    COMMETHOD([dispid(1610743810), 'propget'], HRESULT, 'Balance',
              ( ['out', 'retval'], POINTER(c_int), 'plBalance' )),
]

class IQueueCommand(IUnknown):
    _case_insensitive_ = True
    'IQueueCommand'
    _iid_ = GUID('{56A868B7-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IDeferredCommand(IUnknown):
    _case_insensitive_ = True
    'IDeferredCommand'
    _iid_ = GUID('{56A868B8-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IQueueCommand._methods_ = [
    COMMETHOD([], HRESULT, 'InvokeAtStreamTime',
              ( ['out'], POINTER(POINTER(IDeferredCommand)), 'pCmd' ),
              ( ['in'], c_double, 'time' ),
              ( ['in'], POINTER(GUID), 'iid' ),
              ( ['in'], c_int, 'dispidMethod' ),
              ( ['in'], c_short, 'wFlags' ),
              ( ['in'], c_int, 'cArgs' ),
              ( ['in'], POINTER(VARIANT), 'pDispParams' ),
              ( ['in', 'out'], POINTER(VARIANT), 'pvarResult' ),
              ( ['out'], POINTER(c_short), 'puArgErr' )),
    COMMETHOD([], HRESULT, 'InvokeAtPresentationTime',
              ( ['out'], POINTER(POINTER(IDeferredCommand)), 'pCmd' ),
              ( ['in'], c_double, 'time' ),
              ( ['in'], POINTER(GUID), 'iid' ),
              ( ['in'], c_int, 'dispidMethod' ),
              ( ['in'], c_short, 'wFlags' ),
              ( ['in'], c_int, 'cArgs' ),
              ( ['in'], POINTER(VARIANT), 'pDispParams' ),
              ( ['in', 'out'], POINTER(VARIANT), 'pvarResult' ),
              ( ['out'], POINTER(c_short), 'puArgErr' )),
]

class IAMStats(IDispatch):
    _case_insensitive_ = True
    'Statistics'
    _iid_ = GUID('{BC9BCF80-DCD2-11D2-ABF6-00A0C905F375}')
    _idlflags_ = ['dual', 'oleautomation']
IAMStats._methods_ = [
    COMMETHOD([dispid(1610743808)], HRESULT, 'Reset'),
    COMMETHOD([dispid(1610743809), 'propget'], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'plCount' )),
    COMMETHOD([dispid(1610743810)], HRESULT, 'GetValueByIndex',
              ( ['in'], c_int, 'lIndex' ),
              ( ['out'], POINTER(BSTR), 'szName' ),
              ( ['out'], POINTER(c_int), 'lCount' ),
              ( ['out'], POINTER(c_double), 'dLast' ),
              ( ['out'], POINTER(c_double), 'dAverage' ),
              ( ['out'], POINTER(c_double), 'dStdDev' ),
              ( ['out'], POINTER(c_double), 'dMin' ),
              ( ['out'], POINTER(c_double), 'dMax' )),
    COMMETHOD([dispid(1610743811)], HRESULT, 'GetValueByName',
              ( ['in'], BSTR, 'szName' ),
              ( ['out'], POINTER(c_int), 'lIndex' ),
              ( ['out'], POINTER(c_int), 'lCount' ),
              ( ['out'], POINTER(c_double), 'dLast' ),
              ( ['out'], POINTER(c_double), 'dAverage' ),
              ( ['out'], POINTER(c_double), 'dStdDev' ),
              ( ['out'], POINTER(c_double), 'dMin' ),
              ( ['out'], POINTER(c_double), 'dMax' )),
    COMMETHOD([dispid(1610743812)], HRESULT, 'GetIndex',
              ( ['in'], BSTR, 'szName' ),
              ( ['in'], c_int, 'lCreate' ),
              ( ['out'], POINTER(c_int), 'plIndex' )),
    COMMETHOD([dispid(1610743813)], HRESULT, 'AddValue',
              ( ['in'], c_int, 'lIndex' ),
              ( ['in'], c_double, 'dValue' )),
]

class IFilterInfo(IDispatch):
    _case_insensitive_ = True
    'FilterInfo'
    _iid_ = GUID('{56A868BA-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = ['dual', 'oleautomation']
IFilterInfo._methods_ = [
    COMMETHOD([dispid(1610743808)], HRESULT, 'FindPin',
              ( ['in'], BSTR, 'strPinID' ),
              ( ['out'], POINTER(POINTER(IDispatch)), 'ppUnk' )),
    COMMETHOD([dispid(1610743809), 'propget'], HRESULT, 'Name',
              ( ['out', 'retval'], POINTER(BSTR), 'strName' )),
    COMMETHOD([dispid(1610743810), 'propget'], HRESULT, 'VendorInfo',
              ( ['out', 'retval'], POINTER(BSTR), 'strVendorInfo' )),
    COMMETHOD([dispid(1610743811), 'propget'], HRESULT, 'Filter',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk' )),
    COMMETHOD([dispid(1610743812), 'propget'], HRESULT, 'Pins',
              ( ['out', 'retval'], POINTER(POINTER(IDispatch)), 'ppUnk' )),
    COMMETHOD([dispid(1610743813), 'propget'], HRESULT, 'IsFileSource',
              ( ['out', 'retval'], POINTER(c_int), 'pbIsSource' )),
    COMMETHOD([dispid(1610743814), 'propget'], HRESULT, 'Filename',
              ( ['out', 'retval'], POINTER(BSTR), 'pstrFilename' )),
    COMMETHOD([dispid(1610743814), 'propput'], HRESULT, 'Filename',
              ( ['in'], BSTR, 'pstrFilename' )),
]

class IRegFilterInfo(IDispatch):
    _case_insensitive_ = True
    'Registry Filter Info'
    _iid_ = GUID('{56A868BB-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = ['dual', 'oleautomation']
IRegFilterInfo._methods_ = [
    COMMETHOD([dispid(1610743808), 'propget'], HRESULT, 'Name',
              ( ['out', 'retval'], POINTER(BSTR), 'strName' )),
    COMMETHOD([dispid(1610743809)], HRESULT, 'Filter',
              ( ['out'], POINTER(POINTER(IDispatch)), 'ppUnk' )),
]

IDeferredCommand._methods_ = [
    COMMETHOD([], HRESULT, 'Cancel'),
    COMMETHOD([], HRESULT, 'Confidence',
              ( ['out'], POINTER(c_int), 'pConfidence' )),
    COMMETHOD([], HRESULT, 'Postpone',
              ( ['in'], c_double, 'newtime' )),
    COMMETHOD([], HRESULT, 'GetHResult',
              ( ['out'], POINTER(HRESULT), 'phrResult' )),
]

class FilgraphManager(CoClass):
    'Filtergraph type info'
    _reg_clsid_ = GUID('{E436EBB3-524F-11CE-9F53-0020AF0BA770}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56A868B0-0AD4-11CE-B03A-0020AF0BA770}', 1, 0)
FilgraphManager._com_interfaces_ = [IMediaControl, IMediaEvent, IMediaPosition, IBasicAudio, IBasicVideo, IVideoWindow]

class IMediaTypeInfo(IDispatch):
    _case_insensitive_ = True
    'Media Type'
    _iid_ = GUID('{56A868BC-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = ['dual', 'oleautomation']
IMediaTypeInfo._methods_ = [
    COMMETHOD([dispid(1610743808), 'propget'], HRESULT, 'Type',
              ( ['out', 'retval'], POINTER(BSTR), 'strType' )),
    COMMETHOD([dispid(1610743809), 'propget'], HRESULT, 'Subtype',
              ( ['out', 'retval'], POINTER(BSTR), 'strType' )),
]

# CUSTOM

def SUCCEEDED(hr):
    return hr >= 0

def FAILED(hr):
    return hr < 0

PIN_DIR_OUT = 1
PIN_DIR_IN = 0

TIME_FORMAT_NONE = '{00000000-0000-0000-0000-000000000000}'
TIME_FORMAT_FRAME = '{7B785570-8C82-11CF-BC0C-00AA00AC74F6}'
TIME_FORMAT_BYTE  = '{7B785571-8C82-11CF-BC0C-00AA00AC74F6}'
TIME_FORMAT_SAMPLE = '{7B785572-8C82-11CF-BC0C-00AA00AC74F6}'
TIME_FORMAT_FIELD = '{7B785573-8C82-11CF-BC0C-00AA00AC74F6}'
TIME_FORMAT_MEDIA_TIME = '{7B785574-8C82-11CF-BC0C-00AA00AC74F6}'

FORMAT_VideoInfo = '{05589f80-c356-11ce-bf01-00aa0055595a}'
FORMAT_VideoInfo2 = '{F72A76A0-EB0A-11d0-ACE4-0000C0CC16BA}'
FORMAT_MPEGVideo = '{05589f82-c356-11ce-bf01-00aa0055595a}'
FORMAT_MPEG2_VIDEO = '{E06D80E3-DB46-11CF-B4D1-00805F6CBBEA}'


#typedef struct tagVIDEOINFOHEADER {
#
#    RECT            rcSource;          // The bit we really want to use
#    RECT            rcTarget;          // Where the video should go
#    DWORD           dwBitRate;         // Approximate bit data rate
#    DWORD           dwBitErrorRate;    // Bit error rate for this stream
#    REFERENCE_TIME  AvgTimePerFrame;   // Average time per frame (100ns units)
#
#    BITMAPINFOHEADER bmiHeader;
#
#} VIDEOINFOHEADER;

#typedef struct tagVIDEOINFOHEADER2 {
#  RECT             rcSource;
#  RECT             rcTarget;
#  DWORD            dwBitRate;
#  DWORD            dwBitErrorRate;
#  REFERENCE_TIME   AvgTimePerFrame;
#  DWORD            dwInterlaceFlags;
#  DWORD            dwCopyProtectFlags;
#  DWORD            dwPictAspectRatioX;
#  DWORD            dwPictAspectRatioY;
#  union {
#    DWORD dwControlFlags;
#    DWORD dwReserved1;
#  };
#  DWORD            dwReserved2;
#  BITMAPINFOHEADER bmiHeader;
#} VIDEOINFOHEADER2;

REFERENCE_TIME = c_longlong

class VIDEOINFOHEADER(Structure):
	_fields_ = (
		('rcSource', RECT),
		('rcTarget', RECT),
		('dwBitRate', DWORD),
		('dwBitErrorRate', DWORD),
		('AvgTimePerFrame', REFERENCE_TIME),
	)

class VIDEOINFOHEADER2(Structure):
	_fields_ = (
		('rcSource', RECT),
		('rcTarget', RECT),
		('dwBitRate', DWORD),
		('dwBitErrorRate', DWORD),
		('AvgTimePerFrame', REFERENCE_TIME),
	)

# VMR9
VMR9Mode_Windowed = 0x1
VMR9Mode_Windowless = 0x2

ProcAmpControl9_Brightness = 0x1
ProcAmpControl9_Contrast = 0x2
ProcAmpControl9_Hue = 0x4
ProcAmpControl9_Saturation = 0x8

# General
CLSID_FilterGraph			  = '{E436EBB3-524F-11CE-9F53-0020AF0BA770}'
CLSID_SystemDeviceEnum		 = '{62BE5D10-60EB-11d0-BD3B-00A0C911CE86}'
CLSID_SampleGrabber			= '{C1F400A0-3F08-11d3-9F0B-006008039E37}'
CLSID_CaptureGraphBuilder2	 = '{BF87B6E1-8C27-11d0-B3F0-00AA003761C5}'
CLSID_NullRender			   = '{C1F400A4-3F08-11D3-9F0B-006008039E37}'
CLSID_SmartTee				 = '{CC58E280-8AA1-11d1-B3F1-00AA003761C5}'

# Video renderers
CLSID_VideoRenderer			= '{70E102B0-5556-11CE-97C0-00AA0055595A}'
CLSID_VideoMixingRenderer	  = '{B87BEB7B-8D29-423F-AE4D-6582C10175AC}'
# CLSID_VideoRendererDefault = alias for CLSID_VideoMixingRenderer on systems
# that support VMR7 (XP or newer) or CLSID_VideoRenderer otherwise
CLSID_VideoRendererDefault	 = '{6BC1CFFA-8FC1-4261-AC22-CFB4CC38DB50}'
CLSID_VideoMixingRenderer9	 = '{51B4ABF3-748F-4E3B-A276-C828330E926A}'
CLSID_EnhancedVideoRenderer	= '{FA10746C-9B63-4B6C-BC49-FC300EA5F256}'

# Audio renderers
CLSID_DirectSoundAudioRenderer = '{79376820-07D0-11CF-A24D-0020AFD79767}'
CLSID_DefaultWaveOutDevice	 = '{E30629D1-27E5-11CE-875D-00608CB78066}'

# MIDI renderers
CLSID_MIDIRenderer			 = "{07B65360-C445-11CE-AFDE-00AA006C14F4}"

# Categories
CLSID_VideoInputDeviceCategory = '{860bb310-5d01-11d0-bd3b-00a0c911ce86}'
CLSID_AudioInputDeviceCategory = '{33d9a762-90c8-11d0-bd43-00a0c911ce86}'
CLSID_VideoCompressorCategory  = '{33d9a760-90c8-11d0-bd43-00a0c911ce86}'
CLSID_AudioCompressorCategory  = '{33d9a761-90c8-11d0-bd43-00a0c911ce86}'
CLSID_LegacyAmFilterCategory   = '{083863F1-70DE-11d0-BD40-00A0C911CE86}'
#CLSID_AudioRendererCategory	= '{E0F158E1-CB04-11D0-BD4E-00A0C911CE86}'
#CLSID_MidiRendererCategory	 = '{4EFE2452-168A-11D1-BC76-00C04FB9453B}'
#CLSID_MediaEncoderCategory	 = '{7D22E920-5CA9-4787-8C2B-A6779BD11781}'
#CLSID_MediaMultiplexerCategory = '{236C9559-ADCE-4736-BF72-BAB34E392196}'

# other MS filters
#CLSID_FileWriter			   = "{8596E5F0-0DA5-11D0-BD21-00A0C911CE86}"
#CLSID_WavDest				  = "{3C78B8E2-6C4D-11D1-ADE2-0000F8754B99}"
CLSID_MsDTVDVDAudioDecoder	 = "{E1F1A0B8-BEEE-490D-BA7C-066C40B5E2B9}"
CLSID_MsDTVDVDVideoDecoder	 = "{212690FB-83E5-4526-8FD7-74478B7939CD}"
#CLSID_OverlayMixer			 = "{CD8743A1-3736-11D0-9E69-00C04FD7C15B}"
#CLSID_OverlayMixer2			= "{A0025E90-E45B-11D1-ABE9-00A0C905F375}"
CLSID_FileSourceAsync		  = "{E436EBB5-524F-11CE-9F53-0020AF0BA770}"
#CLSID_FileSourceURL			= "{E436EBB6-524F-11CE-9F53-0020AF0BA770}"
#CLSID_WaveParser			   = "{D51BD5A1-7548-11CF-A520-0080C77EF58A}"
#CLSID_AVISplitter			  = "{1B544C20-FD0B-11CE-8C63-00AA0044B51E}"
CLSID_MIDIParser			   = "{D51BD5A2-7548-11CF-A520-0080C77EF58A}"
#CLSID_AVIWAVFileSource		 = "{D3588AB0-0781-11CE-B03A-0020AF0BA770}"
#CLSID_ColorSpaceConverter	  = "{1643E180-90F5-11CE-97D5-00AA0055595A}"
#CLSID_AudioRecorderWAVDest	 = "{E882F102-F626-49E9-BD68-CE2BE7E59EA0}"
#CLSID_AudioRecorderWaveForm	= "{E882F102-F626-49E9-BD68-CE2BE7E59EB0}"

# LAV filters
CLSID_LAVSplitterSource		= '{B98D13E7-55DB-4385-A33D-09FD1BA26338}'
CLSID_LAVVideoDecoder		  = '{EE30215D-164F-4A92-A4EB-9D4C13390F9F}'
CLSID_LAVAudioDecoder		  = '{E8E73B6B-4CB3-44A4-BE99-4F7BCB96E491}'

# VSFilter/DirectVobSub/DirectVobSubXy
CLSID_VSFilter				 = '{93A22E7A-5091-45EF-BA61-6DA26156A5D0}'
CLSID_VSFilter_autoload		= '{9852A670-F845-491B-9BE6-EBD841B8A613}'

########################################
# IVMRAspectRatioControl9
########################################
class IVMRAspectRatioControl9(IUnknown):
	_case_insensitive_ = True
	_iid_ = GUID('{00D96C29-BBDE-4EFC-9901-BB5036392146}')
	_idlflags_ = []

IVMRAspectRatioControl9._methods_ = [
	COMMETHOD([], HRESULT, 'GetAspectRatioMode',
			(['retval', 'out'], POINTER(DWORD), 'lpdwARMode')),
	COMMETHOD([], HRESULT, 'SetAspectRatioMode',
			(['in'], DWORD, 'dwARMode')),
]

########################################
# IVMRMixerControl9
# https://msdn.microsoft.com/en-us/windows/desktop/dd390457
########################################
class IVMRMixerControl9(IUnknown):
	_case_insensitive_ = True
	_iid_ = GUID('{1A777EAA-47C8-4930-B2C9-8FEE1C1B0F3B}')
	_idlflags_ = []

class VMR9NormalizedRect(Structure):
	_fields_ = (
		('left', FLOAT),
		('top', FLOAT),
		('right', FLOAT),
		('bottom', FLOAT)
	)

class VMR9ProcAmpControl(Structure):
	_fields_ = (
		('dwSize', DWORD),
		('dwFlags', DWORD),
		('Brightness', FLOAT),
		('Contrast', FLOAT),
		('Hue', FLOAT),
		('Saturation', FLOAT)
	)
	def __init__(self):
		self.dwSize = sizeof(VMR9ProcAmpControl)

class VMR9ProcAmpControlRange(Structure):
	_fields_ = (
		('dwSize', DWORD),
		('dwProperty', DWORD),
		('MinValue', FLOAT),
		('MaxValue', FLOAT),
		('DefaultValue', FLOAT),
		('StepSize', FLOAT)
	)
	def __init__(self):
		self.dwSize = sizeof(self)

IVMRMixerControl9._methods_ = [
	COMMETHOD([], HRESULT, 'SetAlpha',
			(['in'], DWORD, 'dwStreamID'),
			(['in'], FLOAT, 'Alpha')),
	COMMETHOD([], HRESULT, 'GetAlpha',
			(['in'], DWORD, 'dwStreamID'),
			(['out'], POINTER(FLOAT), 'pAlpha')),
	COMMETHOD([], HRESULT, 'SetZOrder',
			(['in'], DWORD, 'dwStreamID'),
			(['in'], DWORD, 'dwZ')),
	COMMETHOD([], HRESULT, 'GetZOrder',
			(['in'], DWORD, 'dwStreamID'),
			(['out'], POINTER(DWORD), 'pZ')),
	COMMETHOD([], HRESULT, 'SetOutputRect',
			(['in'], DWORD, 'dwStreamID'),
			(['in'], POINTER(VMR9NormalizedRect), 'pRect')),
	COMMETHOD([], HRESULT, 'GetOutputRect',
			(['in'], DWORD, 'dwStreamID'),
			(['in'], POINTER(VMR9NormalizedRect), 'pRect')),
	COMMETHOD([], HRESULT, 'SetBackgroundClr',
			(['in'], COLORREF, 'ClrBkg')),
	COMMETHOD([], HRESULT, 'GetBackgroundClr',
			(['in'], POINTER(COLORREF), 'lpClrBkg')),
	COMMETHOD([], HRESULT, 'SetMixingPrefs',
			(['in'], DWORD, 'dwMixerPrefs')),
	COMMETHOD([], HRESULT, 'GetMixingPrefs',
			(['out'], POINTER(DWORD), 'pdwMixerPrefs')),
	COMMETHOD([], HRESULT, 'SetProcAmpControl',
			(['in'], DWORD, 'dwStreamID'),
			(['in'], POINTER(VMR9ProcAmpControl), 'lpClrControl')),
	COMMETHOD([], HRESULT, 'GetProcAmpControl',
			(['in'], DWORD, 'dwStreamID'),
			(['in', 'out'], POINTER(VMR9ProcAmpControl), 'lpClrControl')),
	COMMETHOD([], HRESULT, 'GetProcAmpControlRange',
			(['in'], DWORD, 'dwStreamID'),
			(['in', 'out'], POINTER(VMR9ProcAmpControlRange), 'lpClrControl'))
]

########################################
# IDirectVobSub
########################################
class IDirectVobSub(IUnknown):
	_case_insensitive_ = True
	_iid_ = GUID('{EBE1FB08-3957-47CA-AF13-5827E5442E56}')
	_idlflags_ = []

IDirectVobSub._methods_ = [
	COMMETHOD([], HRESULT, 'get_FileName',
			(['in'], POINTER(BSTR), 'fn')),
	COMMETHOD([], HRESULT, 'put_FileName',
			(['in'], BSTR, 'fn')),
	COMMETHOD([], HRESULT, 'get_LanguageCount',
			(['retval', 'out'], POINTER(INT), 'nLangs')),
	COMMETHOD([], HRESULT, 'get_LanguageName',
			(['in'], BSTR, 'iLanguage'),
			(['retval', 'out'], POINTER(POINTER(BSTR)), 'ppName')),
	COMMETHOD([], HRESULT, 'get_SelectedLanguage',
			(['retval', 'out'], POINTER(INT), 'iSelected')),
	COMMETHOD([], HRESULT, 'put_SelectedLanguage',
			(['in'], INT, 'iSelected')),
	COMMETHOD([], HRESULT, 'get_HideSubtitles',
			(['retval', 'out'], POINTER(BOOL), 'fHideSubtitles')),
	COMMETHOD([], HRESULT, 'put_HideSubtitles',
			(['in'], BOOL, 'fHideSubtitles')),
]

########################################
# OleCreatePropertyFrame
########################################
LPUNKNOWN = POINTER(IUnknown)
CLSID = GUID
LPCLSID = POINTER(CLSID)

OleCreatePropertyFrame = windll.oleaut32.OleCreatePropertyFrame
OleCreatePropertyFrame.restype = HRESULT
OleCreatePropertyFrame.argtypes = (
	HWND,  # [in] hwndOwner
	UINT,  # [in] x
	UINT,  # [in] y
	LPCOLESTR,  # [in] lpszCaption
	ULONG,  # [in] cObjects
	POINTER(LPUNKNOWN),  # [in] ppUnk
	ULONG,  # [in] cPages
	LPCLSID,  # [in] pPageClsID
	LCID,  # [in] lcid
	DWORD,  # [in] dwReserved
	LPVOID,  # [in] pvReserved
)

########################################
# ISpecifyPropertyPages
########################################
class ISpecifyPropertyPages(IUnknown):
	_case_insensitive_ = True
	_iid_ = GUID('{B196B28B-BAB4-101A-B69C-00AA00341D07}')
	_idlflags_ = []

class CAUUID(Structure):
	_fields_ = (
		('element_count', ULONG),
		('elements', POINTER(GUID)),
	)
ISpecifyPropertyPages._methods_ = [
	COMMETHOD([], HRESULT, 'GetPages',
			(['out'], POINTER(CAUUID), 'pPages'),
			)
]

########################################
# IAMMediaContent
########################################
class IAMMediaContent(IDispatch):
	_case_insensitive_ = True
	_iid_ = GUID('{FA2AA8F4-8B62-11D0-A520-000000000000}')
	_idlflags_ = []

IAMMediaContent._methods_ = [
	COMMETHOD([], HRESULT, 'get_AuthorName',
			(['retval', 'out'], POINTER(BSTR), 'pbstrAuthorName')),
	COMMETHOD([], HRESULT, 'get_Title',
			(['retval', 'out'], POINTER(BSTR), 'pbstrTitle')),
	COMMETHOD([], HRESULT, 'get_Rating',
			(['retval', 'out'], POINTER(BSTR), 'pbstrRating')),
	COMMETHOD([], HRESULT, 'get_Description',
			(['retval', 'out'], POINTER(BSTR), 'pbstrDescription')),
	COMMETHOD([], HRESULT, 'get_Copyright',
			(['retval', 'out'], POINTER(BSTR), 'pbstrCopyright')),
	COMMETHOD([], HRESULT, 'get_BaseURL',
			(['retval', 'out'], POINTER(BSTR), 'pbstrBaseURL')),
	COMMETHOD([], HRESULT, 'get_LogoURL',
			(['retval', 'out'], POINTER(BSTR), 'pbstrLogoURL')),
	COMMETHOD([], HRESULT, 'get_LogoIconURL',
			(['retval', 'out'], POINTER(BSTR), 'pbstrLogoURL')),
	COMMETHOD([], HRESULT, 'get_WatermarkURL',
			(['retval', 'out'], POINTER(BSTR), 'pbstrWatermarkURL')),
	COMMETHOD([], HRESULT, 'get_MoreInfoURL',
			(['retval', 'out'], POINTER(BSTR), 'pbstrMoreInfoURL')),
	COMMETHOD([], HRESULT, 'get_MoreInfoBannerImage',
			(['retval', 'out'], POINTER(BSTR), 'pbstrMoreInfoBannerImage')),
	COMMETHOD([], HRESULT, 'get_MoreInfoBannerURL',
			(['retval', 'out'], POINTER(BSTR), 'pbstrMoreInfoBannerURL')),
	COMMETHOD([], HRESULT, 'get_MoreInfoText',
			(['retval', 'out'], POINTER(BSTR), 'pbstrMoreInfoText'))
]

########################################
# IVMRFilterConfig9
########################################
class IVMRFilterConfig9(IUnknown):
	_case_insensitive_ = False
	_iid_ = GUID('{5a804648-4f66-4867-9c43-4f5c822cf1b8}')
	_idlflags_ = []

IVMRFilterConfig9._methods_ = [
    COMMETHOD([], HRESULT, 'SetImageCompositor',
              ( ['in'], c_void_p, 'lpVMRImgCompositor' )),
    COMMETHOD([], HRESULT, 'SetNumberOfStreams',
              ( ['in'], DWORD, 'dwMaxStreams' )),
    COMMETHOD([], HRESULT, 'GetNumberOfStreams',
              ( ['out'], POINTER(DWORD), 'pdwMaxStreams' )),
    COMMETHOD([], HRESULT, 'SetRenderingPrefs',
              ( ['in'], DWORD, 'dwRenderFlags' )),
    COMMETHOD([], HRESULT, 'GetRenderingPrefs',
              ( ['out'], POINTER(DWORD), 'pdwRenderFlags' )),
    COMMETHOD([], HRESULT, 'SetRenderingMode',
              ( ['in'], DWORD, 'Mode' )),
    COMMETHOD([], HRESULT, 'GetRenderingMode',
              ( ['out'], POINTER(DWORD), 'pMode' )),
]

########################################
# IVMRWindowlessControl9
########################################

class IVMRWindowlessControl9(IUnknown):
	_case_insensitive_ = False
	_iid_ = GUID('{8f537d09-f85e-4414-b23b-502e54c79927}')
	_idlflags_ = []

LPBYTE = POINTER(BYTE)

class BITMAPINFOHEADER(Structure):
    _fields_ = [
            ('biSize', DWORD),
            ('biWidth', LONG),
            ('biHeight', LONG),
            ('biPlanes', WORD),
            ('biBitCount', WORD),
            ('biCompression', DWORD),
            ('biSizeImage', DWORD),
            ('biXPelsPerMeter', LONG),
            ('biYPelsPerMeter', LONG),
            ('biClrUsed', DWORD),
            ('biClrImportant', DWORD)
    ]

IVMRWindowlessControl9._methods_ = [
    COMMETHOD([], HRESULT, 'GetNativeVideoSize',
              ( ['out'], POINTER(LONG), 'lpWidth' ),
              ( ['out'], POINTER(LONG), 'lpHeight' ),
              ( ['out'], POINTER(LONG), 'lpARWidth' ),
              ( ['out'], POINTER(LONG), 'lpARHeight' )),
    COMMETHOD([], HRESULT, 'GetMinIdealVideoSize',
              ( ['out'], POINTER(LONG), 'lpWidth' ),
              ( ['out'], POINTER(LONG), 'lpHeight' )),
    COMMETHOD([], HRESULT, 'GetMaxIdealVideoSize',
              ( ['out'], POINTER(LONG), 'lpWidth' ),
              ( ['out'], POINTER(LONG), 'lpHeight' )),
    COMMETHOD([], HRESULT, 'SetVideoPosition',
              ( ['in'], POINTER(RECT), 'lpSRCRect' ),
              ( ['in'], POINTER(RECT), 'lpDSTRect' )),
    COMMETHOD([], HRESULT, 'GetVideoPosition',
              ( ['out'], POINTER(RECT), 'lpSRCRect' ),
              ( ['out'], POINTER(RECT), 'lpDSTRect' )),
    COMMETHOD([], HRESULT, 'GetAspectRatioMode',
              ( ['out'], POINTER(DWORD), 'lpAspectRatioMode' )),
    COMMETHOD([], HRESULT, 'SetAspectRatioMode',
              ( ['in'], DWORD, 'AspectRatioMode' )),
    COMMETHOD([], HRESULT, 'SetVideoClippingWindow',
              ( ['in'], HWND, 'hwnd' )),
    COMMETHOD([], HRESULT, 'RepaintVideo',
              ( ['in'], HWND, 'hwnd' ),
              ( ['in'], HDC, 'hdc' )),
    COMMETHOD([], HRESULT, 'DisplayModeChanged'),
    COMMETHOD([], HRESULT, 'GetCurrentImage',
              #( ['in'], POINTER(POINTER(BYTE)), 'lpDib' )),
              ( ['out'], POINTER(LPBYTE), 'lpDib' )),
    COMMETHOD([], HRESULT, 'SetBorderColor',
              ( ['in'], COLORREF, 'Clr' )),
    COMMETHOD([], HRESULT, 'GetBorderColor',
              ( ['out'], POINTER(COLORREF), 'lpClr' )),
]

# IMediaEvent constants
EC_ACTIVATE = 19
EC_BUFFERING_DATA = 17
EC_BUILT = 768
EC_CLOCK_CHANGED = 13
EC_CLOCK_UNSET = 81
EC_CODECAPI_EVENT = 87
EC_COMPLETE = 1
EC_DEVICE_LOST = 31
EC_DISPLAY_CHANGED = 22
EC_END_OF_SEGMENT = 28
EC_ERRORABORT = 3
EC_ERROR_STILLPLAYING = 8
EC_EXTDEVICE_MODE_CHANGE = 49
EC_FULLSCREEN_LOST = 18
EC_GRAPH_CHANGED = 80
EC_LENGTH_CHANGED = 30
EC_NEED_RESTART = 20
EC_NOTIFY_WINDOW = 25
EC_OLE_EVENT = 24
EC_OPENING_FILE = 16
EC_PALETTE_CHANGED = 9
EC_PAUSED = 14
EC_PREPROCESS_COMPLETE = 86
EC_QUALITY_CHANGE = 11
EC_REPAINT = 5
EC_SEGMENT_STARTED = 29
EC_SHUTTING_DOWN = 12
EC_SNDDEV_IN_ERROR = 512
EC_SNDDEV_OUT_ERROR = 513
EC_STARVATION = 23
EC_STATE_CHANGE = 50
EC_STEP_COMPLETE = 36
EC_STREAM_CONTROL_STARTED = 27
EC_STREAM_CONTROL_STOPPED = 26
EC_STREAM_ERROR_STILLPLAYING = 7
EC_STREAM_ERROR_STOPPED = 6
EC_SYSTEMBASE = 0
EC_TIME = 4
EC_TIMECODE_AVAILABLE = 48
EC_UNBUILT = 769
EC_USER = 32768
EC_USERABORT = 2
EC_VIDEO_SIZE_CHANGED = 10
EC_VMR_RECONNECTION_FAILED = 85
EC_VMR_RENDERDEVICE_SET = 83
EC_VMR_SURFACE_FLIPPED = 84
EC_WINDOW_DESTROYED = 21
EC_WMT_EVENT = 594
EC_WMT_INDEX_EVENT = 593



#AM_MEDIA_TYPE = _AMMediaType

#__all__ = [ 'DECIMATION_DEFAULT', 'AM_INTF_SEARCH_OUTPUT_PIN',
#           'AM_AUDREND_STAT_PARAM_SILENCE_DUR',
#           'ICaptureGraphBuilder2', 'AM_STREAM_MEDIA',
#           'tagVMRMONITORINFO',
#           'PhysConn_Video_VideoDecoder', 'IMediaSample2',
#           'AMTUNER_MODE_TV', 'IAMGraphBuilderCallback',
#           'IEnumMediaTypes', 'IFilterChain', 'IGraphConfig',
#           'DvSplitter', 'REG_PINFLAG_B_ZERO', 'PhysConn_Video_USB',
#           'IBindCtx', 'ISequentialStream', 'InterleavingMode',
#           'IAMFilterMiscFlags', 'IMemAllocatorCallbackTemp',
#           'ICreateDevEnum', '_AM_RENSDEREXFLAGS',
#           'AnalogVideo_PAL_B',
#           'VideoControlFlag_ExternalTriggerEnable', 'DvVideoDecoder',
#           'DeinterlacePref_Weave', 'IIPDVDec', 'VideoProcAmp_Gain',
#           'tagAMTunerSignalStrength', 'AM_PIN_FLOW_CONTROL_BLOCK',
#            'TunerInputAntenna', 'DVENCODERRESOLUTION_360x240',
#           'RenderPrefs_ForceOverlays', 'IMediaSample',
#           'PINDIR_INPUT', 'AMAP_3D_TARGET', 'AMOVERFX_MIRRORUPDOWN',
#           '_VMRVIDEOSTREAMINFO', 'IVMRFilterConfig',
#           'AMAP_FORCE_SYSMEM', 'AMSTREAMSELECTENABLE_ENABLEALL',
#           'IKsPropertySet',
#           'AM_GRAPH_CONFIG_RECONNECT_USE_ONLY_CACHED_FILTERS',
#           'IGraphConfigCallback', 'AM_SAMPLE_ENDOFSTREAM',
#           'AnalogVideo_NTSC_M', 'AM_SEEKING_CanGetDuration',
#           'VMRDeinterlaceTech', '_RGNDATA',
#           'VfwCaptureDialog_Source', 'AM_STREAM_CONTROL',
#           'RenderPrefs_DoNotRenderColorKeyAndBorder',
#           'AM_AUDREND_STAT_PARAM_DISCONTINUITIES',
#           'AM_STREAM_INFO_START_DEFINED', 'IResourceManager',
#           'CompressionCaps_CanCrunch', 'PhysConn_Video_1394',
#           'IAMDecoderCaps', 'AM_PUSHSOURCECAPS_PRIVATE_CLOCK',
#           'IAMTVAudio', 'tagCOLORKEY',
#           'AM_AUDREND_STAT_PARAM_SLAVE_DROPWRITE_DUR',
#           'State_Paused', 'IAsyncReader', '_FilterInfo',
#           'AM_SEEKING_CanSeekForwards', 'IEnumString',
#           'DVENCODERVIDEOFORMAT_PAL', 'DeinterlacePref_NextBest',
#           'IDistributorNotify', 'IStream', 'AMPROPERTY_PIN',
#           'IReferenceClock2', 'VideoControlFlag_FlipHorizontal',
#           'DECIMATION_USE_OVERLAY_ONLY', 'INTERLEAVE_FULL',
#           'IAMTVAudioNotification', 'AM_STREAM_INFO_DISCARDING',
#           'CompressionCaps_CanBFrame', 'FileWriter',
#           'IVideoFrameStep', '_AM_PUSHSOURCE_FLAGS',
#           'AM_SEEKING_AbsolutePositioning', 'IAMVideoControl',
#           'VariableBitRatePeak', 'IBaseFilter', 'IAMPushSource',
#           'CameraControl_Roll', 'AM_STREAM_INFO_STOP_SEND_EXTRA',
#           'AM_SEEKING_Segment', 'tagCameraControlFlags',
#           'AMTUNER_MODE_DEFAULT', 'DECIMATION_LEGACY',
#           'VMRSample_Discontinuity', 'AnalogVideo_SECAM_G',
#           'DeinterlaceTech_Unknown', 'VideoControlFlag_Trigger',
#           'IAMBufferNegotiation', 'tagVMRPRESENTATIONINFO',
#           'MixerPref_DecimateMask',
#           'VMR_ARMODE_NONE',
#           'CaptureGraphBuilder2', 'Flood', '_FilterState',
#           'DeinterlaceTech_MedianFiltering', 'IAMVideoProcAmp',
#           'DeinterlaceTech_BOBVerticalStretch',
#           'AMTUNER_SUBCHAN_DEFAULT', 'CompressionCaps_CanQuality',
#           'AMTUNER_MODE_AM_RADIO',
#           'DeinterlaceTech_BOBLineReplicate',
#           'ADVISE_DISPLAY_CHANGE', 'VideoProcAmp_Gamma',
#           '_RGNDATAHEADER', 'DVENCODERFORMAT_DVSD',
#           'MAX_NUMBER_OF_STREAMS', 'MixerPref_NoDecimation',
#           '_AllocatorProperties', 'AM_SAMPLE_SPLICEPOINT',
#           'AMTUNER_HASNOSIGNALSTRENGTH', 'AMAP_DXVA_TARGET',
#           'VMRRenderPrefs', 'AM_SEEKING_NoPositioning',
#           'tagVMRALLOCATIONINFO', 'AM_SEEKING_CanSeekBackwards',
#           'VideoCopyProtectionMacrovisionBasic', 'AM_SEEKING_Source',
#           'IVMRMixerBitmap', 'VideoProcAmp_ColorEnable',
#           'PhysConn_Video_YRYBY', 'AMOVERFX_MIRRORLEFTRIGHT',
#           'CameraControl_Exposure', 'VideoProcAmp_Saturation',
#           'AM_SEEKING_RelativePositioning', 'VMRSample_SyncPoint',
#           'AnalogVideo_SECAM_H', 'CodecAPIEventData', 'IOverlay',
#           'AM_SAMPLE_FLUSH_ON_PAUSE', 'CompressionCaps_CanWindow',
#           'IOverlayNotify2', 'IFileSourceFilter',
#           'CameraControl_Zoom',
#           'IAMCopyCaptureFileProgress', 'AnalogVideo_SECAM_L1',
#           'IEncoderAPI', 'IFilterGraph',
#           'RenderPrefs_RestrictToInitialMonitor',
#           'PhysConn_Audio_SCSI', 'AM_SEEKING_PositioningBitsMask',
#           'IMediaFilter', 'wireHDC', 'AM_SAMPLE_TIMEVALID', 'IDVEnc',
#           'AMTVAUDIO_MODE_MONO', 'AviMux',
#           'AM_AUDREND_STAT_PARAM_BUFFERFULLNESS',
#           'AMAP_ALLOW_SYSMEM', 'PhysConn_Audio_Tuner',
#           'VMR_ASPECT_RATIO_MODE', 'AM_FILTER_MISC_FLAGS_IS_SOURCE',
#           'VMR_ARMODE_LETTER_BOX',
#           'VideoCopyProtectionMacrovisionCBI',
#           'PhysConn_Video_SVideo', 'IMemInputPin', 'IAMStreamSelect',
#           'AMOVERLAYFX', 'AMPROPERTY_PIN_MEDIUM',
#           'IAMVfwCaptureDialogs', 'CameraControl_Pan', 'tagSTATSTG',
#           'IVMRImagePresenterConfig',
#           'tagVideoProcAmpFlags', '_DVENCODERVIDEOFORMAT',
#           'tagTVAudioMode', 'IAMVideoDecimationProperties',
#           'DeinterlaceTech_MotionVectorSteered',
#           'DVENCODERFORMAT_DVSL', 'tagTIMECODE_SAMPLE',
#           'AMTVAUDIO_MODE_LANG_A',
#           'AMTVAUDIO_MODE_STEREO', '_AM_FILTER_FLAGS',
#           'AMTVAUDIO_MODE_LANG_B', 'tagPALETTEENTRY',
#           'AnalogVideo_PAL_60', 'VMRSample_TimeValid',
#           'IAMExtDevice',
#           'IGetCapabilitiesKey', 'IAMTVTuner',
#           'MixerPref_RenderTargetYUV444', 'REG_PINFLAG_B_RENDERER',
#           'AM_SEEKING_SeekingFlags', 'IDecimateVideoImage',
#           'REGFILTERPINS', 'AnalogVideo_PAL_M', '_PinDirection',
#           'DVENCODERRESOLUTION_180x120',
#           'VideoProcAmp_BacklightCompensation',
#           'AM_AUDREND_STAT_PARAM_LAST_BUFFER_DUR',
#           'AM_SEEKING_IncrementalPositioning',
#           'AMTUNER_EVENT_CHANGED', '_AMRESCTL_RESERVEFLAGS',
#           'AM_SEEKING_CanSeekAbsolute',
#           'VMRPresentationFlags', 'VfwCaptureDialogs',
#           'IOverlayNotify', 'AMTUNER_MODE_FM_RADIO',
#           '_REM_FILTER_FLAGS', 'IVMRSurfaceAllocatorNotify',
#           'DVENCODERFORMAT_DVHD', 'IPinConnection',
#           'VideoProcAmp_Flags_Auto', 'DVRESOLUTION_DC',
#           'IAMovieSetup', 'AM_FILTER_FLAGS_REMOVABLE',
#           'VariableBitRateAverage', 'DVENCODERRESOLUTION_88x60',
#           'IVideoEncoder', 'IVMRMonitorConfig', 'DVRESOLUTION_FULL',
#           'IStreamBuilder', 'IAMAnalogVideoDecoder',
#           'AnalogVideo_SECAM_L', 'AviSplitter', 'VideoProcAmp_Hue',
#           'VIDEOENCODER_BITRATE_MODE', 'IAMLatency',
#           'PhysConn_Video_VideoEncoder',
#           'RenderPrefs_Mask', 'IAMTuner', 'INTERLEAVE_CAPTURE',
#           'PhysConn_Audio_Line', 'PhysConn_Audio_AESDigital',
#           'tagAMTunerModeType', 'AMTVAUDIO_EVENT_CHANGED',
#           'AM_SEEKING_CanPlayBackwards', 'IResourceConsumer',
#           'IMemAllocator', 'AM_AUDREND_STAT_PARAM_JITTER',
#           'DeinterlacePref_BOB', 'AMRESCTL_RESERVEFLAGS_RESERVE',
#           'VfwCompressDialogs', 'MixerPref_PointFiltering',
#           'AM_AUDREND_STAT_PARAM_BREAK_COUNT', 'CameraControl_Iris',
#           'State_Stopped', 'IMoniker', 'IPinFlowControl',
#           '_VMRVideoDesc', 'AM_SEEKING_SeekingCapabilities',
#           'AM_SEEKING_NoFlush',
#           'MixerPref_RenderTargetMask', 'ADVISE_CLIPPING',
#           'DVENCODERVIDEOFORMAT_NTSC', 'IAMCameraControl',
#           'DECIMATION_USE_VIDEOPORT_ONLY', 'VMRMode_Windowless',
#           'IFilterMapper2', 'CK_RGB', 'IConfigInterleaving',
#           'AM_SEEKING_CanDoSegments', 'IVMRMixerControl',
#           'IReferenceClock', 'IVMRImagePresenterExclModeConfig',
#           'IMemAllocatorNotifyCallbackTemp',
#           'AMTUNER_SUBCHAN_NO_TUNE', 'IVMRSurface',
#           'AsyncFileReader', '_AM_AUDIO_RENDERER_STAT_PARAM',
#           'IAMVfwCompressDialogs', 'AM_INTF_SEARCH_INPUT_PIN',
#           'IEnumStreamIdMap',
#           'ConstantBitRate',
#           'VideoCopyProtectionType', 'PhysConn_Video_Composite',
#           'AM_FILE_OVERWRITE', 'CameraControl_Tilt',
#           'AMSTREAMSELECTINFO_EXCLUSIVE', 'CK_NOCOLORKEY',
#           'REGFILTER2', 'ADVISE_NONE',
#           'IAMExtTransport', 'IAMGraphStreams', 'PhysConn_Audio_Mic',
#           'AM_SEEKING_ReturnTime', 'PhysConn_Video_RGB',
#           'DVDECODERRESOLUTION_360x240', 'PhysConn_Video_Tuner',
#           'DVENCODERRESOLUTION_720x480', 'IGraphVersion',
#           'tagPhysicalConnectorType', 'DVINFO', 'CK_INDEX',
#           'DECIMATION_USE_DECODER_ONLY', 'IVMRSurfaceAllocator',
#           'VideoControlFlag_FlipVertical', '_DVENCODERRESOLUTION',
#           'RenderPrefs_ForceOffscreen', 'tagTIMECODE',
#           'STREAM_ID_MAP', 'IAMAudioInputMixer',
#           'CameraControl_Focus', 'AMSTREAMSELECTINFO_ENABLED',
#           'PhysConn_Video_SCSI', 'tagTunerInputType',
#           'IAMDroppedFrames', 'AnalogVideo_SECAM_B', '_DVRESOLUTION',
#           'INTERLEAVE_NONE_BUFFERED', 'ADVISE_COLORKEY',
#           '_DVDECODERRESOLUTION', 'IFilterMapper3',
#           'AnalogVideo_PAL_N_COMBO', 'MixerPref_RenderTargetYUV422',
#           'ICaptureGraphBuilder', 'IDVRGB219',
#           'AMSTREAMSELECTENABLE_ENABLE', 'PhysConn_Audio_AUX',
#           'AMOVERFX_DEINTERLACE',
#           'REG_PINFLAG_B_OUTPUT', 'AnalogVideo_SECAM_K',
#           'AnalogVideo_PAL_D', 'AnalogVideo_NTSC_M_J',
#           'VMRDeinterlacePrefs', 'IPersistStream',
#           'IVMRImagePresenter', 'ISeekingPassThru',
#           'PhysConn_Audio_USB', 'IMediaPropertyBag',
#           '_AM_GRAPH_CONFIG_RECONNECT_FLAGS', 'IBPCSatelliteTuner',
#           'tagAMTVAudioEventType', 'DeinterlaceTech_EdgeFiltering',
#           'IMediaSeeking', 'AMTUNER_NOSIGNAL', 'VMRMode_Mask',
#           'RenderPrefs_Reserved',
#           'tagAMTunerEventType', 'TunerInputCable', 'PINDIR_OUTPUT',
#           'IVPManager',
#           '_VMRFrequency', 'VideoProcAmp_Contrast',
#           'IEnumFilters',
#           'CameraControl_Flags_Manual', 'IAMStreamConfig',
#           'REG_PINFLAG_B_MANY', 'IAMTunerNotification', 'IEnumPins',
#           'DeinterlacePref_Mask', 'IFilterGraph2', 'IAMOpenProgress',
#           '_RemotableHandle', 'MixerPref_RenderTargetReserved',
#           'IPin',
#           'AMTUNER_SIGNALPRESENT', 'DVDECODERRESOLUTION_720x480',
#           'AnalogVideo_PAL_G', 'VMRMixerPrefs',
#           'PhysConn_Audio_SPDIFDigital', 'MixerPref_DecimateOutput',
#           'AnalogVideo_PAL_H', 'AM_SAMPLE_TYPECHANGED',
#           'IEnumMoniker', 'VMRMode_Windowed', 'IVMRImageCompositor',
#           'AnalogVideo_None', 'AMAP_PIXELFORMAT_VALID',
#           'REMFILTERF_LEAVECONNECTED',
#           '_AM_PIN_FLOW_CONTROL_BLOCK_FLAGS', 'AMAP_DIRECTED_FLIP',
#           '_AMMediaType', 'REGPINTYPES', 'IAMAnalogVideoEncoder',
#           'RenderPrefs_PreferAGPMemWhenMixing',
#           'tagAnalogVideoStandard',
#           'AM_AUDREND_STAT_PARAM_SLAVE_RATE',
#           'AM_STREAM_INFO_STOP_DEFINED', 'IVMRWindowlessControl',
#           'IGraphBuilder', 'VideoProcAmp_Flags_Manual',
#           'AM_PUSHSOURCECAPS_INTERNAL_RM', 'AnalogVideo_NTSC_433',
#           'AM_SAMPLE_PREROLL', 'DVDECODERRESOLUTION_88x60',
#           'CompressionCaps_CanKeyFrame', 'IVMRDeinterlaceControl',
#           'FilterGraph',
#           'MixerPref_RenderTargetRGB', 'AM_SAMPLE_DATADISCONTINUITY',
#           'AMRESCTL_RESERVEFLAGS_UNRESERVE',
#           'VfwCompressDialog_QueryConfig', 'VMRSample_Preroll',
#           'AMTUNER_MODE_DSS', 'IAMOverlayFX',
#           'AM_FILTER_MISC_FLAGS_IS_RENDERER', 'PhysConn_Video_SCART',
#           'AMPROPERTY_PIN_CATEGORY', 'IMPEG2StreamIdMap',
#           'IConfigAviMux', 'PhysConn_Video_AUX', '_NORMALIZEDRECT',
#           'tagQuality', 'IDrawVideoImage', 'IAMDeviceRemoval',
#           'IFileSinkFilter2', 'AM_PUSHSOURCECAPS_NOT_LIVE',
#           'IPersistMediaPropertyBag',
#           'tagAMTunerSubChannel', 'VfwCompressDialog_QueryAbout',
#           'VideoProcAmp_Sharpness', 'AM_SEEKING_SeekToKeyFrame',
#           'ADVISE_PALETTE', 'AnalogVideo_PAL_I', 'IAMCrossbar',
#           'AM_SEEKING_CanGetCurrentPos',
#           'DeinterlaceTech_FieldAdaptive', 'IAMClockSlave',
#           'IVMRAspectRatioControl', 'tagAM_SAMPLE_PROPERTY_FLAGS',
#           'DDCOLORKEY', 'VMRMode_Renderless', 'ADVISE_POSITION',
#           'IVMRVideoStreamControl', 'IAMAudioRendererStats',
#           'IAMVideoCompression', 'IAMClockAdjust',
#           'AM_PUSHSOURCEREQS_USE_STREAM_CLOCK',
#           'VfwCaptureDialog_Format', 'IFileSinkFilter', 'ICodecAPI',
#           '_VMRDeinterlaceCaps', '_DECIMATION_USAGE',
#           '_AM_INTF_SEARCH_FLAGS', 'IQualityControl',
#           'AM_AUDREND_STAT_PARAM_SLAVE_LASTHIGHLOWERROR',
#           'AM_AUDREND_STAT_PARAM_SLAVE_ACCUMERROR',
#           'AM_GRAPH_CONFIG_RECONNECT_DIRECTCONNECT',
#           '_AMSTREAMSELECTENABLEFLAGS', 'IDVSplitter',
#           'CameraControl_Flags_Auto', 'REGFILTER',
#           'IAMTimecodeReader', 'IAMDevMemoryAllocator',
#           'AnalogVideo_SECAM_K1', 'State_Running',
#           'RenderPrefs_AllowOverlays', 'IEnumRegFilters',
#           'IFilterMapper', 'IMpeg2Demultiplexer',
#           'AM_AUDREND_STAT_PARAM_SLAVE_HIGHLOWERROR',
#           'REGFILTERPINS2', 'IRunningObjectTable', 'INTERLEAVE_NONE',
#           'VMRMode', 'tagQualityMessageType',
#           '_AM_FILTER_MISC_FLAGS',
#           'AM_AUDREND_STAT_PARAM_SLAVE_MODE',
#           'tagCameraControlProperty', 'IMediaEventSink',
#           'tagVideoProcAmpProperty', 'AMOVERFX_NOFX',
#           'tagVideoControlFlags', 'MixerPref_RenderTargetYUV420',
#           'IAMPhysicalPinInfo', 'AM_SAMPLE_TIMEDISCONTINUITY',
#           'VideoProcAmp_WhiteBalance', 'AMTVAUDIO_MODE_LANG_C',
#           'IRegisterServiceProvider', 'IAMTimecodeDisplay',
#           'DVRESOLUTION_HALF', 'AM_SEEKING_CanGetStopPos',
#           'VfwCaptureDialog_Display', 'VfwCompressDialog_About',
#           'AM_FILESINK_FLAGS', 'DeinterlaceTech_PixelAdaptive',
#           'tagVMRGUID', 'MixerPref_BiLinearFiltering',
#           'AM_STREAM_INFO', 'VideoProcAmp_Brightness',
#           'AM_SAMPLE_STOPVALID', '_VMRALPHABITMAP',
#           'VMRSurfaceAllocationFlags', 'CompressionCaps',
#           'PhysConn_Audio_1394', 'PhysConn_Video_Black', 'LONG_PTR',
#           '_DVENCODERFORMAT', 'Famine',
#           'PhysConn_Audio_AudioDecoder',
#           'AnalogVideo_PAL_N', 'MixerPref_FilteringMask',
#           'RenderPrefs_AllowOffscreen', '_AMSTREAMSELECTINFOFLAGS',
#           'IAMResourceControl', 'REGPINMEDIUM', '_PinInfo',
#           'AnalogVideo_SECAM_D', 'PhysConn_Video_SerialDigital',
#           'DVDECODERRESOLUTION_180x120', 'VfwCompressDialog_Config',
#           'AM_RENDEREX_RENDERTOEXISTINGRENDERERS',
#           'AM_INTF_SEARCH_FILTER', 'AM_STREAM_INFO_FLAGS',
#           'IAMStreamControl', 'IAMTimecodeGenerator',
#           'tagAM_SAMPLE2_PROPERTIES',
#           'PhysConn_Video_ParallelDigital', 'DVRESOLUTION_QUARTER',
#           'AM_GRAPH_CONFIG_RECONNECT_CACHE_REMOVED_FILTERS',
#           'IAMDevMemoryControl',
#           # quartz
#           'IAMStats', 'IMediaEvent', 'IBasicVideo', 'IFilterInfo',
#           'FilgraphManager', 'IPinInfo', 'IDeferredCommand',
#           'IRegFilterInfo', 'LONG_PTR', 'IVideoWindow',
#           'IMediaPosition', 'IMediaControl', 'IBasicVideo2',
#           'IMediaEventEx', 'IQueueCommand', 'IMediaTypeInfo',
#           'IBasicAudio', 'IAMCollection']
