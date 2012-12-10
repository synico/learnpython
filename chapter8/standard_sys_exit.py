'''
Created on May 30, 2012

@author: 907729
'''

import sys
import optparse

if __name__ == '__main__':
    p = optparse.OptionParser()
    p.add_option("-x")
    p.add_option("-y")
    opts, args = p.parse_args()
    print(opts)
    if len(sys.argv) != 3:
        sys.stderr.write("Usage : python %s inputfile outputfile\n" % sys.argv[0])
        raise SystemExit(1)
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    
