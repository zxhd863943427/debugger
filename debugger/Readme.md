# 这是崩溃的调试器开发笔记

## 5.26
我终于知道为什么在vs code里跑的好好的内存操作函数到了IDE里就是不行了！
首先，是函数的输入格式  
其次，是调用dll的句柄。  
readProcessMemory只需要 **PROCESS_VM_READ** 权限就可以读取，但是WriteProcessMemory 不仅要**PROCESS_VM_WRITE**，还要**PROCESS_VM_OPERATION**，老实来说，还是直接用**PROCESS_ALL_ACCESS**算了。  
