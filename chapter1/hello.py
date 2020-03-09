#!/usr/bin/python3.8

import sys

print("system info: " + sys.version)
print('Hello world')


def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]
    output = " ".join(inputWords)
    return output


result = reverseWords("I like Python")
print(result)
