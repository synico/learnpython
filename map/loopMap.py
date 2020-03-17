#!/usr/bin/python3.8


def defineMap():
    map = {1: 'a', 2: 'b', 3: 'c'}
    return map


def loop1(map):
    for i in map:
        print('key: ', i, ', value: ', map[i])


# loop entry as tuple
def loop2(map):
    for (k, v) in map.items():
        print('tuple | key: ', k, ', value: ', v)


if __name__ == '__main__':
    map = defineMap()
    loop2(map)
