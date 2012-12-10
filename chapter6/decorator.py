'''
Created on Mar 30, 2012

@author: 907729
'''
import chapter7.Account

def eventhandler(btn):
    print('event handler... {0}'.format(''))
    def handler(func, *args, **kwargs):
        print("calling %s: %s, %s" % (func.__name__, args, kwargs))
        r = func(*args, **kwargs)
        return r
    return handler
    
@eventhandler
def handle_btn():
    print('handle btn')

if __name__ == '__main__':
    handle_btn()
