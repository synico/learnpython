'''
Created on Aug 5, 2012

@author: 907729
'''

import optparse
p = optparse.OptionParser()

#this option receives one parameter
p.add_option("-o", action="store", dest="outfile")
p.add_option("--output", action="store", dest="outfile")

#this option set a flag
p.add_option("-d", action="store_true", dest="debug")
p.add_option("--debug", action="store_true", dest="debug")

#set default value
p.set_defaults(debug=False)

#parse input
opts, args = p.parse_args()

#set options
outfile = opts.outfile
debugmode = opts.debug

print('outfile: ', outfile, ', debugmode: ', debugmode)

if __name__ == '__main__':
    pass