#!/usr/bin/python3.8

from sys import argv, path


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(100)

print('==========python from import===========')
print('path:', path)

print('==============start==============')
for i in argv:
    print(i)
print('==============end==============')
