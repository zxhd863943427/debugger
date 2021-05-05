from defines.bash_debugger import *
test=bash_debugger()
test.load(r'C:\Users\admin\Desktop\calc.exe')
print('error = ',kernel32.GetLastError())
print('正在获取进程句柄')
print(f'进程句柄为{test.get_process_handle(test.PID)}')
print('error = ',kernel32.GetLastError())
print(f'线程句柄为{test.get_thread_handle(test.TID)}')
print('error = ',kernel32.GetLastError())
dic={}
debug=DEBUG_EVENT()
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
while debug.dwDebugEventCode!=EXIT_PROCESS_DEBUG_EVENT:
    i+=1
    print(dic[debug.dwDebugEventCode])
    test.wait(-1,debug)
    print('已暂停，即将继续')
    test.ContinueEvent(debug.dwProcessId,debug.dwThreadId)
    print(debug.dwDebugEventCode)
    print('第',i,'次','error = ',kernel32.GetLastError())
a=input('准备退出……')
