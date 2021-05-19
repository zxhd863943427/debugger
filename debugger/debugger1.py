# coding=utf-8
'''
NAME:
author:zx弘
version：1.0
'''
def get_error(str):
    print(str,' 的报错代码是 ',kernel32.GetLastError())
from defines.bash_debugger import bash_debugger,kernel32
from defines.debugger_class import DEBUG_EVENT,CONTEXT,tagTHREADENTRY32
from defines.consist import TH32CS_SNAPTHREAD
from defines.types import sizeof
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
test=bash_debugger()
test.PID=eval(input('PID'))
handle=test.get_hSnapshot_handle(4,test.PID)
