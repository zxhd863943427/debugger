# coding=utf-8
'''
NAME:尝试使用获取上下文模块
author:zx弘
version：1.0
'''

from defines.main import debugger

test = debugger()
a=eval(input('输入PID'))
test.attach(a)
test.get_thread_context_new()
test.debugStop(a)