'''
Created on May 24, 2012

@author: 907729
'''

import math

class Circle(object):
    '''
    classdocs
    '''


    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi*self.radius**2
    @property
    def perimeter(self):
        return math.pi*self.radius*2
    
if __name__=='__main__':
    c = Circle(4)
    print("Area: %s" % c.area)
    print("Perimeter: %s" % c.perimeter)
            