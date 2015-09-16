import os
import sys
import re

if len(sys.argv) < 2:
    print 'path argument expected'
    sys.exit()

filepat = r".*\.csv"
files = os.walk(sys.argv[1])
for p in files:
    print type(p)
    m = re.match(r".*\.csv", p)
    if m:
        print p
        

