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
