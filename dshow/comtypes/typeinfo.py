import sys
import weakref

from ctypes import *
from ctypes.wintypes import ULONG

from dshow.comtypes import STDMETHOD, COMMETHOD, _GUID, GUID
# XXX should import more stuff from ctypes.wintypes...
from dshow.comtypes.automation import (BSTR, DISPID, DISPPARAMS, DWORD, EXCEPINFO, HRESULT, IID, IUnknown, LCID, LONG,
        SCODE, UINT, VARIANT, VARIANTARG, VARTYPE, WCHAR, WORD, tagVARIANT)

is_64_bit = sys.maxsize > 2**32

BOOL = c_int
HREFTYPE = DWORD
INT = c_int
MEMBERID = DISPID
OLECHAR = WCHAR
PVOID = c_void_p
SHORT = c_short
# See https://msdn.microsoft.com/en-us/library/windows/desktop/aa383751(v=vs.85).aspx#ULONG_PTR  # noqa
ULONG_PTR = c_uint64 if is_64_bit else c_ulong

USHORT = c_ushort
LPOLESTR = POINTER(OLECHAR)

################################################################
# enums
tagSYSKIND = c_int # enum
SYS_WIN16 = 0
SYS_WIN32 = 1
SYS_MAC = 2
SYS_WIN64 = 3
SYSKIND = tagSYSKIND

tagREGKIND = c_int # enum
REGKIND_DEFAULT = 0
REGKIND_REGISTER = 1
REGKIND_NONE = 2
REGKIND = tagREGKIND

tagTYPEKIND = c_int # enum
TKIND_ENUM = 0
TKIND_RECORD = 1
TKIND_MODULE = 2
TKIND_INTERFACE = 3
TKIND_DISPATCH = 4
TKIND_COCLASS = 5
TKIND_ALIAS = 6
TKIND_UNION = 7
TKIND_MAX = 8
TYPEKIND = tagTYPEKIND

tagINVOKEKIND = c_int # enum
INVOKE_FUNC = 1
INVOKE_PROPERTYGET = 2
INVOKE_PROPERTYPUT = 4
INVOKE_PROPERTYPUTREF = 8
INVOKEKIND = tagINVOKEKIND

tagDESCKIND = c_int # enum
DESCKIND_NONE = 0
DESCKIND_FUNCDESC = 1
DESCKIND_VARDESC = 2
DESCKIND_TYPECOMP = 3
DESCKIND_IMPLICITAPPOBJ = 4
DESCKIND_MAX = 5
DESCKIND = tagDESCKIND

tagVARKIND = c_int # enum
VAR_PERINSTANCE = 0
VAR_STATIC = 1
VAR_CONST = 2
VAR_DISPATCH = 3
VARKIND = tagVARKIND

tagFUNCKIND = c_int # enum
FUNC_VIRTUAL = 0
FUNC_PUREVIRTUAL = 1
FUNC_NONVIRTUAL = 2
FUNC_STATIC = 3
FUNC_DISPATCH = 4
FUNCKIND = tagFUNCKIND

tagCALLCONV = c_int # enum
CC_FASTCALL = 0
CC_CDECL = 1
CC_MSCPASCAL = 2
CC_PASCAL = 2
CC_MACPASCAL = 3
CC_STDCALL = 4
CC_FPFASTCALL = 5
CC_SYSCALL = 6
CC_MPWCDECL = 7
CC_MPWPASCAL = 8
CC_MAX = 9
CALLCONV = tagCALLCONV

IMPLTYPEFLAG_FDEFAULT = 1
IMPLTYPEFLAG_FSOURCE = 2
IMPLTYPEFLAG_FRESTRICTED = 4
IMPLTYPEFLAG_FDEFAULTVTABLE = 8

tagTYPEFLAGS = c_int # enum
TYPEFLAG_FAPPOBJECT = 1
TYPEFLAG_FCANCREATE = 2
TYPEFLAG_FLICENSED = 4
TYPEFLAG_FPREDECLID = 8
TYPEFLAG_FHIDDEN = 16
TYPEFLAG_FCONTROL = 32
TYPEFLAG_FDUAL = 64
TYPEFLAG_FNONEXTENSIBLE = 128
TYPEFLAG_FOLEAUTOMATION = 256
TYPEFLAG_FRESTRICTED = 512
TYPEFLAG_FAGGREGATABLE = 1024
TYPEFLAG_FREPLACEABLE = 2048
TYPEFLAG_FDISPATCHABLE = 4096
TYPEFLAG_FREVERSEBIND = 8192
TYPEFLAG_FPROXY = 16384
TYPEFLAGS = tagTYPEFLAGS

tagFUNCFLAGS = c_int # enum
FUNCFLAG_FRESTRICTED = 1
FUNCFLAG_FSOURCE = 2
FUNCFLAG_FBINDABLE = 4
FUNCFLAG_FREQUESTEDIT = 8
FUNCFLAG_FDISPLAYBIND = 16
FUNCFLAG_FDEFAULTBIND = 32
FUNCFLAG_FHIDDEN = 64
FUNCFLAG_FUSESGETLASTERROR = 128
FUNCFLAG_FDEFAULTCOLLELEM = 256
FUNCFLAG_FUIDEFAULT = 512
FUNCFLAG_FNONBROWSABLE = 1024
FUNCFLAG_FREPLACEABLE = 2048
FUNCFLAG_FIMMEDIATEBIND = 4096
FUNCFLAGS = tagFUNCFLAGS

tagVARFLAGS = c_int # enum
VARFLAG_FREADONLY = 1
VARFLAG_FSOURCE = 2
VARFLAG_FBINDABLE = 4
VARFLAG_FREQUESTEDIT = 8
VARFLAG_FDISPLAYBIND = 16
VARFLAG_FDEFAULTBIND = 32
VARFLAG_FHIDDEN = 64
VARFLAG_FRESTRICTED = 128
VARFLAG_FDEFAULTCOLLELEM = 256
VARFLAG_FUIDEFAULT = 512
VARFLAG_FNONBROWSABLE = 1024
VARFLAG_FREPLACEABLE = 2048
VARFLAG_FIMMEDIATEBIND = 4096
VARFLAGS = tagVARFLAGS

PARAMFLAG_NONE = 0
PARAMFLAG_FIN = 1
PARAMFLAG_FOUT = 2
PARAMFLAG_FLCID = 4
PARAMFLAG_FRETVAL = 8
PARAMFLAG_FOPT = 16
PARAMFLAG_FHASDEFAULT = 32
PARAMFLAG_FHASCUSTDATA = 64

################################################################
# a helper
def _deref_with_release(ptr, release):
    # Given a POINTER instance, return the pointed to value.
    # Call the 'release' function with 'ptr' to release resources
    # when the value is no longer needed.
    result = ptr[0]
    result.__ref__ = weakref.ref(result, lambda dead: release(ptr))
    return result

# interfaces

class ITypeLib(IUnknown):
    _iid_ = GUID("{00020402-0000-0000-C000-000000000046}")

    # Commented out methods use the default implementation that comtypes
    # automatically creates for COM methods.

##    def GetTypeInfoCount(self):
##        "Return the number of type informations"

##    def GetTypeInfo(self, index):
##        "Load type info by index"

##    def GetTypeInfoType(self, index):
##        "Return the TYPEKIND of type information"

##    def GetTypeInfoOfGuid(self, guid):
##        "Return type information for a guid"

    def GetLibAttr(self):
        "Return type library attributes"
        return _deref_with_release(self._GetLibAttr(), self.ReleaseTLibAttr)

##    def GetTypeComp(self):
##        "Return an ITypeComp pointer."

##    def GetDocumentation(self, index):
##        "Return documentation for a type description."

    def IsName(self, name, lHashVal=0):
        """Check if there is type information for this name.

        Returns the name with capitalization found in the type
        library, or None.
        """
        from ctypes import create_unicode_buffer
        namebuf = create_unicode_buffer(name)
        found = BOOL()
        self.__com_IsName(namebuf, lHashVal, byref(found))
        if found.value:
            return namebuf[:].split("\0", 1)[0]
        return None

    def FindName(self, name, lHashVal=0):
        # Hm...
        # Could search for more than one name - should we support this?
        found = c_ushort(1)
        tinfo = POINTER(ITypeInfo)()
        memid = MEMBERID()
        self.__com_FindName(name, lHashVal, byref(tinfo), byref(memid), byref(found))
        if found.value:
            return memid.value, tinfo
        return None

##    def ReleaseTLibAttr(self, ptla):
##        "Release TLIBATTR"

################

def fix_name(name):
    # Some typelibs contain BSTR with embedded NUL characters,
    # probably the len of the BSTR is wrong.
    if name is None:
        return name
    return name.split("\0")[0]

class ITypeInfo(IUnknown):
    _iid_ = GUID("{00020401-0000-0000-C000-000000000046}")

    def GetTypeAttr(self):
        "Return the TYPEATTR for this type"
        return _deref_with_release(self._GetTypeAttr(), self.ReleaseTypeAttr)

##    def GetTypeComp(self):
##        "Return ITypeComp pointer for this type"

    def GetDocumentation(self, memid):
        """Return name, docstring, helpcontext, and helpfile for 'memid'."""
        name, doc, helpcontext, helpfile = self._GetDocumentation(memid)
        return fix_name(name), fix_name(doc), helpcontext, fix_name(helpfile)

    def GetFuncDesc(self, index):
        "Return FUNCDESC for index"
        return _deref_with_release(self._GetFuncDesc(index), self.ReleaseFuncDesc)

    def GetVarDesc(self, index):
        "Return VARDESC for index"
        return _deref_with_release(self._GetVarDesc(index), self.ReleaseVarDesc)

    def GetNames(self, memid, count=1):
        "Return names for memid"
        names = (BSTR * count)()
        cnames = c_uint()
        self.__com_GetNames(memid, names, count, byref(cnames))
        return names[:cnames.value]

##    def GetRefTypeOfImplType(self, index):
##        "Get the reftype of an implemented type"

##    def GetImplTypeFlags(self, index):
##        "Get IMPLTYPEFLAGS"

    def GetIDsOfNames(self, *names):
        "Maps function and argument names to identifiers"
        rgsznames = (c_wchar_p * len(names))(*names)
        ids = (MEMBERID * len(names))()
        self.__com_GetIDsOfNames(rgsznames, len(names), ids)
        return ids[:]


    # not yet wrapped
##    STDMETHOD(HRESULT, 'Invoke', [PVOID, MEMBERID, WORD, POINTER(DISPPARAMS), POINTER(VARIANT), POINTER(EXCEPINFO), POINTER(UINT)]),

##    def GetDllEntry(self, memid, invkind):
##        "Return the dll name, function name, and ordinal for a function and invkind."

##    def GetRefTypeInfo(self, href):
##        "Get type info for reftype"

    def AddressOfMember(self, memid, invkind):
        "Get the address of a function in a dll"
        raise "Check Me"
        p = c_void_p()
        self.__com_AddressOfMember(memid, invkind, byref(p))
        # XXX Would the default impl return the value of p?
        return p.value

    def CreateInstance(self, punkouter=None, interface=IUnknown, iid=None):
        if iid is None:
            iid = interface._iid_
        return self._CreateInstance(punkouter, byref(interface._iid_))

##    def GetMops(self, index):
##        "Get marshalling opcodes (whatever that is...)"

##    def GetContainingTypeLib(self):
##        "Return index into and the containing type lib itself"

##    def ReleaseTypeAttr(self, pta):

##    def ReleaseFuncDesc(self, pfd):

##    def ReleaseVarDesc(self, pvd):

################

class ITypeComp(IUnknown):
    _iid_ = GUID("{00020403-0000-0000-C000-000000000046}")

    def Bind(self, name, flags=0, lHashVal=0):
        "Bind to a name"
        bindptr = BINDPTR()
        desckind = DESCKIND()
        ti = POINTER(ITypeInfo)()
        self.__com_Bind(name, lHashVal, flags, byref(ti), byref(desckind), byref(bindptr))
        kind = desckind.value
        if kind == DESCKIND_FUNCDESC:
            fd = bindptr.lpfuncdesc[0]
            fd.__ref__ = weakref.ref(fd, lambda dead: ti.ReleaseFuncDesc(bindptr.lpfuncdesc))
            return "function", fd
        elif kind == DESCKIND_VARDESC:
            vd = bindptr.lpvardesc[0]
            vd.__ref__ = weakref.ref(vd, lambda dead: ti.ReleaseVarDesc(bindptr.lpvardesc))
            return "variable", vd
        elif kind == DESCKIND_TYPECOMP:
            return "type", bindptr.lptcomp
        elif kind == DESCKIND_IMPLICITAPPOBJ:
            raise NotImplementedError
        elif kind == DESCKIND_NONE:
            raise NameError("Name %s not found" % name)

    def BindType(self, name, lHashVal=0):
        "Bind a type, and return both the typeinfo and typecomp for it."
        ti = POINTER(ITypeInfo)()
        tc = POINTER(ITypeComp)()
        self.__com_BindType(name, lHashVal, byref(ti), byref(tc))
        return ti, tc


################

class ICreateTypeLib(IUnknown):
    _iid_ = GUID("{00020406-0000-0000-C000-000000000046}")
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 2149

class ICreateTypeLib2(ICreateTypeLib):
    _iid_ = GUID("{0002040F-0000-0000-C000-000000000046}")

class ICreateTypeInfo(IUnknown):
    _iid_ = GUID("{00020405-0000-0000-C000-000000000046}")
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 915

    def SetFuncAndParamNames(self, index, *names):
        rgszNames = (c_wchar_p * len(names))()
        for i, n in enumerate(names):
            rgszNames[i] = n
        return self._SetFuncAndParamNames(index, rgszNames, len(names))

class IRecordInfo(IUnknown):
    # C:/vc98/include/OAIDL.H 5974
    _iid_ = GUID("{0000002F-0000-0000-C000-000000000046}")

    def GetFieldNames(self, *args):
        count = c_ulong()
        self.__com_GetFieldNames(count, None)
        array = (BSTR * count.value)()
        self.__com_GetFieldNames(count, array)
        result = array[:]
        # XXX Should SysFreeString the array contents. How to?
        return result

IRecordInfo. _methods_ = [
        COMMETHOD([], HRESULT, 'RecordInit',
                  (['in'], c_void_p, 'pvNew')),
        COMMETHOD([], HRESULT, 'RecordClear',
                  (['in'], c_void_p, 'pvExisting')),
        COMMETHOD([], HRESULT, 'RecordCopy',
                  (['in'], c_void_p, 'pvExisting'),
                  (['in'], c_void_p, 'pvNew')),
        COMMETHOD([], HRESULT, 'GetGuid',
                  (['out'], POINTER(GUID), 'pguid')),
        COMMETHOD([], HRESULT, 'GetName',
                  (['out'], POINTER(BSTR), 'pbstrName')),
        COMMETHOD([], HRESULT, 'GetSize',
                  (['out'], POINTER(c_ulong), 'pcbSize')),
        COMMETHOD([], HRESULT, 'GetTypeInfo',
                  (['out'], POINTER(POINTER(ITypeInfo)), 'ppTypeInfo')),
        COMMETHOD([], HRESULT, 'GetField',
                  (['in'], c_void_p, 'pvData'),
                  (['in'], c_wchar_p, 'szFieldName'),
                  (['out'], POINTER(VARIANT), 'pvarField')),
        COMMETHOD([], HRESULT, 'GetFieldNoCopy',
                  (['in'], c_void_p, 'pvData'),
                  (['in'], c_wchar_p, 'szFieldName'),
                  (['out'], POINTER(VARIANT), 'pvarField'),
                  (['out'], POINTER(c_void_p), 'ppvDataCArray')),
        COMMETHOD([], HRESULT, 'PutField',
                  (['in'], c_ulong, 'wFlags'),
                  (['in'], c_void_p, 'pvData'),
                  (['in'], c_wchar_p, 'szFieldName'),
                  (['in'], POINTER(VARIANT), 'pvarField')),
        COMMETHOD([], HRESULT, 'PutFieldNoCopy',
                  (['in'], c_ulong, 'wFlags'),
                  (['in'], c_void_p, 'pvData'),
                  (['in'], c_wchar_p, 'szFieldName'),
                  (['in'], POINTER(VARIANT), 'pvarField')),
        COMMETHOD([], HRESULT, 'GetFieldNames',
                  (['in', 'out'], POINTER(c_ulong), 'pcNames'),
                  (['in'], POINTER(BSTR), 'rgBstrNames')),
        COMMETHOD([], BOOL, 'IsMatchingType',
                  (['in'], POINTER(IRecordInfo))),
        COMMETHOD([], HRESULT, 'RecordCreate'),
        COMMETHOD([], HRESULT, 'RecordCreateCopy',
                  (['in'], c_void_p, 'pvSource'),
                  (['out'], POINTER(c_void_p), 'ppvDest')),
        COMMETHOD([], HRESULT, 'RecordDestroy',
                  (['in'], c_void_p, 'pvRecord'))]



################################################################
# functions
_oleaut32 = oledll.oleaut32

def GetRecordInfoFromTypeInfo(tinfo):
    "Return an IRecordInfo pointer to the UDT described in tinfo"
    ri = POINTER(IRecordInfo)()
    _oleaut32.GetRecordInfoFromTypeInfo(tinfo, byref(ri))
    return ri

def GetRecordInfoFromGuids(rGuidTypeLib, verMajor, verMinor, lcid, rGuidTypeInfo):
    ri = POINTER(IRecordInfo)()
    _oleaut32.GetRecordInfoFromGuids(byref(GUID(rGuidTypeLib)),
                                     verMajor, verMinor, lcid,
                                     byref(GUID(rGuidTypeInfo)),
                                     byref(ri))
    return ri

def LoadRegTypeLib(guid, wMajorVerNum, wMinorVerNum, lcid=0):
    "Load a registered type library"
    tlib = POINTER(ITypeLib)()
    _oleaut32.LoadRegTypeLib(byref(GUID(guid)), wMajorVerNum, wMinorVerNum, lcid, byref(tlib))
    return tlib

if hasattr(_oleaut32, "LoadTypeLibEx"):
    def LoadTypeLibEx(szFile, regkind=REGKIND_NONE):
        "Load, and optionally register a type library file"
        ptl = POINTER(ITypeLib)()
        _oleaut32.LoadTypeLibEx(c_wchar_p(szFile), regkind, byref(ptl))
        return ptl
else:
    def LoadTypeLibEx(szFile, regkind=REGKIND_NONE):
        "Load, and optionally register a type library file"
        ptl = POINTER(ITypeLib)()
        _oleaut32.LoadTypeLib(c_wchar_p(szFile), byref(ptl))
        return ptl

def LoadTypeLib(szFile):
    "Load and register a type library file"
    tlib = POINTER(ITypeLib)()
    _oleaut32.LoadTypeLib(c_wchar_p(szFile), byref(tlib))
    return tlib

def UnRegisterTypeLib(libID, wVerMajor, wVerMinor, lcid=0, syskind=SYS_WIN32):
    "Unregister a registered type library"
    return _oleaut32.UnRegisterTypeLib(byref(GUID(libID)), wVerMajor, wVerMinor, lcid, syskind)

def RegisterTypeLib(tlib, fullpath, helpdir=None):
    "Register a type library in the registry"
    return _oleaut32.RegisterTypeLib(tlib, c_wchar_p(fullpath), c_wchar_p(helpdir))

def CreateTypeLib(filename, syskind=SYS_WIN32):
    "Return a ICreateTypeLib2 pointer"
    ctlib = POINTER(ICreateTypeLib2)()
    _oleaut32.CreateTypeLib2(syskind, c_wchar_p(filename), byref(ctlib))
    return ctlib

def QueryPathOfRegTypeLib(libid, wVerMajor, wVerMinor, lcid=0):
    "Return the path of a registered type library"
    pathname = BSTR()
    _oleaut32.QueryPathOfRegTypeLib(byref(GUID(libid)), wVerMajor, wVerMinor, lcid, byref(pathname))
    return pathname.value.split("\0")[0]

################################################################
# Structures

class tagTLIBATTR(Structure):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 4437
    def __repr__(self):
        return "TLIBATTR(GUID=%s, Version=%s.%s, LCID=%s, FLags=0x%x)" % \
               (self.guid, self.wMajorVerNum, self.wMinorVerNum, self.lcid, self.wLibFlags)
TLIBATTR = tagTLIBATTR

class tagTYPEATTR(Structure):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 672
    def __repr__(self):
        return "TYPEATTR(GUID=%s, typekind=%s, funcs=%s, vars=%s, impltypes=%s)" % \
               (self.guid, self.typekind, self.cFuncs, self.cVars, self.cImplTypes)
TYPEATTR = tagTYPEATTR

class tagFUNCDESC(Structure):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 769
    def __repr__(self):
        return "FUNCDESC(memid=%s, cParams=%s, cParamsOpt=%s, callconv=%s, invkind=%s, funckind=%s)" % \
               (self.memid, self.cParams, self.cParamsOpt, self.callconv, self.invkind, self.funckind)


FUNCDESC = tagFUNCDESC
class tagVARDESC(Structure):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 803
    pass
VARDESC = tagVARDESC

class tagBINDPTR(Union):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 3075
    pass
BINDPTR = tagBINDPTR
class tagTYPEDESC(Structure):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 582
    pass
TYPEDESC = tagTYPEDESC
class tagIDLDESC(Structure):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 633
    pass
IDLDESC = tagIDLDESC

class tagARRAYDESC(Structure):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 594
    pass

################################################################
# interface vtbl definitions

ICreateTypeLib._methods_ = [
# C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 2149
    COMMETHOD([], HRESULT, 'CreateTypeInfo',
              (['in'], LPOLESTR, 'szName'),
              (['in'], TYPEKIND, 'tkind'),
              (['out'], POINTER(POINTER(ICreateTypeInfo)), 'ppCTInfo')),
    STDMETHOD(HRESULT, 'SetName', [LPOLESTR]),
    STDMETHOD(HRESULT, 'SetVersion', [WORD, WORD]),
    STDMETHOD(HRESULT, 'SetGuid', [POINTER(GUID)]),
    STDMETHOD(HRESULT, 'SetDocString', [LPOLESTR]),
    STDMETHOD(HRESULT, 'SetHelpFileName', [LPOLESTR]),
    STDMETHOD(HRESULT, 'SetHelpContext', [DWORD]),
    STDMETHOD(HRESULT, 'SetLcid', [LCID]),
    STDMETHOD(HRESULT, 'SetLibFlags', [UINT]),
    STDMETHOD(HRESULT, 'SaveAllChanges', []),
]

ICreateTypeLib2._methods_ = [
# C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 2444
    STDMETHOD(HRESULT, 'DeleteTypeInfo', [POINTER(ITypeInfo)]),
    STDMETHOD(HRESULT, 'SetCustData', [POINTER(GUID), POINTER(VARIANT)]),
    STDMETHOD(HRESULT, 'SetHelpStringContext', [ULONG]),
    STDMETHOD(HRESULT, 'SetHelpStringDll', [LPOLESTR]),
    ]

ITypeLib._methods_ = [
# C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 4455
    COMMETHOD([], UINT, 'GetTypeInfoCount'),
    COMMETHOD([], HRESULT, 'GetTypeInfo',
              (['in'], UINT, 'index'),
              (['out'], POINTER(POINTER(ITypeInfo)))),
    COMMETHOD([], HRESULT, 'GetTypeInfoType',
              (['in'], UINT, 'index'),
              (['out'], POINTER(TYPEKIND))),
    COMMETHOD([], HRESULT, 'GetTypeInfoOfGuid',
              (['in'], POINTER(GUID)),
              (['out'], POINTER(POINTER(ITypeInfo)))),
    COMMETHOD([], HRESULT, 'GetLibAttr',
              (['out'], POINTER(POINTER(TLIBATTR)))),
    COMMETHOD([], HRESULT, 'GetTypeComp',
              (['out'], POINTER(POINTER(ITypeComp)))),
    COMMETHOD([], HRESULT, 'GetDocumentation',
              (['in'], INT, 'index'),
              (['out'], POINTER(BSTR)),
              (['out'], POINTER(BSTR)),
              (['out'], POINTER(DWORD)),
              (['out'], POINTER(BSTR))),
    COMMETHOD([], HRESULT, 'IsName',
              # IsName changes the casing of the passed in name to
              # match that in the type library.  In the automatically
              # wrapped version of this method, ctypes would pass a
              # Python unicode string which would then be changed -
              # very bad.  So we have (see above) to implement the
              # IsName method manually.
              (['in', 'out'], LPOLESTR, 'name'),
              (['in', 'optional'], DWORD, 'lHashVal', 0),
              (['out'], POINTER(BOOL))),
    STDMETHOD(HRESULT, 'FindName', [LPOLESTR, DWORD, POINTER(POINTER(ITypeInfo)),
                                    POINTER(MEMBERID), POINTER(USHORT)]),
    COMMETHOD([], None, 'ReleaseTLibAttr',
              (['in'], POINTER(TLIBATTR)))
]

ITypeInfo._methods_ = [
# C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 3230
    COMMETHOD([], HRESULT, 'GetTypeAttr',
              (['out'], POINTER(POINTER(TYPEATTR)), 'ppTypeAttr')),
    COMMETHOD([], HRESULT, 'GetTypeComp',
              (['out'], POINTER(POINTER(ITypeComp)))),
    COMMETHOD([], HRESULT, 'GetFuncDesc',
              (['in'], UINT, 'index'),
              (['out'], POINTER(POINTER(FUNCDESC)))),
    COMMETHOD([], HRESULT, 'GetVarDesc',
              (['in'], UINT, 'index'),
              (['out'], POINTER(POINTER(VARDESC)))),
    STDMETHOD(HRESULT, 'GetNames', [MEMBERID, POINTER(BSTR), UINT, POINTER(UINT)]),
    COMMETHOD([], HRESULT, 'GetRefTypeOfImplType',
              (['in'], UINT, 'index'),
              (['out'], POINTER(HREFTYPE))),
    COMMETHOD([], HRESULT, 'GetImplTypeFlags',
              (['in'], UINT, 'index'),
              (['out'], POINTER(INT))),
##    STDMETHOD(HRESULT, 'GetIDsOfNames', [POINTER(LPOLESTR), UINT, POINTER(MEMBERID)]),
    # this one changed, to accept c_wchar_p array
    STDMETHOD(HRESULT, 'GetIDsOfNames', [POINTER(c_wchar_p), UINT, POINTER(MEMBERID)]),
    STDMETHOD(HRESULT, 'Invoke', [PVOID, MEMBERID, WORD, POINTER(DISPPARAMS), POINTER(VARIANT), POINTER(EXCEPINFO), POINTER(UINT)]),

    COMMETHOD([], HRESULT, 'GetDocumentation',
              (['in'], MEMBERID, 'memid'),
              (['out'], POINTER(BSTR), 'pBstrName'),
              (['out'], POINTER(BSTR), 'pBstrDocString'),
              (['out'], POINTER(DWORD), 'pdwHelpContext'),
              (['out'], POINTER(BSTR), 'pBstrHelpFile')),
    COMMETHOD([], HRESULT, 'GetDllEntry',
              (['in'], MEMBERID, 'index'),
              (['in'], INVOKEKIND, 'invkind'),
              (['out'], POINTER(BSTR), 'pBstrDllName'),
              (['out'], POINTER(BSTR), 'pBstrName'),
              (['out'], POINTER(WORD), 'pwOrdinal')),
    COMMETHOD([], HRESULT, 'GetRefTypeInfo',
              (['in'], HREFTYPE, 'hRefType'),
              (['out'], POINTER(POINTER(ITypeInfo)))),
    STDMETHOD(HRESULT, 'AddressOfMember', [MEMBERID, INVOKEKIND, POINTER(PVOID)]),
    COMMETHOD([], HRESULT, 'CreateInstance',
              (['in'], POINTER(IUnknown), 'pUnkOuter'),
              (['in'], POINTER(IID), 'refiid'),
              (['out'], POINTER(POINTER(IUnknown)))),
    COMMETHOD([], HRESULT, 'GetMops',
              (['in'], MEMBERID, 'memid'),
              (['out'], POINTER(BSTR))),
    COMMETHOD([], HRESULT, 'GetContainingTypeLib',
              (['out'], POINTER(POINTER(ITypeLib))),
              (['out'], POINTER(UINT))),
    COMMETHOD([], None, 'ReleaseTypeAttr',
              (['in'], POINTER(TYPEATTR))),
    COMMETHOD([], None, 'ReleaseFuncDesc',
              (['in'], POINTER(FUNCDESC))),
    COMMETHOD([], None, 'ReleaseVarDesc',
              (['in'], POINTER(VARDESC))),
]

ITypeComp._methods_ = [
# C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 3090
    STDMETHOD(HRESULT, 'Bind',
              [LPOLESTR, DWORD, WORD, POINTER(POINTER(ITypeInfo)),
               POINTER(DESCKIND), POINTER(BINDPTR)]),
    STDMETHOD(HRESULT, 'BindType',
              [LPOLESTR, DWORD, POINTER(POINTER(ITypeInfo)), POINTER(POINTER(ITypeComp))]),
]

ICreateTypeInfo._methods_ = [
# C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 915
    STDMETHOD(HRESULT, 'SetGuid', [POINTER(GUID)]),
    STDMETHOD(HRESULT, 'SetTypeFlags', [UINT]),
    STDMETHOD(HRESULT, 'SetDocString', [LPOLESTR]),
    STDMETHOD(HRESULT, 'SetHelpContext', [DWORD]),
    STDMETHOD(HRESULT, 'SetVersion', [WORD, WORD]),
#    STDMETHOD(HRESULT, 'AddRefTypeInfo', [POINTER(ITypeInfo), POINTER(HREFTYPE)]),
    COMMETHOD([], HRESULT, 'AddRefTypeInfo',
              (['in'], POINTER(ITypeInfo)),
              (['out'], POINTER(HREFTYPE))),
    STDMETHOD(HRESULT, 'AddFuncDesc', [UINT, POINTER(FUNCDESC)]),
    STDMETHOD(HRESULT, 'AddImplType', [UINT, HREFTYPE]),
    STDMETHOD(HRESULT, 'SetImplTypeFlags', [UINT, INT]),
    STDMETHOD(HRESULT, 'SetAlignment', [WORD]),
    STDMETHOD(HRESULT, 'SetSchema', [LPOLESTR]),
    STDMETHOD(HRESULT, 'AddVarDesc', [UINT, POINTER(VARDESC)]),
    STDMETHOD(HRESULT, 'SetFuncAndParamNames', [UINT, POINTER(c_wchar_p), UINT]),
    STDMETHOD(HRESULT, 'SetVarName', [UINT, LPOLESTR]),
    STDMETHOD(HRESULT, 'SetTypeDescAlias', [POINTER(TYPEDESC)]),
    STDMETHOD(HRESULT, 'DefineFuncAsDllEntry', [UINT, LPOLESTR, LPOLESTR]),
    STDMETHOD(HRESULT, 'SetFuncDocString', [UINT, LPOLESTR]),
    STDMETHOD(HRESULT, 'SetVarDocString', [UINT, LPOLESTR]),
    STDMETHOD(HRESULT, 'SetFuncHelpContext', [UINT, DWORD]),
    STDMETHOD(HRESULT, 'SetVarHelpContext', [UINT, DWORD]),
    STDMETHOD(HRESULT, 'SetMops', [UINT, BSTR]),
    STDMETHOD(HRESULT, 'SetTypeIdldesc', [POINTER(IDLDESC)]),
    STDMETHOD(HRESULT, 'LayOut', []),
]

class IProvideClassInfo(IUnknown):
    _iid_ = GUID("{B196B283-BAB4-101A-B69C-00AA00341D07}")
    _methods_ = [
        # Returns the ITypeInfo interface for the object's coclass type information.
        COMMETHOD([], HRESULT, "GetClassInfo",
                  ( ['out'],  POINTER(POINTER(ITypeInfo)), "ppTI" ) )
        ]

class IProvideClassInfo2(IProvideClassInfo):
    _iid_ = GUID("{A6BC3AC0-DBAA-11CE-9DE3-00AA004BB851}")
    _methods_ = [
        # Returns the GUID for the object's outgoing IID for its default event set.
        COMMETHOD([], HRESULT, "GetGUID",
                  ( ['in'], DWORD, "dwGuidKind" ),
                  ( ['out', 'retval'], POINTER(GUID), "pGUID" ))
        ]


################################################################
# Structure fields

tagTLIBATTR._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 4437
    ('guid', GUID),
    ('lcid', LCID),
    ('syskind', SYSKIND),
    ('wMajorVerNum', WORD),
    ('wMinorVerNum', WORD),
    ('wLibFlags', WORD),
]
class N11tagTYPEDESC5DOLLAR_203E(Union):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 584
    pass
N11tagTYPEDESC5DOLLAR_203E._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 584
    ('lptdesc', POINTER(tagTYPEDESC)),
    ('lpadesc', POINTER(tagARRAYDESC)),
    ('hreftype', HREFTYPE),
]
tagTYPEDESC._anonymous_ = ('_',)
tagTYPEDESC._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 582
    # Unnamed field renamed to '_'
    ('_', N11tagTYPEDESC5DOLLAR_203E),
    ('vt', VARTYPE),
]
tagIDLDESC._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 633
    ('dwReserved', ULONG_PTR),
    ('wIDLFlags', USHORT),
]
tagTYPEATTR._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 672
    ('guid', GUID),
    ('lcid', LCID),
    ('dwReserved', DWORD),
    ('memidConstructor', MEMBERID),
    ('memidDestructor', MEMBERID),
    ('lpstrSchema', LPOLESTR),
    ('cbSizeInstance', DWORD),
    ('typekind', TYPEKIND),
    ('cFuncs', WORD),
    ('cVars', WORD),
    ('cImplTypes', WORD),
    ('cbSizeVft', WORD),
    ('cbAlignment', WORD),
    ('wTypeFlags', WORD),
    ('wMajorVerNum', WORD),
    ('wMinorVerNum', WORD),
    ('tdescAlias', TYPEDESC),
    ('idldescType', IDLDESC),
]
class N10tagVARDESC5DOLLAR_205E(Union):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 807
    pass
N10tagVARDESC5DOLLAR_205E._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 807
    ('oInst', DWORD),
    ('lpvarValue', POINTER(VARIANT)),
]
class tagELEMDESC(Structure):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 661
    pass
class N11tagELEMDESC5DOLLAR_204E(Union):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 663
    pass

class tagPARAMDESC(Structure):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 609
    pass

class tagPARAMDESCEX(Structure):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 601
    pass
LPPARAMDESCEX = POINTER(tagPARAMDESCEX)

tagPARAMDESC._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 609
    ('pparamdescex', LPPARAMDESCEX),
    ('wParamFlags', USHORT),
]
PARAMDESC = tagPARAMDESC

N11tagELEMDESC5DOLLAR_204E._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 663
    ('idldesc', IDLDESC),
    ('paramdesc', PARAMDESC),
]
tagELEMDESC._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 661
    ('tdesc', TYPEDESC),
    # Unnamed field renamed to '_'
    ('_', N11tagELEMDESC5DOLLAR_204E),
]
ELEMDESC = tagELEMDESC

tagVARDESC._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 803
    ('memid', MEMBERID),
    ('lpstrSchema', LPOLESTR),
    # Unnamed field renamed to '_'
    ('_', N10tagVARDESC5DOLLAR_205E),
    ('elemdescVar', ELEMDESC),
    ('wVarFlags', WORD),
    ('varkind', VARKIND),
]
tagBINDPTR._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 3075
    ('lpfuncdesc', POINTER(FUNCDESC)),
    ('lpvardesc', POINTER(VARDESC)),
    ('lptcomp', POINTER(ITypeComp)),
]

tagFUNCDESC._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 769
    ('memid', MEMBERID),
    ('lprgscode', POINTER(SCODE)),
    ('lprgelemdescParam', POINTER(ELEMDESC)),
    ('funckind', FUNCKIND),
    ('invkind', INVOKEKIND),
    ('callconv', CALLCONV),
    ('cParams', SHORT),
    ('cParamsOpt', SHORT),
    ('oVft', SHORT),
    ('cScodes', SHORT),
    ('elemdescFunc', ELEMDESC),
    ('wFuncFlags', WORD),
]

tagPARAMDESCEX._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 601
    ('cBytes', DWORD),
    ('varDefaultValue', VARIANTARG),
]

class tagSAFEARRAYBOUND(Structure):
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 226
    _fields_ = [
        ('cElements', DWORD),
        ('lLbound', LONG),
    ]
SAFEARRAYBOUND = tagSAFEARRAYBOUND

tagARRAYDESC._fields_ = [
    # C:/Programme/gccxml/bin/Vc71/PlatformSDK/oaidl.h 594
    ('tdescElem', TYPEDESC),
    ('cDims', USHORT),
    ('rgbounds', SAFEARRAYBOUND * 1),
]
