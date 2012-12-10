'''
Created on May 31, 2012

@author: 907729
'''

f = open("test","r+")
f.write("1st line")

src_file = open("file_access.py", "r")
f.writelines(src_file.readlines())
print(f.__next__())
f.close()
print(f.closed)
