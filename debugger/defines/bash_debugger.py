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
        self.context=None
        self.debug_event=None
        self.ExceptionAddress=None
        self.ExceptionInformation=None
        self.dwFirstChance=None
        self.bp_list = {}
        self.active=False
        
 ##############################################创建进程###########################################################
    #已测试
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
    
    #获取线程句柄     已测试
    def get_thread_handle(self,TID,dwDesiredAccess=THREAD_ALL_ACCESS):
        handle=kernel32.OpenThread(dwDesiredAccess,False,TID)
        return handle

    #获取进程句柄     已测试
    def get_process_handle(self,PID,dwDesiredAccess=PROCESS_ALL_ACCESS,mode = 1):
        """
        获取进程句柄,并更新主结构体中的process_handle参数。默认句柄为最大权限模式。将mode改为0
        可以不更新主结构体中的process_handle参数
        """
        kernel32.OpenProcess.argtypes=[DWORD,BOOL,DWORD]
        kernel32.OpenProcess.restype = HANDLE
        handle=kernel32.OpenProcess(dwDesiredAccess,False,PID)
        #print('获取的句柄为',handle)
        if mode == 1:
            self.process_handle = handle
        
        return handle
    
    #获取快照句柄     已测试
    def get_hSnapshot_handle(self,dwFlags,th32ProcessID):
        handle=kernel32.CreateToolhelp32Snapshot(dwFlags,th32ProcessID)
        # DWORD dwFlags
        return handle

    

##############################################获取各种调试结构体的各种方法###########################################################

    #捕获调试结果并返回一个储存调试信息的结构体      已测试
    def wait(self,dwMilliseconds=INFINITE,DebugEvent=DEBUG_EVENT(),mode=0):
        '''
        捕获调试结果并返回一个储存调试信息的结构体,可以选择mode=1，来决定是否更新结构体的PID，TID
        '''
        #DebugEvent = DEBUG_EVENT()
        output=kernel32.WaitForDebugEventEx(byref(DebugEvent),dwMilliseconds)

        if mode == 1:
            self.PID = DebugEvent.dwProcessId
            self.TID = DebugEvent.dwThreadId
        return output

##############################################对进程的各种方法###########################################################

    #将调试器附加到进程上     已测试
    def attach(self,PID):
        '''
        将调试器附加到进程,参数为目标PID
        '''
        attrack=kernel32.DebugActiveProcess(PID)
        return attrack

    #让进程继续              未测试
    def ContinueEvent(self,dwProcessId,dwThreadId,dwContinueStatus=DBG_CONTINUE):
        kernel32.ContinueDebugEvent.argtypes = [DWORD,DWORD,DWORD]
        kernel32.ContinueDebugEvent.restype = BOOL
        return kernel32.ContinueDebugEvent(dwProcessId,dwThreadId,dwContinueStatus)

    #停止目标进程的调试器附着   已测试
    def debugStop(self,dwProcessId):
        '''
        关闭结构体的进程句柄、线程句柄,然后清除process_handle、thread_handle、PID、TID并退出进程附着
        '''
        if self.process_handle !=None:
            kernel32.CloseHandle(self.process_handle)
            self.process_handle = None
        if self.thread_handle !=None:            
            kernel32.CloseHandle(self.thread_handle)
            self.thread_handle = None
        if self.PID !=None:
            self.PID = None
        if self.TID !=None:            
            self.TID = None
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


##############################################对内存的各种方法###########################################################

    def read_process_memory(self,address,length=2,handle=None):
        '''
        #读取内存的函数，默认读取两个字节
        '''
        if handle == None:
            if self.PID !=None:
                handle = self.get_process_handle(self.PID,PROCESS_VM_READ,mode=0)
            else:
                print('在未输入参数的情况下未从主结构体中获得PID')
                return False
        
        # 初始化函数的参数输入和输出
        kernel32.ReadProcessMemory.argtypes = [HANDLE,LPVOID,LPVOID,SIZE_T,SIZE_T]
        kernel32.ReadProcessMemory.restype = BOOL

        #导入创建内存缓存区的函数
        from ctypes import create_string_buffer
        
        # 初始输出变量、内存区和参数
        data = b''
        read_buf = create_string_buffer(length)
        count = 0        

        if not kernel32.ReadProcessMemory(
            handle,
            address,
            read_buf,
            length,
            count):
            print("读取内存失败……")
            print('WriteProcessMemory','error = ',kernel32.GetLastError())
            return False
    
        else:
            data += read_buf.raw
            kernel32.CloseHandle(handle)
            return data    
    

    def write_process_memory(self,address,data,handle=None):
        '''
        一个写入内存的函数，默认句柄从主结构体获得,需要输入写入的地址和待写入的数据
        注意！输入的数据必须是二进制的！
        '''

        #检测是否输入句柄参数
        if handle == None:
            if self.PID !=None:
                handle = self.get_process_handle(self.PID,PROCESS_VM_WRITE,mode=0)
            else:
                print('在未输入参数的情况下未从主结构体中获得句柄')
                return False        

        # 初始化变量
        count = 0
        length = len(data)

        #设置函数的传入和返回类型
        kernel32.WriteProcessMemory.argtypes = [HANDLE,LPVOID,LPVOID,SIZE_T,SIZE_T]
        kernel32.WriteProcessMemory.restype = BOOL     

        if not kernel32.WriteProcessMemory(
            handle,
            address,
            data,
            length,
            count):
            print('写入内存失败……')
            print('WriteProcessMemory','error = ',kernel32.GetLastError())
            return False
        
        else:
            kernel32.CloseHandle(handle)
            return True

##############################################对dll库的各种方法###########################################################

    def resolve_function(self, dll, func):
        '''
        获取dll或exe库中的函数或变量，输入必须为byte类型。第一个参数为库名，第二个参数为函数
        '''

        #初始化GetModuleHandleA的输入和返回类型，该函数用来获取dll或exe库的句柄
        kernel32.GetModuleHandleA.argtypes = [c_char_p]
        kernel32.GetModuleHandleA.restype = c_void_p
        handle = kernel32.GetModuleHandleA(dll)

        #调试位
        print('GetModuleHandleA','error = ',kernel32.GetLastError())
        print(handle)

        #初始化GetProcAddress的输入和返回类型，该函数用来获取指定模块的地址
        kernel32.GetProcAddress.argtypes = [c_void_p,c_char_p]
        kernel32.GetProcAddress.restype = c_void_p    
        address = kernel32.GetProcAddress(handle, func)

        #调试位
        print('GetProcAddress','error = ',kernel32.GetLastError())

        #关闭库的句柄，不知道为什么没有用
        #kernel32.CloseHandle.argtypes = [c_void_p]
        #.CloseHandle.restype = BOOL
        #kernel32.CloseHandle(handle)

        #调试位
        #print('CloseHandle','error = ',kernel32.GetLastError())

        #将报错归零
        #kernel32.GetLastError(0)

        #返回值
        return address

