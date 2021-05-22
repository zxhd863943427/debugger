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
                print('异常地址为：',ExceptionRecord.ExceptionAddress)

            if ExceptionRecord.ExceptionCode == EXCEPTION_GUARD_PAGE:
                print('触发内存保护页断点')
                print('异常地址为：',ExceptionRecord.ExceptionAddress) 

            if ExceptionRecord.ExceptionCode == EXCEPTION_ACCESS_VIOLATION:
                print('线程试图读取或写入对其没有适当访问权限的虚拟地址。') 
                print('异常地址为：',ExceptionRecord.ExceptionAddress)                  


            if ExceptionRecord.ExceptionCode == EXCEPTION_FLT_STACK_CHECK:
                print('浮点运算的结果是堆栈上溢或下溢。') 
                print('异常地址为：',ExceptionRecord.ExceptionAddress)   

            if ExceptionRecord.ExceptionCode == EXCEPTION_STACK_OVERFLOW:
                print('线程耗尽了其堆栈。') 
                print('异常地址为：',ExceptionRecord.ExceptionAddress)   

            a=input('捕获异常调试事件并处理完成！请继续……')