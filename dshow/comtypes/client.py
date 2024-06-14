import dshow.comtypes
import dshow.comtypes.dynamic

import logging
logger = logging.getLogger(__name__)


__all__ = ["CreateObject", "GetBestInterface"]


def wrap_outparam(punk):
    logger.debug("wrap_outparam(%s)", punk)
    if not punk:
        return None
    if punk.__com_interface__ == dshow.comtypes.automation.IDispatch:
        return GetBestInterface(punk)
    return punk

def GetBestInterface(punk):
    """Try to QueryInterface a COM pointer to the 'most useful'
    interface.

    Get type information for the provided object, either via
    IDispatch.GetTypeInfo(), or via IProvideClassInfo.GetClassInfo().
    Generate a wrapper module for the typelib, and QI for the
    interface found.
    """
    if not punk: # NULL COM pointer
        return punk # or should we return None?
    # find the typelib and the interface name
    logger.debug("GetBestInterface(%s)", punk)
    try:
        try:
            pci = punk.QueryInterface(dshow.comtypes.typeinfo.IProvideClassInfo)
            logger.debug("Does implement IProvideClassInfo")
        except dshow.comtypes.COMError:
            # Some COM objects support IProvideClassInfo2, but not IProvideClassInfo.
            # These objects are broken, but we support them anyway.
            logger.debug("Does NOT implement IProvideClassInfo, trying IProvideClassInfo2")
            pci = punk.QueryInterface(dshow.comtypes.typeinfo.IProvideClassInfo2)
            logger.debug("Does implement IProvideClassInfo2")
        tinfo = pci.GetClassInfo() # TypeInfo for the CoClass
        # find the interface marked as default
        ta = tinfo.GetTypeAttr()
        for index in range(ta.cImplTypes):
            if tinfo.GetImplTypeFlags(index) == 1:
                break
        else:
            if ta.cImplTypes != 1:
                # Hm, should we use dynamic now?
                raise TypeError("No default interface found")
            # Only one interface implemented, use that (even if
            # not marked as default).
            index = 0
        href = tinfo.GetRefTypeOfImplType(index)
        tinfo = tinfo.GetRefTypeInfo(href)
    except dshow.comtypes.COMError:
        logger.debug("Does NOT implement IProvideClassInfo/IProvideClassInfo2")
        try:
            pdisp = punk.QueryInterface(dshow.comtypes.automation.IDispatch)
        except dshow.comtypes.COMError:
            logger.debug("No Dispatch interface: %s", punk)
            return punk
        try:
            tinfo = pdisp.GetTypeInfo(0)
        except dshow.comtypes.COMError:
            pdisp = dshow.comtypes.client.dynamic.Dispatch(pdisp)
            logger.debug("IDispatch.GetTypeInfo(0) failed: %s" % pdisp)
            return pdisp

    typeattr = tinfo.GetTypeAttr()
    logger.debug("Default interface is %s", typeattr.guid)
    try:
        punk.QueryInterface(dshow.comtypes.IUnknown, typeattr.guid)
    except dshow.comtypes.COMError:
        logger.debug("Does not implement default interface, returning dynamic object")
        #return dshow.comtypes.client.dynamic.Dispatch(punk)
        return dshow.comtypes.dynamic.Dispatch(punk)

    itf_name = tinfo.GetDocumentation(-1)[0] # interface name
    tlib = tinfo.GetContainingTypeLib()[0] # typelib

    # import the wrapper, generating it on demand
    mod = GetModule(tlib)
    # Python interface class
    interface = getattr(mod, itf_name)
    logger.debug("Implements default interface from typeinfo %s", interface)
    # QI for this interface
    # XXX
    # What to do if this fails?
    # In the following example the engine.Eval() call returns
    # such an object.
    #
    # engine = CreateObject("MsScriptControl.ScriptControl")
    # engine.Language = "JScript"
    # engine.Eval("[1, 2, 3]")
    #
    # Could the above code, as an optimization, check that QI works,
    # *before* generating the wrapper module?
    result = punk.QueryInterface(interface)
    logger.debug("Final result is %s", result)
    return result

def _manage(obj, clsid, interface):
    obj.__dict__['__clsid'] = str(clsid)
    if interface is None:
        obj = GetBestInterface(obj)
    return obj

#def GetClassObject(progid,
#                   clsctx=None,
#                   pServerInfo=None,
#                   interface=None):
#    """Create and return the class factory for a COM object.
#
#    'clsctx' specifies how to create the object, use the CLSCTX_... constants.
#    'pServerInfo', if used, must be a pointer to a comtypes.COSERVERINFO instance
#    'interface' may be used to request an interface other than IClassFactory
#    """
#    clsid = dshow.comtypes.GUID.from_progid(progid)
#    return dshow.comtypes.CoGetClassObject(clsid,
#                                     clsctx, pServerInfo, interface)

def CreateObject(progid,                  # which object to create
                 clsctx=None,             # how to create the object
                 machine=None,            # where to create the object
                 interface=None,          # the interface we want
                 dynamic=False,           # use dynamic dispatch
                 pServerInfo=None):       # server info struct for remoting
    """Create a COM object from 'progid', and try to QueryInterface()
    it to the most useful interface, generating typelib support on
    demand.  A pointer to this interface is returned.

    'progid' may be a string like "InternetExplorer.Application",
       a string specifying a clsid, a GUID instance, or an object with
       a _clsid_ attribute which should be any of the above.
    'clsctx' specifies how to create the object, use the CLSCTX_... constants.
    'machine' allows to specify a remote machine to create the object on.
    'interface' allows to force a certain interface
    'dynamic=True' will return a dynamic dispatch object
    'pServerInfo', if used, must be a pointer to a comtypes.COSERVERINFO instance
        This supercedes 'machine'.

    You can also later request to receive events with GetEvents().
    """
    clsid = dshow.comtypes.GUID.from_progid(progid)
    logger.debug("%s -> %s", progid, clsid)
    if dynamic:
        if interface:
            raise ValueError("interface and dynamic are mutually exclusive")
        interface = dshow.comtypes.automation.IDispatch
    elif interface is None:
        interface = getattr(progid, "_com_interfaces_", [None])[0]
    if machine is None and pServerInfo is None:
        logger.debug("CoCreateInstance(%s, clsctx=%s, interface=%s)",
                     clsid, clsctx, interface)
        obj = dshow.comtypes.CoCreateInstance(clsid, clsctx=clsctx, interface=interface)
    else:
        logger.debug("CoCreateInstanceEx(%s, clsctx=%s, interface=%s, machine=%s,\
                        pServerInfo=%s)",
                     clsid, clsctx, interface, machine, pServerInfo)
        if machine is not None and pServerInfo is not None:
            msg = "You can notset both the machine name and server info."
            raise ValueError(msg)
        obj = dshow.comtypes.CoCreateInstanceEx(clsid, clsctx=clsctx,
                interface=interface, machine=machine, pServerInfo=pServerInfo)
    if dynamic:
        return dshow.comtypes.client.dynamic.Dispatch(obj)
    return _manage(obj, clsid, interface=interface)
