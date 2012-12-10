'''
Created on May 24, 2012

@author: 907729
'''
import Account

class Test(Account.EvilAccount):
    pass

class TypedProperty():
    def __init__(self, name, type, default=None):
        self.name = "_" + name
        self.type = type
        self.default = default if default else type()
    def __get__(self, instance, cls):
        print("call __get__(%s, %s, %s)" % (self, instance, cls))
        return getattr(instance, self.name, self.default)
    def __set__(self, instance, value):
        print("call __set__(%s, %s, %s)" % (self, instance, value))
        if not isinstance(value, self.type):
            raise TypeError("Must be a %s" % self.type)
        setattr(instance, self.name, value)
    def __delete__(self, instance):
        #raise AttributeError("Can't delete attribute")
        print("call __del__(%s, %s):%s" % (self, instance, self.name))
        del self.name
        print(self.__dict__)
    
class Foo():
    name = TypedProperty("name", str)
    #print(name.__dict__)
    num = TypedProperty("num", int, 42)  
    #print(num.__dict__)
    '''def __init__(self):
        self.name = TypedProperty("name", str)
        #print(name.__dict__)
        self.num = TypedProperty("num", int, 42)  
        #print(num.__dict__)'''

if __name__ == "__main__":
    #print(Test.__mro__)
    f = Foo()
    f.action = "search"
    print("instance dictionary: %s" % (f.__dict__))
    print("class dictionary: %s" % (f.__class__.__dict__))
    #a = f.name #call __get__
    f.name = "Guido" #call __set__
    #del f.name
    #print(f.name) #call __get__
    print('#################################')
    #print(f.__class__.__dict__["num"].__dict__)
    instance = TypedProperty("ins", str, "test")
    instance.name = "_ns"
    print(instance.name)
    

