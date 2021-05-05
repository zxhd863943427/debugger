# coding=utf-8
'''
NAME:类型
author:zx弘
version：1.0
'''
'''
这是一堆python与Windows平台类型的对应表，为了防止出错，确保变量引用最小原则
'''

from ctypes import addressof
from ctypes import sizeof
from ctypes import POINTER
from ctypes import WINFUNCTYPE
from ctypes import windll
from ctypes import byref
from ctypes import c_void_p
from ctypes import c_char
from ctypes import c_char
from ctypes import c_wchar
from ctypes import c_ubyte
from ctypes import c_byte
from ctypes import c_ushort
from ctypes import c_short
from ctypes import c_uint
from ctypes import c_int
from ctypes import c_ulonglong
from ctypes import c_longlong
from ctypes import c_int8
from ctypes import c_uint8
from ctypes import c_char_p
from ctypes import c_wchar_p
from ctypes import c_float
from ctypes import c_double


addressof   = addressof
sizeof      = sizeof
SIZEOF      = sizeof
POINTER     = POINTER
WINFUNCTYPE = WINFUNCTYPE
windll      = windll


# 一些对应表，来自一份开源软件，根据版本做了部分修改
LPVOID      = c_void_p
CHAR        = c_char
WCHAR       = c_wchar
BYTE        = c_ubyte
SBYTE       = c_byte
WORD        = c_ushort
SWORD       = c_short
DWORD       = c_uint
SDWORD      = c_int
QWORD       = c_ulonglong
SQWORD      = c_longlong
SHORT       = c_short
USHORT      = c_ushort
INT         = c_int
UINT        = c_uint
LONG        = c_int
ULONG       = c_uint
LONGLONG    = c_longlong        # c_longlong
ULONGLONG   = c_ulonglong       # c_ulonglong
LPSTR       = c_char_p
LPWSTR      = c_wchar_p
INT8        = c_int8
INT16       = c_short
INT32       = c_int
INT64       = c_longlong
UINT8       = c_uint8
UINT16      = c_ushort
UINT32      = c_uint
UINT64      = c_ulonglong
LONG32      = c_int
LONG64      = c_longlong
ULONG32     = c_uint
ULONG64     = c_ulonglong
DWORD32     = c_uint
DWORD64     = c_ulonglong
BOOL        = c_int
FLOAT       = c_float        
DOUBLE      = c_double       

PVOID       = LPVOID
PPVOID      = POINTER(PVOID)
PSTR        = LPSTR
PWSTR       = LPWSTR
PCHAR       = LPSTR
PWCHAR      = LPWSTR
LPBYTE      = POINTER(BYTE)
LPSBYTE     = POINTER(SBYTE)
LPWORD      = POINTER(WORD)
LPSWORD     = POINTER(SWORD)
LPDWORD     = POINTER(DWORD)
LPSDWORD    = POINTER(SDWORD)
LPULONG     = POINTER(ULONG)
LPLONG      = POINTER(LONG)
LPTSTR      = LPWSTR
PDWORD      = LPDWORD
PULONG      = LPULONG
PLONG       = LPLONG
CCHAR       = CHAR
BOOLEAN     = BYTE
PBOOL       = POINTER(BOOL)
LPBOOL      = PBOOL
TCHAR       = CHAR      
UCHAR       = BYTE
DWORDLONG   = ULONGLONG
LPDWORD32   = POINTER(DWORD32)
LPULONG32   = POINTER(ULONG32)
LPDWORD64   = POINTER(DWORD64)
LPULONG64   = POINTER(ULONG64)
PDWORD32    = LPDWORD32
PULONG32    = LPULONG32
PDWORD64    = LPDWORD64
PULONG64    = LPULONG64
ATOM        = WORD
HANDLE      = LPVOID
PHANDLE     = POINTER(HANDLE)
LPHANDLE    = PHANDLE
HMODULE     = HANDLE
HINSTANCE   = HANDLE
HTASK       = HANDLE
HKEY        = HANDLE
PHKEY       = POINTER(HKEY)
HDESK       = HANDLE
HRSRC       = HANDLE
HSTR        = HANDLE
HWINSTA     = HANDLE
HKL         = HANDLE
HDWP        = HANDLE
HFILE       = HANDLE
HRESULT     = LONG
HGLOBAL     = HANDLE
HLOCAL      = HANDLE
HGDIOBJ     = HANDLE
HDC         = HGDIOBJ
HRGN        = HGDIOBJ
HBITMAP     = HGDIOBJ
HPALETTE    = HGDIOBJ
HPEN        = HGDIOBJ
HBRUSH      = HGDIOBJ
HMF         = HGDIOBJ
HEMF        = HGDIOBJ
HENHMETAFILE = HGDIOBJ
HMETAFILE   = HGDIOBJ
HMETAFILEPICT = HGDIOBJ
HWND        = HANDLE
NTSTATUS    = LONG
PNTSTATUS   = POINTER(NTSTATUS)
RVA         = DWORD
RVA64       = QWORD
WPARAM      = DWORD
LPARAM      = LPVOID
LRESULT     = LPVOID
ACCESS_MASK = DWORD
REGSAM      = ACCESS_MASK
PACCESS_MASK = POINTER(ACCESS_MASK)
PREGSAM     = POINTER(REGSAM)
