# coding=utf-8
from defines.main import debugger
from defines.bash_debugger import kernel32
from defines.consist import EXIT_PROCESS_DEBUG_EVENT,PROCESS_ALL_ACCESS
from defines.debugger_class import *
from ctypes import c_uint32, c_ulong, create_string_buffer

def read_prcess_memory(handle,adress,length):
    data = b''
    read_buf = create_string_buffer(length)
    count = 0

    kernel32.ReadProcessMemory.argtypes = [HANDLE,LPVOID,LPVOID,SIZE_T,SIZE_T]
    kernel32.ReadProcessMemory.restype = BOOL
    if not kernel32.ReadProcessMemory(
        handle,
        adress,
        read_buf,
        length,
        count):
        print("读取内存失败……")
        print('WriteProcessMemory','error = ',kernel32.GetLastError())
        return False
    
    else:
        data += read_buf.raw
        return data


def write_prcess_memory(handle,adress,data):
    count = 0
    length = len(data)

    c_data = c_char_p(data[count:])

    kernel32.WriteProcessMemory.argtypes = [HANDLE,LPVOID,LPVOID,SIZE_T,SIZE_T]
    kernel32.WriteProcessMemory.restype = BOOL   
    if not kernel32.WriteProcessMemory(
        handle,
        adress,
        c_data,
        length,
        count):
        print('写入失败内存……')
        print('WriteProcessMemory','error = ',kernel32.GetLastError())
        return False
    else:
        return True

def bp_set(pid,adress):

    handle=test.get_process_handle(pid,0x001F0FFF)

    original_byte=read_prcess_memory(handle,adress,12)
    print('读取的数据为',original_byte)
    a = input('继续……')
    # 写入数据
    handle=test.get_process_handle(pid,0x001F0FFF)
    write_prcess_memory(handle,adress,b'\xCC')

    list1 =[(adress,original_byte)]
    if list1 != None:
        return list1
    try:
        # 备份数据
        original_byte=read_prcess_memory(handle,adress,1)
        print('读取的数据为',original_byte)
        a = input('继续……')
        # 写入数据
        write_prcess_memory(handle,adress,b'H\xCC')

        list1 =[(adress,original_byte)]
        return list1
    except :
        return False

def resolve_function(dll, func):
    kernel32.GetModuleHandleA.argtypes = [c_char_p]
    kernel32.GetModuleHandleA.restype = c_void_p
    handle = kernel32.GetModuleHandleA(dll)
    print('GetModuleHandleA','error = ',kernel32.GetLastError())
    print(handle)
    kernel32.GetProcAddress.argtypes = [c_void_p,c_char_p]
    kernel32.GetProcAddress.restype = c_void_p    
    address = kernel32.GetProcAddress(handle, func)
    print('GetProcAddress','error = ',kernel32.GetLastError())
    kernel32.CloseHandle.argtypes = [c_void_p]
    kernel32.CloseHandle.restype = BOOL
    kernel32.CloseHandle(handle)
    return address

c_char_p(b'msvcrt.dll')

i =1

test = debugger()
#pid = eval(input('请输入PID'))
pid=524
print('附加的结果是',test.attach(pid))


printf_address = resolve_function(b'msvcrt.dll',b'printf')
print(printf_address)
print('resolve_function','error = ',kernel32.GetLastError())

print('第',i,'次','error = ',kernel32.GetLastError())

print('第',i,'次','error = ',kernel32.GetLastError())
print('地址为：',printf_address)

if bp_set(pid,printf_address):
    print('继续')
else:
    print('设置断点失败……')
handle=test.get_process_handle(pid,0x0010)
original_byte=read_prcess_memory(handle,printf_address,12)
print('读取的数据为',original_byte)

debug = DEBUG_EVENT()


i=0
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

'''
while debug.dwDebugEventCode!=EXIT_PROCESS_DEBUG_EVENT  and i<=33:
    i+=1
    print(dic[debug.dwDebugEventCode])
    test.wait(-1,debug)
    print('已暂停，即将继续')
    test.ContinueEvent(debug.dwProcessId,debug.dwThreadId)
    print(debug.dwDebugEventCode)
    print('第',i,'次','error = ',kernel32.GetLastError())
a=input('准备退出……')
'''

test.debugStop(pid)