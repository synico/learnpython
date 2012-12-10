'''
Created on May 31, 2012

@author: 907729
'''
from chapter7.Account import EvilAccount
import shelve

my_account = EvilAccount("nick",200)
db = shelve.open("shelve_account")
db['key'] = my_account

obj = db['key']
obj.deposit(1000)
print(obj.inquiry())
db.close()

