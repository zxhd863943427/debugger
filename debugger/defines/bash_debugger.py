# coding=utf-8
'''
NAME:bash
author:zx弘
version：1.0

这里负责写入最简单的API接口，完成从WIN32 API到python的封装
'''

from defines.types import *
from defines.debugger_class import *
from defines.consist import *

kernel32=windll.kernel32
class bash_debugger():

    def __init__(self):
        self.PID=None
        self.TID=None
        self.process_handle=None
        self.thread_handle=None
        self.thread_hSnapshot_handle=None
        self.active=False
 ##############################################创建进程###########################################################
    def load(self,path_to_exe):
            # 实例化结构体
            startupinfo =               STARTUPINFO()
            process_information =       PROCESS_INFORMATION()
            startupinfo.dwflags =       STARTF_USHOWWINDOW
            startupinfo.wShowWindow =   0x00000001
            startupinfo.cb =            sizeof(startupinfo)

            if kernel32.CreateProcessW(path_to_exe,None,None,None,False,DEBUG_PROCESS,None,None,byref(startupinfo),byref(process_information)):
                print(f'载入{path_to_exe}成功！')
                print(f'{path_to_exe}的PID标识符是 {process_information.dwProcessId}')
                self.PID=process_information.dwProcessId
                self.TID=process_information.dwThreadId
                self.process_handle=self.get_process_handle(self.PID)
                #print(f'该调用进程的句柄是{kernel32.GetCurrentProcessId()}')
            else:
                print(f"载入{path_to_exe}程序失败")
 
                
##############################################获取各种句柄的各种方法###########################################################
    
    #获取线程句柄
    def get_thread_handle(self,TID,dwDesiredAccess=THREAD_ALL_ACCESS):
        handle=kernel32.OpenThread(dwDesiredAccess,False,TID)
        return handle

    #获取进程句柄
    def get_process_handle(self,PID,dwDesiredAccess=PROCESS_ALL_ACCESS):
        handle=kernel32.OpenProcess(dwDesiredAccess,False,PID)
        return handle
    
    #获取快照句柄
    def get_hSnapshot_handle(self,dwFlags,th32ProcessID):
        handle=kernel32.CreateToolhelp32Snapshot(dwFlags,th32ProcessID)
        return handle

    

##############################################获取各种调试结构体的各种方法###########################################################

    #捕获调试结果并返回一个储存调试信息的结构体
    def wait(self,dwMilliseconds=INFINITE,DebugEvent=DEBUG_EVENT()):
        DebugEvent = DEBUG_EVENT()
        output=kernel32.WaitForDebugEventEx(byref(DebugEvent),dwMilliseconds)
        #print(output)
        #print(dir(DebugEvent))
        return output

##############################################对进程的各种方法###########################################################

    #将调试器附加到进程上
    def attach(self,PID):
        attrack=kernel32.DebugActiveProcess(PID)
        return attrack

    #让进程继续
    def ContinueEvent(self,dwProcessId,dwThreadId,dwContinueStatus=DBG_CONTINUE):
        return kernel32.ContinueDebugEvent(dwProcessId,dwThreadId,dwContinueStatus)

    #停止目标进程的调试器附着
    def debugStop(self,dwProcessId):
        output=kernel32.DebugActiveProcessStop(dwProcessId)
        return output

##############################################对线程的各种方法###########################################################

    #取得线程上下文并传出
    def get_context(self,h_thread,Context=CONTEXT()):
        output=kernel32.GetThreadContext(h_thread,byref(Context))
        #print('*'*100,output)
        return output


##############################################对快照的各种方法###########################################################
    
    #获取线程首个快照
    def get_thread_first_Snapshot(self,handle,tag=tagTHREADENTRY32()):
        tag.cntUsage=0
        tag.tpDeltaPri=0
        tag.dwFlags=0
        tag.dwSize=sizeof(tag)
        output=kernel32.Thread32First(handle, byref(tag))
        return output

    #获取线程接下来的快照
    def get_thread_next_Snapshot(self,handle,tag=tagTHREADENTRY32()):
        tag.cntUsage=0
        tag.tpDeltaPri=0
        tag.dwFlags=0
        tag.dwSize=sizeof(tag)
        output=kernel32.Thread32Next(handle, byref(tag))
        return output