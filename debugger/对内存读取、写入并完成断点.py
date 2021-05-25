# coding=utf-8
'''
NAME:
author:zx弘
version：1.0
'''
# coding=utf-8
'''
NAME建立异常事件处理例程
author:zx弘
version：1.0
'''
from defines.main import debugger
from defines.bash_debugger import kernel32
from defines.consist import *
from defines.debugger_class import *
test=debugger()
test.load(r'C:\Users\admin\Desktop\calc.exe')
print('error = ',kernel32.GetLastError())
debug=DEBUG_EVENT()
test.wait(-1,debug)
print('error = ',kernel32.GetLastError())
test.ContinueEvent(debug.dwProcessId,debug.dwThreadId)
print('error = ',kernel32.GetLastError())
test.debugStop(debug.dwProcessId)
print('error = ',kernel32.GetLastError())
a = eval(input('已退出创建调试，重新输入PID，进入附着调试'))
kernel32.DebugActiveProcess(a)
print('error = ',kernel32.GetLastError())
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

dic1={
0x80000003 : '#调试事件为触发断点',
0xC0000005 : '#线程试图读取或写入对其没有适当访问权限的虚拟地址。',
0xC0000092 : '#浮点运算的结果是堆栈上溢或下溢。',
0xC00000FD : '#线程耗尽了其堆栈。',}      


i=1
while debug.dwDebugEventCode!=EXIT_PROCESS_DEBUG_EVENT and i <=150:
    i+=1
    debug=DEBUG_EVENT()
    test.wait(-1,debug,1)
    test.progress_handle = test.get_process_handle(debug.dwProcessId)
    print(dic[debug.dwDebugEventCode])
    print(debug.dwDebugEventCode)

    test.exception_do(debug)  
    print('已暂停，即将继续')
    print(test.process_handle)
    str1=test.read_process_memory(0x00001,0x02,test.progress_handle)
    #print(str1)
    print(debug.dwProcessId,debug.dwThreadId)
    print(kernel32.ContinueDebugEvent(debug.dwProcessId,debug.dwThreadId,DBG_CONTINUE))
    print(debug.dwDebugEventCode)
    print('第',i,'次','error = ',kernel32.GetLastError())
    print('*'*70)
    #if i >=300:
    #    break
a=input('准备退出……')