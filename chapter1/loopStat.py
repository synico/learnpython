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
        print("start to loop in range", i)
    else:
        print(i, "end of for loop")

    print("outer of for loop")


def forRange():
    for i in range(0, 10, 3):
        print("i in range: ", i)

def forContinue():
    for i in range(2, 10):
        if i % 2 == 0:
            print("i is even number: ", i)
            continue
        print("i is odd number:  ", i)

def forSwitch(point):
    match point:
        case "1":
            print("point is 1")
        case "2":
            print("point is 2")
        case "3":
            print("point is 3")
        case _:
            print("point is not in case")



# whileLoop()
# forLoop()
# forRange()
# forContinue()
forSwitch("1")
