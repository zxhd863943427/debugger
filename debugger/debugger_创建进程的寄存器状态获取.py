# coding=utf-8
'''
NAME:寄存器状态获取
author:zx弘
version：1.0
'''
from defines.bash_debugger import bash_debugger,kernel32
from defines.debugger_class import DEBUG_EVENT,CONTEXT
from defines.consist import TH32CS_SNAPTHREAD

dic={3:'CREATE_PROCESS_DEBUG_EVENT',
2:'CREATE_THREAD_DEBUG_EVENT',
1:'ECEPTION_DEBUG_EVENT',
5:'EIT_PROCESS_DEBUG_EVENT',
4:'EIT_THREAD_DEBUG_EVENT',
6:'LOAD_DLL_DEBUG_EVENT',
8:'OUTPUT_DEBUG_STRING_EVENT',
9:'RIP_EVENT',
7:'UNLOAD_DLL_DEBUG_EVENT',
0:'start'}

def get_error(str):
    print(str,' 的报错代码是 ',kernel32.GetLastError())

test=bash_debugger()
test.load(r"C:\Users\admin\Desktop\calc.exe")
DebugEvent=DEBUG_EVENT()
while DebugEvent.dwDebugEventCode !=5:
    test.wait(-1,DebugEvent)
    get_error('wait')
    test.PID=DebugEvent.dwProcessId
    test.TID=DebugEvent.dwThreadId
    test.thread_handle=test.get_thread_handle(test.TID)
    get_error('test.get_thread_handle')
    test.thread_hSnapshot_handle=test.get_hSnapshot_handle(TH32CS_SNAPTHREAD,test.PID)
    get_error('test.get_hSnapshot_handle')
    get_Snapshot_active=True
    context=CONTEXT()
    kernel32.SuspendThread(test.thread_handle)
    test.get_context(test.thread_handle,context)
    get_error('test.get_context')
    print(f'Dr0的值为:{context.Dr0}')
    print(f'Dr1的值为:{context.Dr1}')
    print(f'Dr2的值为:{context.Dr2}')
    print(f'Dr3的值为:{context.Dr3}')
    print(f'Dr6的值为:{context.Dr6}')
    print(f'Dr7的值为:{context.Dr7}')
    print(f'Rax的值为:{context.Rax}')
    print(f'Rcx的值为:{context.Rcx}')
    print(f'Rdx的值为:{context.Rdx}')
    print(f'Rbx的值为:{context.Rbx}')
    print(f'Rsp的值为:{context.Rsp}')
    print(f'Rbp的值为:{context.Rbp}')
    print(f'Rsi的值为:{context.Rsi}')
    print(f'Rdi的值为:{context.Rdi}')
    print(f'R8的值为:{context.R8}')
    print(f'R9的值为:{context.R9}')
    print(f'R10的值为:{context.R10}')
    print(f'R11的值为:{context.R11}')
    print(f'R12的值为:{context.R12}')
    print(f'R13的值为:{context.R13}')
    print(f'R14的值为:{context.R14}')
    print(f'R15的值为:{context.R15}')
    print(f'Rip的值为:{context.Rip}') 
    test.ContinueEvent(test.PID,test.TID)
    kernel32.ResumeThread(test.thread_handle)
    print(dic[DebugEvent.dwDebugEventCode])
    get_error('test.ContinueEvent')
