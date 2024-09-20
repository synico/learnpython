#!/usr/bin/python3.8

from sys import argv, path
import json

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(100)

print('==========python from import===========')
# print('path:', path)
for i in path:
    print(i.ljust(80) + "|")

print('==============start==============')
for i in argv:
    print(i)
print('==============end==============')

print(__name__)
