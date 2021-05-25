# coding=utf-8
'''
NAME:类
author:zx弘
version：1.0
'''
# -*- coding: utf-8 -*-



###############################################定义常值########################################################

from defines.types import *
from ctypes import Structure
from ctypes import Union

###############################################################定义结构体###############################################################

#定义函数CreateProcessA()函数所需结构体

#定义STARTINFO结构体
class STARTUPINFO(Structure):           #继承ctypes中结构体的类
    _fields_ = [
        ('cb',DWORD),                   #定义结构的大小，以字节为单位
        ('lpReserved',LPTSTR),          #一个保留参数，值必须为"NULL"
        ('lpDesktop',LPTSTR),           #该参数为桌面的名称，每个桌面的窗口和线程是互不干扰的。在这里填入的桌面如果存在，那么就会将线程与桌面进行连接，如果不存在，系统就会用填入的名称新建一个桌面再连接。如果填“NULL”，就会将其与当前的桌面关联
        ('lpTitle',LPTSTR),             #对于控制台进程而言,如果创建了新的控制台，那么该参数的值就为标题栏中的标题。如果填为“NULL”，则将可执行文件的名称作为标题。但如果不创建新控制台，则该参数必须为“NULL”。        
        ('dwX',DWORD),                  #如果在本结构体中的‘Dwflags’成员指定为‘STARTF_USEPOSITION’，则该参数为创建新窗口时的x偏移量。偏移量从屏幕左上角开始，以像素为单位
        ('dWY',DWORD),                  #同上，只不过这是y的偏移量
        ('dwXSize',DWORD),              #如果在本结构体中的‘Dwflags’成员指定为‘STARTF_USESIZE’，则该参数为创建新窗口时的窗口宽度，以像素为单位
        ('dwYSize',DWORD),              #同上，只不过这是窗口的高度
        ('dwXCountChars',DWORD),        #如果在本结构体中的‘Dwflags’成员指定为‘STARTF_USECOUNTCHARS’，则如果在控制台进程中创建了新的控制台窗口，则该成员的值为指定屏幕缓冲区的宽度。 否则，将忽略此成员。
        ('dwYCountChars',DWORD),        #同上，只不过这是屏幕缓冲区的高度
        ('dwFillAttribute',DWORD),      #如果在本结构体中的‘Dwflags’成员指定为‘TARTF_USEFILLATTRIBUTE’，则该参数为新的控制台窗口的初始文本颜色和初始背景颜色
        ('dwFlags',DWORD),              #用以确定新建进程的窗口模式，值可以为一个或多个
        ('wShowWindow',WORD),           #这实际上是传递给ShowWindows（）函数的值，可以指定一些窗口的显示情况。不过，一般来说，在第一次启动，该函数会默认忽视WShowWindows传入的值而使用默认值。
        ('cbReserved2',WORD),           #保留供C运行时使用； 必须为零。
        ('lpReserved2',LPBYTE),         #保留供C运行时使用； 必须为NULL。
        ('hStdInput',HANDLE),           #如果在本结构体中的‘Dwflags’成员指定为‘STARTF_USESTDHANDLES’，则该成员的值为该过程的输入句柄，否则，则默认的输入是键盘缓冲区。
        ('hStdOutput',HANDLE),          #如果在本结构体中的‘Dwflags’成员指定为‘STARTF_USESTDHANDLES’，则该成员的值为该过程的输出句柄，否则，默认的输出是控制台缓冲区。
        ('hStdError',HANDLE),           #如果在本结构体中的‘Dwflags’成员指定为‘STARTF_USESTDHANDLES’，则该成员的值为该过程的标准错误句柄。 否则，将忽略此成员，标准错误的默认值是控制台窗口的缓冲区。
    ]


# 定义PROCESS_INFORMATION结构体
class PROCESS_INFORMATION(Structure):
    _fields_=[
        ('hProcess',HANDLE),            #新创建的进程的句柄。
        ('hThread',HANDLE),             #新创建的进程的主线程的句柄。         
        ('dwProcessId',DWORD),          #可用于标识进程的标识符。
        ('dwThreadId',DWORD),           #可用于标识线程的标识符。
    ]
# 注：当关闭该创建的进程时，应该使用CloseHandle()函数来关闭句柄，否则系统将无法清理子进程的进程结构，因为父进程仍具有子进程的打开句柄。


# 定义WaitForDebugEvent()所需联合体和结构体

#定义输出文本EXCEPTION_DEBUG_INFO结构体
class OUTPUT_DEBUG_STRING_INFO(Structure):
    _fields_=[
       ('lpDebugStringData',LPSTR),
       ('fUnicode',WORD),
       ('nDebugStringLength',WORD),

    ]

#定义调试事件信息结构体

class EXCEPTION_RECORD(Structure):
    _fields_=[
        ('ExceptionCode',DWORD),
        ('ExceptionFlags',DWORD),
        ('ExceptionRecord',DWORD),
        ('ExceptionAddress',PVOID),
        ('NumberParameters',DWORD),
        ('ExceptionInformation',ULONG),            
    ]

class EXCEPTION_RECORD(Structure):
    '''
        ('ExceptionCode',DWORD),        #发生异常的原因。常量已在consist模块定义
        ('ExceptionFlags',DWORD),       #异常标志。 该成员可以为零，表示可连续的异常
        ('ExceptionRecord',EXCEPTION_RECORD),#指向关联的指针 EXCEPTION_RECORD 结构。以在发生嵌套异常时提供其他信息
        ('ExceptionAddress',PVOID),     #发生异常的地址。
        ('NumberParameters',DWORD),     #与异常关联的参数数。 
        ('ExceptionInformation',ULONG), #一组描述异常的附加参数。当异常为EXCEPTION_ACCESS_VIOLATION时，数组的第一个元素包含一个读写标志，该标志指示导致访问冲突的操作类型。 如果该值为零，则线程尝试读取不可访问的数据。 如果该值为1，则线程尝试写入不可访问的地址。第二个数组元素指定不可访问数据的虚拟地址。           
        '''
    _fields_=[
        ('ExceptionCode',DWORD),        #发生异常的原因。常量已在consist模块定义
        ('ExceptionFlags',DWORD),       #异常标志。 该成员可以为零，表示可连续的异常
        ('ExceptionRecord',EXCEPTION_RECORD),#指向关联的指针 EXCEPTION_RECORD 结构。以在发生嵌套异常时提供其他信息
        ('ExceptionAddress',PVOID),     #发生异常的地址。
        ('NumberParameters',DWORD),     #与异常关联的参数。 
        ('ExceptionInformation',ULONG), #一组描述异常的附加参数。当异常为EXCEPTION_ACCESS_VIOLATION时，数组的第一个元素包含一个读写标志，该标志指示导致访问冲突的操作类型。 如果该值为零，则线程尝试读取不可访问的数据。 如果该值为1，则线程尝试写入不可访问的地址。第二个数组元素指定不可访问数据的虚拟地址。           
    ]
#
class EXCEPTION_DEBUG_INFO(Structure):
    _fields_=[
        ('ExceptionRecord',EXCEPTION_RECORD),#一个 EXCEPTION_RECORD 结构，包括异常代码，标志，地址，指向相关异常的指针，其他参数等。
        ('dwFirstChance',DWORD),        #一个值，指示调试器是否遇到指定的 ExceptionRecord异常成员，果 dwFirstChance 成员非零，则这是调试器第一次遇到该异常。 
    ]

# 定义DEBUG_EVENT_UNION联合体
class DEBUG_EVENT_UNION(Union):
    _fields_=[
        ('Exception',EXCEPTION_DEBUG_INFO),#触发异常调试事件
        ('CreateThread',HANDLE),        #创建线程
        ('CreateProcessInfo',HANDLE),   #创建进程
        ('ExitThread',HANDLE),          #退出线程
        ('ExitProcess',HANDLE),         #退出进程
        ('LoadDll',HANDLE),             #加载DLL
        ('UnloadDll',HANDLE),           #卸载DLL
        ('DebugString',OUTPUT_DEBUG_STRING_INFO),#调试输出字符串         
        ('RipInfo',HANDLE),
    ]

# 定义DEBUG_EVENT结构体
class DEBUG_EVENT(Structure):
    _fields_=[
        ('dwDebugEventCode',DWORD),     #调试事件的代码
        ('dwProcessId',DWORD),          #被调试程序的PID
        ('dwThreadId',DWORD),           #被调试程序的TID
        ('u',DEBUG_EVENT_UNION),        #调试事件的进一步详情，其具体由调试事件代码而定
    ]

# 定义Thread32First()所需结构体
# 定义tagTHREADENTRY32结构体
class tagTHREADENTRY32(Structure):
    _fields_=[
        ('dwSize',DWORD),               #结构体的大小，以字节为单位。在传送给Thread32First，必须使用sizeof(THREADENTRY32)，否则会失败。  
        ('cntUsage',DWORD),             #该成员不再被使用，并且始终设置为零。
        ('th32ThreadID',DWORD),         #线程标识符，与CreateProcess函数返回的线程标识符兼容。
        ('th32OwnerProcessID',DWORD),   #创建线程的进程的标识符。
        ('tpBasePri',LONG),             #分配给线程的内核基本优先级。 优先级是从0到31的数字，0表示最低的线程优先级。 有关更多信息，请参见KeQueryPriorityThread。
        ('tpDeltaPri',LONG),            #该成员不再被使用，并且始终设置为零。  
        ('dwFlags',DWORD),              #该成员不再被使用，并且始终设置为零。 
    ]

# 定义GetThreadContext所需结构体
#定义M128A
class M128A(Structure):
    _pack_=1
    _fields_=[
        ('Low',LONGLONG),
        ('High',ULONGLONG),
    ]
#定义
class NEON128(Structure):
    _pack_=1
    _fields_=[
        ('Low',LONGLONG),
        ('High',ULONGLONG),
    ]
#定义DUMMYSTRUCTNAME（虚拟结构体）结构
class ONE(Structure):
    _pack_=1
    _fields_=[
        ('Header',M128A*2),
        ('Legacy',M128A*8),
        ('Xmm0',M128A),
        ('Xmm1',M128A),
        ('Xmm2',M128A),
        ('Xmm3',M128A),
        ('Xmm4',M128A),
        ('Xmm5',M128A),
        ('Xmm6',M128A),
        ('Xmm7',M128A),
        ('Xmm8',M128A),
        ('Xmm9',M128A),
        ('Xmm10',M128A),
        ('Xmm11',M128A),
        ('Xmm12',M128A),
        ('Xmm13',M128A),
        ('Xmm14',M128A),
        ('Xmm15',M128A),        
    ]
#定义XMM_SAVE_AREA32结构体
class XMM_SAVE_AREA32(Structure):
    _pack_=1
    _fields_=[
        ('ControlWord', WORD),
        ('StatusWord',  WORD),
        ('TagWord',     BYTE),
        ('Reserved1',   BYTE),
        ('ErrorOpcode', WORD),
        ('ErrorOffset', DWORD),
        ('ErrorSelector',WORD),
        ('Reserved2',   WORD),
        ('DataOffset',  DWORD),
        ('DataSelector',WORD),
        ('Reserved3',   WORD),
        ('MxCsr',       DWORD),
        ('MxCsr_Mask',  DWORD),
        ('FloatRegisters',M128A*8),
        ('XmmRegisters',M128A*16),
        ('Reserved4',   BYTE*96),
    ]
#定义虚拟联合体（DUMMYUNIONNAME）
class TWO(Union):
    _fields_=[
        ('FltSave',XMM_SAVE_AREA32),
        ('Q',NEON128*16),
        ('D',ULONGLONG*32),
        ('DUMMYSTRUCTNAME',ONE),
        ('S',DWORD*32),
    ]
# 定义CONTEXT结构

class CONTEXT(Structure):
    _fields_=[
        ('P1Home',                  DWORD64),
        ('P2Home',                  DWORD64),
        ('P3Home',                  DWORD64),
        ('P4Home',                  DWORD64),
        ('P5Home',                  DWORD64),
        ('P6Home',                  DWORD64),
        ('ContextFlags',            DWORD),
        ('MxCsr',                   DWORD),
        ('SegCs',                   WORD),
        ('SegDs',                   WORD),
        ('SegEs',                   WORD),
        ('SegFs',                   WORD),
        ('SegGs',                   WORD),
        ('SegSs',                   WORD),
        ('EFlags',                  DWORD),
        ('Dr0',                     DWORD64),
        ('Dr1',                     DWORD64),
        ('Dr2',                     DWORD64),
        ('Dr3',                     DWORD64),
        ('Dr6',                     DWORD64),
        ('Dr7',                     DWORD64),
        ('Rax',                     DWORD64),
        ('Rcx',                     DWORD64),
        ('Rdx',                     DWORD64),
        ('Rbx',                     DWORD64),
        ('Rsp',                     DWORD64),
        ('Rbp',                     DWORD64),
        ('Rsi',                     DWORD64),
        ('Rdi',                     DWORD64),
        ('R8',                      DWORD64),
        ('R9',                      DWORD64),
        ('R10',                     DWORD64),
        ('R11',                     DWORD64),
        ('R12',                     DWORD64),
        ('R13',                     DWORD64),
        ('R14',                     DWORD64),
        ('R15',                     DWORD64),
        ('Rip',                     DWORD64),
        ('DUMMYUNIONNAME',          TWO),
        ('VectorRegister[26]',      M128A*26),
        ('VectorControl',           DWORD64),
        ('DebugControl',            DWORD64),
        ('LastBranchToRip',         DWORD64),
        ('LastBranchFromRip',       DWORD64),
        ('LastExceptionToRip',      DWORD64),
        ('LastExceptionFromRip',    DWORD64),
    ]