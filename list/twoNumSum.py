#!/usr/bin/python3.8


# hashtable
def twoNumSum1(list, target):
    print("list: ", list)
    print("target: ", target)
    map = {}
    result = set()
    for index, value in enumerate(list):
        diff = target - value
        if value in map:
            result.add(index)
            result.add(map.get(value))
        map[diff] = index
    return result


if __name__ == '__main__':
    list = [2, 7, 11, 15]
    target = 9
    rst = twoNumSum1(list, target)
    print(rst)
