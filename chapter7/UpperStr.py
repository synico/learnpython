'''
Created on May 25, 2012

@author: 907729
'''
class UpperStr(str):
    '''def __new__(cls, value=""):
        return str.__new__(cls, value.upper())'''
    def __init__(self, value):
        self = value.upper()
        value = value.upper()
        print(self)
    
if __name__ == "__main__":
    u = UpperStr("hello")
    print(u)
