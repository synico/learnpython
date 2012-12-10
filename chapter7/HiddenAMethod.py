'''
Created on Jul 2, 2012

@author: 907729
'''

class C(object):
    def f(self):
        return "f defined in class"
    
cobj = C()

print(cobj.f())

def another_f():
    print('another f')
    return "another f"

cobj.f = another_f

cobj.f()