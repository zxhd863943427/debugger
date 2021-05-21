# coding=utf-8
'''
NAME:尝试使用获取上下文模块
author:zx弘
version：1.0
'''

from defines.main import debugger,kernel32
from defines.debugger_class import CONTEXT,DEBUG_EVENT

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

test = debugger()
a=eval(input('输入PID'))
test.attach(a)
test.PID = a
debug = DEBUG_EVENT()
test.context = CONTEXT()

i = 0
stop = 0
while debug.dwDebugEventCode!= 5:
    i+=1
    #stop=input('输入回车继续或输入1退出')
    if i >= 1000:
        break
    test.wait(-1,debug)
    print('test.wait','error = ',kernel32.GetLastError())
    print('已进入调试，准备继续……')
    print('目前的调试事件为：',dic[debug.dwDebugEventCode])
    print('正在获取进程全部线程……')
    TID_list=test.get_thread_all_Snapshot(test.PID)
    print('test.get_thread_all_Snapshot','error = ',kernel32.GetLastError())
    for tid in TID_list:
        test.TID = tid
        test.context = CONTEXT()
        test.get_thread_context()
        print('test.get_thread_context_new','error = ',kernel32.GetLastError())
        print(f'已获取线程TID为{tid}的寄存器信息，正在输出……')
        test.print_context()
        print('test.print_context','error = ',kernel32.GetLastError())
    test.ContinueEvent(debug.dwProcessId,debug.dwThreadId)
    print(debug.dwDebugEventCode)
    print('第',i,'次','error = ',kernel32.GetLastError())

test.debugStop(a)