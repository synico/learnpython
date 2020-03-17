#!/usr/bin/python3.8


def defineList():
    list = [1, 2, 3, 4, 5]
    return list


def loop1(list):
    for index, value in enumerate(list):
        print('index: ', index, ' value: ', value)


def loop2(list):
    for i in list:
        print('value: ', i)


def listFunc(list):
    print('length of list:', len(list))
    print('max value in list: ', max(list))
    print('min value of list: ', min(list))


def listMethod(list):
    list.append(2)
    print('append object to list: ', list)
    print('count of 1 in list: ', list.count(2))
    lang = ('cn', 'en', 'fr')
    list.extend(lang)
    print('extends list: ', list)
    print('index of 2: ', list.index(2), ' index of cn: ', list.index('cn'))
    print('pop value from list: ', list.pop(8), ' list: ', list)
    print('reverse list: ', list.reverse(), list)
    print('sort list: ', list.sort(), list)


if __name__ == '__main__':
    list = defineList()
#    loop1(list)
#    loop2(list)
    listMethod(list)
