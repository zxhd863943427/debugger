# coding=utf-8
'''
NAME:仿照书本的进程枚举加寄存器状态获取
author:zx弘
version：1.0
'''
def main():
    def get_error(str):
        print(str,' 的报错代码是 ',kernel32.GetLastError())

    from defines.bash_debugger import bash_debugger,kernel32
    from defines.debugger_class import DEBUG_EVENT,CONTEXT,tagTHREADENTRY32
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


    test=bash_debugger()


    get_error('get_thread_handle(test.handle)')
    list1=[]
    test.PID=eval(input('请输入PID'))
    PID=test.PID
    test.thread_hSnapshot_handle=test.get_hSnapshot_handle(4,test.PID)
    get_error('test.get_hSnapshot_handle(')
    tag=tagTHREADENTRY32()
    test.get_thread_first_Snapshot(test.thread_hSnapshot_handle,tag)
    get_error('get_thread_first_Snapshot(')
    if tag.th32OwnerProcessID==test.PID:
        list1.append(tag.th32ThreadID)
    access=True
    while access:
        tag=tagTHREADENTRY32()
        access=test.get_thread_next_Snapshot(test.thread_hSnapshot_handle,tag)
        get_error('test.get_thread_next_Snapshot(')
        if tag.th32OwnerProcessID==test.PID:
            list1.append(tag.th32ThreadID)
    list1=list(set(list1))
    print(list1)







a=''
while a=='':
    main()
    a=input('回车继续……')