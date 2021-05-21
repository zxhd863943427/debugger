    def get_thread_context_new_only_see(self,PID=None,TID=None,context=None,ContextFlags=CONTEXT_ALL):
        '''
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
                context = self.CONTEXT
            else:
                print("在无参数输入的的情况下未从结构体本身读取到输出结构体")
                return -3

                
        get_Snapshot_active=True
        context.ContextFlags=ContextFlags
        thread_handle = self.get_thread_handle(TID)
        kernel32.SuspendThread(thread_handle)
        self.get_context(thread_handle,context)            
        print(context)
        self.ContinueEvent(PID,TID)
        kernel32.ResumeThread(thread_handle)

        return context