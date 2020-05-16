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


def loop3(map):
    it = iter(map)
    for key in it:
        print('key: ', key, ' ,value: ', map.get(key))


def mapMethod(map):
    if 1 in map:
        print('1 is in map')
    print('---------------key in dict-----------------')

    keys = map.keys()
    for key in keys:
        print('key: ', key)
    print('---------------dict.keys()-----------------')

    items = map.items()
    for item in items:
        print('item.key: ', item[0], ', item.value: ', item[1])
    print('---------------dict.items()-----------------')

    map.setdefault(6, 'six')
    map.setdefault(4, 'four')
    print(map.setdefault(8))
    print(map)
    print('---------------dict.setdefault(key[, value])-----------------')

    map.update(red=1, blue=2)
    print(map)
    print('---------------dict.update(key, value)-----------------')


if __name__ == '__main__':
    map = defineMap()
    mapMethod(map)
