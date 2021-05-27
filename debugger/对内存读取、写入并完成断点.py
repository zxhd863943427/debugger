# coding=utf-8
'''
NAME:对内存读取、写入并完成断点
author:zx弘
version：1.0
'''
from defines.main import debugger,kernel32,DEBUG_EVENT,EXIT_PROCESS_DEBUG_EVENT

test=debugger()

test.PID = eval(input('请输入PID'))
print('start','error = ',kernel32.GetLastError())
a = test.attach(test.PID)
print('附加的结果是',a)
print('attach','error = ',kernel32.GetLastError())
address = test.resolve_function(b'msvcrt.dll',b'printf')
print('函数的地址为：',address)
pid =test.PID

test.bp_set(address,pid)
handle=test.get_process_handle(test.PID,0x0010,mode=0)
original_byte=test.read_process_memory(address,36,handle)
print('设置断点后读取的数据为',original_byte)


i=1
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

debug = DEBUG_EVENT()

while debug.dwDebugEventCode!=EXIT_PROCESS_DEBUG_EVENT and i <=100:
    i+=1
    print(dic[debug.dwDebugEventCode])
    test.wait(-1,debug)
    test.exception_do(debug)
    print('已暂停，即将继续')
    test.ContinueEvent(debug.dwProcessId,debug.dwThreadId)
    print(debug.dwDebugEventCode)
    print('第',i,'次','error = ',kernel32.GetLastError())


read = test.read_process_memory(address,12)
print(read)
test.debugStop(test.PID)
a=input('准备退出……')