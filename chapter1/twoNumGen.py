#!/usr/bin/python3.8

from random import choice


def genAdd():
    result = set()
    for i in range(5, 50):
        for j in range(9, 20):
            if(i + j <= 99 and i + j >= 18):
                result.add(str(i) + " + " + str(j) + " = ")

    for x in range(20):
        test = choice(list(result))
        print(test)


def genSub():
    result = set()
    for i in range(11, 50):
        for j in range(9, 20):
            if(i - j >= 9):
                result.add(str(i) + " - " + str(j) + " = ")

    for x in range(20):
        test = choice(list(result))
        print(test)


genAdd()
print("=========================")
genSub()
