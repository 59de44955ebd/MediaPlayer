''' minimal script for handling .LNK files in Windows '''

__all__ = ["get_lnk_target_path"]

from dshow.comtypes import GUID, CreateObject
from dshow.lib import IDispatch, COMMETHOD, HRESULT, BSTR, POINTER

class IWshShell(IDispatch):
    """Shell Object Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{F935DC21-1CF0-11D0-ADB9-00C04FD58A0B}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

class IWshShortcut(IDispatch):
    """Shortcut Object"""
    _case_insensitive_ = True
    _iid_ = GUID('{F935DC23-1CF0-11D0-ADB9-00C04FD58A0B}')
    _idlflags_ = ['dual', 'oleautomation']

IWshShell._methods_ = [COMMETHOD([], HRESULT, '_')] * 4 + [
    COMMETHOD([], HRESULT, 'CreateShortcut',
        (['in'], BSTR, 'PathLink'),
        (['out', 'retval'], POINTER(POINTER(IDispatch)), 'out_Shortcut')
    ),
]

IWshShortcut._methods_ = [COMMETHOD([], HRESULT, '_')] * 10 + [
    COMMETHOD(['propget'], HRESULT, 'TargetPath', (['out', 'retval'], POINTER(BSTR), 'out_Path')),
]

def get_lnk_target_path(lnk_path):
    shortcut = CreateObject("WScript.Shell", interface=IWshShell).CreateShortCut(lnk_path)
    return shortcut.QueryInterface(IWshShortcut).TargetPath
