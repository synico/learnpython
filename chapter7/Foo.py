'''
Created on Apr 10, 2012

@author: 907729
'''

class Foo(object):
    def __init__(self, name):
        self.__name = name
    def bar(self):
        print("bar")
    def spam(self):
        Foo.bar(self)
        self.bar()
        print("spam")
        
    '''@property    
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string!")
        self.__name = value
    @name.deleter
    def name(self):
        raise TypeError("Can't delete name")'''    

if __name__ == "__main__":
    f = Foo("Guido")
    f.spam()
    n = f.name
    f.name = "Monty"
    print(f.name)
    '''f.name = 45
    del f.name'''
    
    print("*********************************")
    print(dir(object))
