# coding=utf-8
'''
NAME:主程序
author:zx弘
version：1.0
'''
"""
这里只写最简单的调用

"""
from defines.types import *
from defines.debugger_class import *
from defines.consist import *
from defines.bash_debugger import *

kernel32=windll.kernel32
class debugger(bash_debugger):

    def __init__(self):
        bash_debugger.__init__(self)
        


    #获取全部线程快照句柄
    def get_thread_hSnapshot_handle(self):
        handle=self.get_hSnapshot_handle(TH32CS_SNAPTHREAD,0)
        self.thread_hSnapshot_handle=handle
        return handle
 


    #使用附加进程调试的组合函数，返回储存附加进程信息的结构体
    def start(self,PID):
        print(PID)
        self.process_handle=self.get_process_handle(PID)
        if self.attach(PID):
            print('附着程序成功！正在获取调试信息……')
            self.active=True
            self.run()
        else:
            print('附着程序失败，正在退出……')
    
    def run(self):
        print(1)
        while self.active==True:
            print(2)
            debugEvent=DEBUG_EVENT()
            if self.wait(INFINITE,debugEvent):
                print(3)
                print(debugEvent.dwProcessId)
                self.PID=debugEvent.dwProcessId
                print(4)
                self.TID=debugEvent.dwThreadId
                print(f'捕获调试信息成功！目标进程的PID为{self.PID}，线程TID为{self.TID}')
                test=input('请输入命令或退出调试……')
                self.active=False
                if self.ContinueEvent(self.PID,self.TID):
                    print('继续进程成功！')
                else:
                    print('继续进程失败……')
            else:
                print(f'捕获调试信息失败……')
                test=input('请输入命令或退出调试……')
                self.active=False

    def detach(self):
        if self.debugStop(self.PID):
            print('解除附着成功！')
        else:
            print('解除附着失败……')

    

##################################################组合高级命令##########################################
    #循环提取全部目标进程
    def get_thread_all_Snapshot(self,PID):
        #初始化结构体和设置循环状态
        tag=tagTHREADENTRY32()
        active=True
        list1=[]
        h_thread=None
        #获取快照句柄
        self.get_thread_hSnapshot_handle()
        self.get_thread_first_Snapshot(self.thread_hSnapshot_handle,tag)
        if tag.th32OwnerProcessID==PID:
            print(f'已经捕获目标进程的线程，线程TID为{tag.th32ThreadID}')
            #h_thread=self.get_thread_handle(tag.th32ThreadID)
            h_thread=tag.th32ThreadID
            list1.append(h_thread)
        while active==True:
            active=self.get_thread_next_Snapshot(self.thread_hSnapshot_handle,tag)
            if tag.th32OwnerProcessID==PID:
                print(f'已经捕获目标进程的线程，线程TID为{tag.th32ThreadID}')
                #h_thread=self.get_thread_handle(tag.th32ThreadID)
                h_thread=tag.th32ThreadID
                list1.append(h_thread)
        return list1

    #获取线程上下文
    def get_thread_context(self,PID):
        context=CONTEXT()
        list1=self.get_thread_all_Snapshot(PID)
        for item in list1:
            item=self.get_thread_handle(item)
            kernel32.SuspendThread(item)
            self.get_context(item,context)
            kernel32.ResumeThread(item)
            kernel32.CloseHandle(item)
            print(f'已获取线程句柄为{item}的寄存器信息，正在输出……')
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


if __name__ =='__main__':
    test=debugger()
    a=input('PID')
    a=eval(a)
    test.get_process_handle(PROCESS_ALL_ACCESS,a)
    print(kernel32.GetLastError())