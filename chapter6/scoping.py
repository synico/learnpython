'''
Created on Mar 30, 2012

@author: 907729
'''

n = 9
def countdown(start):
    n = start
    def display():
        print("T-minus %d" % n)
    def decrement():
        nonlocal n
        n -= 1
    while n > 0:
        display()
        decrement()
        

if __name__ == '__main__':
    countdown(10)