'''
Created on Apr 10, 2012

@author: 907729
'''

import Account
import sys


class Desc(object):
    "A descriptor example that just demonstrates the protocol"

    def __get__(self, obj, cls=None):
        print("call get: %s" % obj)

    def __set__(self, obj, val):
        print("call set: %s" % val)

    def __delete__(self, obj):
        print("call delete")


class C(object):
    "A class with a single descriptor"
    d = Desc()


if __name__ == '__main__':
    a = Account.Account("Nick", 1000.00)
    print(a.inquiry())
    cobj = C()

    x = cobj.d
    # C.d = "assign"
    # print(C.__dict__)
    cobj.d = "setting a value"
    cobj.__dict__['d'] = "try to force a value"
    x = cobj.d
    del cobj.d

    x = C.d
    C.d = "setting a value on class"
    # print(sys.modules)
