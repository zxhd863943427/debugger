import ctypes
kernel32 = ctypes.windll.kernel32
print(kernel32.GetLastError())
dwProcessId=ctypes.c_longlong(eval(input('PID \n')))
kernel32.DebugActiveProcess(dwProcessId)
print(kernel32.GetLastError())
output=kernel32.DebugActiveProcessStop(dwProcessId)
print(kernel32.GetLastError())