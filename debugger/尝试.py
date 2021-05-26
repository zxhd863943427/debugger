# coding=utf-8
from defines.main import debugger
from defines.bash_debugger import kernel32
from defines.consist import EXIT_PROCESS_DEBUG_EVENT,PROCESS_ALL_ACCESS
from defines.debugger_class import *
from ctypes import c_uint32, c_ulong
import _winapi as win

def read_process_memory(adress,length,handle):
    from ctypes import create_string_buffer
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


def write_process_memory(adress,data,handle):
    count = 0
    length = 2

    #c_data = c_char_p(data[count:])
    c_data = data

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

    handle=test.get_process_handle(pid,0x0010)

    test.read_process_memory(adress,36,handle)
    #print('读取的数据为',original_byte)
    a = input('继续……')
    # 写入数据
    handle=test.get_process_handle(pid,0x001F0FFF)
    test.write_process_memory(adress,b'H\xcc',handle)
    
    #return original_byte
    return True



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
    #win.CloseHandle(handle)
    kernel32.CloseHandle(handle)
    print('CloseHandle','error = ',kernel32.GetLastError())
    return address

c_char_p(b'msvcrt.dll')

i =1

test = debugger()
pid = eval(input('请输入PID'))
#pid=17092
print('附加的结果是',test.attach(pid))


printf_address = test.resolve_function(b'msvcrt.dll',b'printf')
print(printf_address)
print('resolve_function','error = ',kernel32.GetLastError())

print('第',i,'次','error = ',kernel32.GetLastError())

print('第',i,'次','error = ',kernel32.GetLastError())
print('地址为：',printf_address)
handle=test.get_process_handle(pid,0x0010)
original_byte=test.read_process_memory(printf_address,36,handle)
print('设置断点前读取的数据为',original_byte)
if test.bp_set(printf_address,pid):
    print('继续')
else:
    print('设置断点失败……')
handle=test.get_process_handle(pid,0x0010)
original_byte=read_process_memory(printf_address,36,handle)

print('设置断点后读取的数据为',original_byte)
a=input('准备退出……')

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


while debug.dwDebugEventCode!=EXIT_PROCESS_DEBUG_EVENT  and i<=50:
    i+=1
    print(dic[debug.dwDebugEventCode])
    test.wait(-1,debug)
    print('已暂停，即将继续')
    print('test.wait','error = ',kernel32.GetLastError())
    test.ContinueEvent(debug.dwProcessId,debug.dwThreadId)
    print(debug.dwDebugEventCode)
    print('第',i,'次','error = ',kernel32.GetLastError())
a=input('准备退出……')


test.debugStop(pid)