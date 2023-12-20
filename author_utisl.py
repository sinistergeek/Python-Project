import ctypes as ctypes
from ctypes import wintypes as wintypes
import os
import sys

kernel32 = ctypes.WinDLL('kernel32',use_last_error=True)
advapi32 = ctypes.WinDLL('advapi32',use_last_error=True)
ERROR_INVALID_FUNCTION =  0x0001
ERROR_FILE_NOT_FOUND = 0x0002
ERROR_PATH_NOT_FOUND = 0x0003
ERROR_ACCESS_DENIED = 0x0005
ERROR_SHARING_VIOLATION = 0x0020
SE_FILE_OBJECT = 1
OWNER_SECURITY_INFORMATION = 0x00000001
GROUP_SECURITY_INFORMATION = 0x00000002
DACL_SECURITY_INFORMATION = 0x00000004
SACL_SECURITY_INFORMATION = 0x00000008
LABEL_SECURITY_InfORMATION = 0x0000010

_DEFAULT_SECURITY_INFORMATION =(OWNER_SECURITY_INFORMATION|GROUP_SECURITY_INFORMATION|DACL_SECURITY_INFORMATION|LABEL_SECURITY_INFORMATION)
LPDWORD =ctypes.POINTER(wintypes.DWORD)
SE_OBJECT_TYPE =wintypes.DWORD
SECURITY_INFORMAtIOn =wintypes.DWORD
class SID_NAME_USE(wintypes.DWORD):
    _sid_types = dict(enumerate("User Group DOmain Alias WellKnownGroup DeletedAccount Invalid Unknown Computer Label".split(),1))
    def __init(self,value=None):
        if value is not None:
            if value not in self.side_types:
                raise ValueError('invalid SID type')
            wintypes.DWORD.__init__(value)
