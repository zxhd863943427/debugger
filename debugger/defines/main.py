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
    

    #获取目标进程线程的上下文环境并输出结构体
    def get_thread_context(self,PID=None,TID=None,context=None,ContextFlags=CONTEXT_ALL):
        '''
        #获取目标进程线程的上下文环境并输出结构体
        CONTEXT_CONTROL =           0x00100001      #获取调试寄存器的值
        CONTEXT_FULL =              0x0010000B      #获取所有寄存器的值
        CONTEXT_ALL =               0x0010001B      #获取所有寄存器的值
        CONTEXT_INTEGER =           0x00100002      #获取通用寄存器的值
        CONTEXT_SEGMENTS =          0x00010004      #获取Seg寄存器的值————暂时不知道是什么东西        
        '''
        if PID == None:
            if self.PID !=None:
                PID = self.PID
            else:
                print("在无参数输入的的情况下未从结构体本身读取到程序PID")
                return -1

        if TID == None:
            if self.TID !=None:
                TID = self.TID
            else:
                print("在无参数输入的的情况下未从结构体本身读取到程序TID")
                return -2

        if context == None:
            if self.context !=None:                
                context = self.context            
            else:
                print("在无参数输入的的情况下未从结构体本身读取到输出结构体")
                return -3

                
        context.ContextFlags=ContextFlags
        thread_handle = self.get_thread_handle(TID)
        #print('self.get_thread_handle','error = ',kernel32.GetLastError())
        kernel32.SuspendThread(thread_handle)
        #print('kernel32.SuspendThread','error = ',kernel32.GetLastError())
        self.get_context(thread_handle,context)            
        #print('self.get_context','error = ',kernel32.GetLastError())
        #self.ContinueEvent(PID,TID)
        #print('self.ContinueEvent','error = ',kernel32.GetLastError())
        kernel32.ResumeThread(thread_handle)
        #print('kernel32.ResumeThread','error = ',kernel32.GetLastError())
        kernel32.CloseHandle(thread_handle)
        #print('kernel32.CloseHandle','error = ',kernel32.GetLastError())

        return context


            


    # 输出上下文信息
    def print_context(self, context=None,mode=2):
        '''
        输出上下文信息,输入一个CONTEXT结构体，默认输出为精简版信息，
        可以修改mode=1查看完整版信息
        '''
        if context ==None:
            if self.context != None:
                context = self.context
            else:
                print('当前函数未输入参数，而未从结构体获取context结构体')
                return -1
        if mode == 1:
            print(f'P1Home的值为: {context. P1Home }')
            print(f'P2Home的值为: {context. P2Home }')
            print(f'P3Home的值为: {context. P3Home }')
            print(f'P4Home的值为: {context. P4Home }')
            print(f'P5Home的值为: {context. P5Home }')
            print(f'P6Home的值为: {context. P6Home }')
            print(f'ContextFlags的值为: {context. ContextFlags }')
            print(f'MxCsr的值为: {context. MxCsr }')
            print(f'SegCs的值为: {context. SegCs }')
            print(f'SegDs的值为: {context. SegDs }')
            print(f'SegEs的值为: {context. SegEs }')
            print(f'SegFs的值为: {context. SegFs }')
            print(f'SegGs的值为: {context. SegGs }')
            print(f'SegSs的值为: {context. SegSs }')
            print(f'EFlags的值为: {context. EFlags }')
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
        elif mode == 2:
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

    #调试事件处理例程模块
    def exception_do(self,debug_event=None):
        '''
        传入一个DEBUG_EVENT结构体，自动分析是否为异常调试事件，若是，再进入异常事件处理例程，并更新主结构的
        ExceptionAddress、ExceptionInformation、dwFirstChance参数。
        若使用默认值，则调用结构体自身debug_event属性
        '''
        
        if debug_event == None:
            if self.debug_event != None:
                debug_event = self.debug_event
            else:
                print('在未输入参数的情况下没有从主结构体中读取到DEBUG_EVENT结构体')

        from defines.consist import EXCEPTION_DEBUG_EVENT
        from defines.consist import EXCEPTION_BREAKPOINT
        from defines.consist import EXCEPTION_ACCESS_VIOLATION
        from defines.consist import EXCEPTION_FLT_STACK_CHECK
        from defines.consist import EXCEPTION_STACK_OVERFLOW
        from defines.consist import EXCEPTION_SINGLE_STEP
        from defines.consist import EXCEPTION_GUARD_PAGE


        if debug_event.dwDebugEventCode != EXCEPTION_DEBUG_EVENT:
            return False
        
        else:
            self.dwFirstChance = debug_event.u.Exception.dwFirstChance
            ExceptionRecord = debug_event.u.Exception.ExceptionRecord  #方便后面写

            if ExceptionRecord.ExceptionCode == EXCEPTION_BREAKPOINT:
                print('调试事件为触发断点')
                print(ExceptionRecord.ExceptionFlags)
                print(ExceptionRecord.NumberParameters)
                print(ExceptionRecord.ExceptionInformation)
                print('异常地址为：',ExceptionRecord.ExceptionAddress)

            elif ExceptionRecord.ExceptionCode == EXCEPTION_GUARD_PAGE:
                print('触发内存保护页断点')
                print('异常地址为：',ExceptionRecord.ExceptionAddress) 

            elif ExceptionRecord.ExceptionCode == EXCEPTION_ACCESS_VIOLATION:
                print('线程试图读取或写入对其没有适当访问权限的虚拟地址。') 
                print('异常地址为：',ExceptionRecord.ExceptionAddress)                  


            elif ExceptionRecord.ExceptionCode == EXCEPTION_FLT_STACK_CHECK:
                print('浮点运算的结果是堆栈上溢或下溢。') 
                print('异常地址为：',ExceptionRecord.ExceptionAddress)   

            elif ExceptionRecord.ExceptionCode == EXCEPTION_STACK_OVERFLOW:
                print('线程耗尽了其堆栈。') 
                print('异常地址为：',ExceptionRecord.ExceptionAddress)   

            a=input('捕获异常调试事件并处理完成！请继续……')

    # 仅供查看的完全进程托管模式
    def get_thread_context_new_only_see(self):
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
        DebugEvent=DEBUG_EVENT()
        while DebugEvent.dwDebugEventCode !=5:
            self.wait(-1,DebugEvent)
            self.PID=DebugEvent.dwProcessId
            self.TID=DebugEvent.dwThreadId
            self.thread_handle=self.get_thread_handle(self.TID)
            self.thread_hSnapshot_handle=self.get_hSnapshot_handle(TH32CS_SNAPTHREAD,self.PID)
            get_Snapshot_active=True
            context=CONTEXT()
            CONTEXT_CONTROL =           0x00100001      #获取
            CONTEXT_FULL =              0x0010000B
            CONTEXT_ALL =               0x0010001B
            CONTEXT_INTEGER =           0x00100002
            CONTEXT_SEGMENTS =          0x00010004
            context.ContextFlags=CONTEXT_FULL
            kernel32.SuspendThread(self.thread_handle)
            self.get_context(self.thread_handle,context)
            
            print(f'已获取线程句柄为{self.thread_handle}的寄存器信息，正在输出……')
            self.print_context(context)
            
            print(context)
            self.ContinueEvent(self.PID,self.TID)
            kernel32.ResumeThread(self.thread_handle)
            print(dic[DebugEvent.dwDebugEventCode])

    def bp_set(self,address,PID):
        '''
        设置断点的函数，必选参数有address、PID
        '''

        # 获取地址的原信息
        read_handle = self.get_process_handle(PID,PROCESS_VM_READ,mode=0)
        origin_buf = self.read_process_memory(address,2,read_handle)
        if not origin_buf:
            print('获取内存失败，已返回')
            return False
        
        # 写入断点信息
        write_handle = self.get_process_handle(PID,0x0028,mode=0)
        if not self.write_process_memory(address, b'H\xcc', write_handle):
            print('写入断点失败，已返回')
            return False
        
        #更新内存断点列表
        self.bp_list[address]=b'H\xCC'
        return True




if __name__ =='__main__':
    test=debugger()
    a=input('PID')
    a=eval(a)
    test.get_process_handle(PROCESS_ALL_ACCESS,a)
    print(kernel32.GetLastError())

