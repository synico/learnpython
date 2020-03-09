#!/usr/bin/python3.8

from random import choice


def genAdd():
    result = set()
    for i in range(1, 20):
        for j in range(1, 20):
            if(i + j <= 30 and i + j >= 18):
                result.add(str(i) + " + " + str(j) + " = ")

    for x in range(10):
        test = choice(list(result))
        print(test)


def genSub():
    result = set()
    for i in range(1, 20):
        for j in range(1, 20):
            if(i - j >= 0):
                result.add(str(i) + " - " + str(j) + " = ")

    for x in range(20):
        test = choice(list(result))
        print(test)


genAdd()
print("=========================")
genSub()
