'''
Created on May 28, 2012

@author: 907729
'''

class AttrAccessSequence(object):
    classAttr = "attribute on class"
    
if __name__ == "__main__":
    aas = AttrAccessSequence()
    aas.instanceAttr = "attribute on instance"
    aas.classAttr = "attribute on instance"
    print(aas.__dict__)
    
