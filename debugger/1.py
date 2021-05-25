from ctypes import cdll,c_char_p
from time import sleep
msvcrt = cdll.msvcrt
counter = 0

while True:
    str1 = c_char_p(b'this is test for read!')
    msvcrt.printf(str1)
    msvcrt.printf(b'\n')
    sleep(2)
    counter += 1
