# coding=utf-8
'''
NAME:常量
author:zx弘
version：1.0
'''
##CreateProcessA()所需常量
DEBUG_PROCESS =       0x00000001
#这个常值意思是"父进程可以调试子进程，孙进程"
CREATE_NEW_CONSOLE =  0x00000010
#这个常值意识是"新进程创建新的窗口"

## 定义一些OpenProcess()的常量
PROCESS_ALL_ACCESS =        0x001F0FFF      #允许对指定进程对象的所有可能的访问操作
PROCESS_CREATE_PROCESS =    0x0080          #创建过程所需
PROCESS_CREATE_THREAD =     0x0002          #创建线程所需
PROCESS_DUP_HANDLE =        0x0040          #使用DuplicateHandle复制句柄是必需的
PROCESS_SUSPEND_RESUME =    0x0800          #暂停或恢复过程所需
SYNCHRONIZE =               0x00100000      #使用wait()函数来等待进程终止是必需的

# 定义Dwflags的参数常量
STARTF_USECOUNTCHARS =      0x00000008      #调用dwXCountChars 和 dwYCountChars的参数。
STARTF_USEFILLATTRIBUTE =   0x00000010      #调用 dwFillAttribute 的参数
STARTF_USEPOSITION =        0x00000004      #调用 DWX 和 DWY 的参数
STARTF_USHOWWINDOW =        0x00000001      #调用 wShowWindow 的参数
STARTF_USESIZE =            0x00000002      #调用 dwXSize 和 dwYSize 的参数
STARTF_USESTDHANDLES =      0x00000100      #调用 hStdInput ， hStdOutput 和 hStdError的参数

# 定义WaitForDebugEventEx的参数常量
INFINITE =                  0xFFFFFFFF

CREATE_PROCESS_DEBUG_EVENT =0x00000003
CREATE_THREAD_DEBUG_EVENT = 0x00000002
EXCEPTION_DEBUG_EVENT =     0x00000001
EXIT_PROCESS_DEBUG_EVENT =  0x00000005
EXIT_THREAD_DEBUG_EVENT =   0x00000004
LOAD_DLL_DEBUG_EVENT =      0x00000006
OUTPUT_DEBUG_STRING_EVENT = 0x00000008
RIP_EVENT =                 0x00000009
UNLOAD_DLL_DEBUG_EVENT =    0x00000007

# 定义ContinueDebugEvent的参数常量
DBG_CONTINUE =              0x00010002      #如果dwThreadId参数指定的线程先前报告了EXCEPTION_DEBUG_EVENT调试事件，则该函数将停止所有异常处理并继续执行该线程，并将该异常标记为已处理。 对于任何其他调试事件，此标志仅继续执行线程。
DBG_EXCEPTION_NOT_HANDLED = 0x80010001      #如果由dwThreadId指定的线程先前报告了EXCEPTION_DEBUG_EVENT调试事件，该函数将继续异常处理。如果这是第一次发生的异常事件，则使用结构化异常处理程序的搜索和分派逻辑;否则，进程将被终止。对于任何其他调试事件，此标志只是继续线程。
DBG_REPLY_LATER =           0x40010001      #在Windows 10，版本1507或更高版本中支持，这个标志导致dwThreadId在目标继续后重放现有的中断事件。通过对dwThreadId调用suspenthread API，调试器可以恢复进程中的其他线程，然后返回到中断状态。

#定义OpenThred的参数常量
THREAD_ALL_ACCESS =         0x001FFFFF

#定义CreateToolhelp32Snapshot的参数常量
TH32CS_INHERIT =            0x80000000      #标识快照句柄是可继承的。
TH32CS_SNAPALL =            0x0000000F      #包括系统中的所有进程和线程，以及th32ProcessID中指定的进程的堆和模块。 等效于指定使用OR运算（'|'）组合的TH32CS_SNAPHEAPLIST，TH32CS_SNAPMODULE，TH32CS_SNAPPROCESS和TH32CS_SNAPTHREAD值。
TH32CS_SNAPHEAPLIST =       0x00000001      #包括快照中th32ProcessID中指定的所有进程堆。 要枚举堆，请参见Heap32ListFirst。
TH32CS_SNAPMODULE =         0x00000008      #包括快照中th32ProcessID中指定的进程的所有模块。 要枚举模块，请参见Module32First。 如果函数失败并显示ERROR_BAD_LENGTH，请重试该函数，直到成功为止。在32位进程中使用此标志包括th32ProcessID中指定的进程的32位模块，而在64位进程中使用它包括64位模块。 要包含来自64位进程的th32ProcessID中指定的进程的32位模块，请使用TH32CS_SNAPMODULE32标志。
TH32CS_SNAPMODULE32 =       0x00000010      #从64位进程调用时，包括快照中th32ProcessID中指定的进程的所有32位模块。 该标志可以与TH32CS_SNAPMODULE或TH32CS_SNAPALL结合使用。 如果函数失败并显示ERROR_BAD_LENGTH，请重试该函数，直到成功为止。
TH32CS_SNAPPROCESS =        0x00000002      #在快照中包括系统中的所有进程。 要枚举进程，请参阅Process32First。
TH32CS_SNAPTHREAD =         0x00000004      #在快照中包括系统中的所有线程。 要枚举线程，请参见Thread32First。要标识属于特定进程的线程，请在枚举线程时将其进程标识符与THREADENTRY32结构的th32OwnerProcessID成员进行比较。