#!/usr/bin/python3.8


def whileLoop():
    i = 1
    while(i < 10):
        i = i + 1
        print(i)
    else:
        print('i is greater than 10')


def forLoop():
    for i in range(5):
        print("start to loop in range")
    else:
        print("end of for loop")

    print("outer of for loop")


def forRange():
    for i in range(0, 10, 3):
        print("i in range: ", i)


# whileLoop()
# forLoop()
forRange()
