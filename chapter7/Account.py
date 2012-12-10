'''
Created on Apr 10, 2012

@author: 907729
'''
import random

class Account(object):
    '''
    classdocs
    '''
    num_accounts = 0

    def __init__(self, name, balance):
        '''
        Constructor
        '''
        self.name = name
        self.balance = balance
        Account.num_accounts += 1
        
    def __del__(self):
        Account.num_accounts -= 1
        
    def deposit(self, amt):
        self.balance = self.balance + amt
        
    def withdraw(self, amt):
        self.balance = self.balance - amt
    
    def inquiry(self):
        return self.balance

class EvilAccount(Account):
    def inquiry(self):
        self.withdraw(10)
        if random.randint(0, 4) == 1:
            return self.balance * 2.1
        else:
            return self.balance
        
 
if __name__ == '__main__':
    print(EvilAccount.__mro__)
    '''a = EvilAccount("Nick", 1000.00)
    idx = 0
    while idx < 3:
        idx += 1
        print(EvilAccount.inquiry(a), a.name, a.inquiry())'''
        