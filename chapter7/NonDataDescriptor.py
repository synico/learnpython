'''
Created on May 28, 2012

@author: 907729
'''

class GetOnlyDesc(object):
    "Another useless descriptor"
    
    def __get__(self, obj, type=None):
        pass

class C(object):
    "A class with a single descriptor"
    d = GetOnlyDesc()
    

if __name__ == "__main__":
    cobj = C()
    x = cobj.d
    print("1: %s" % x)
    cobj.d = "setting a value"
    print("2: %s" % cobj.d)
    del cobj.d
    
    x = C.d
    print("3: %s" % x)
    print("4: %s" % C.__dict__)
    C.d = "setting a value on class"
    print("5: %s" % C.__dict__)
