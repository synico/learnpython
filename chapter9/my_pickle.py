'''
Created on May 31, 2012

@author: 907729
'''

from chapter7.Account import EvilAccount
import pickle

account = EvilAccount("Nick", 1000)
f = open('pickle_yaccount', 'wb')
pickle.dump(account, f)
f.close
