import sys
import csv

class AnalyzeMissing:
    def __init__(self, infile,  outfile):
        if len(sys.argv) < 2:
            print 'Usage: analyze.py <inputfile> <outputfile>'

        print 'setting {} {}'.format(infile, outfile)
        self.infile = infile
        self.outfile = outfile

ob = AnalyzeMissing(sys.argv[1], sys.argv[2])
input_iter = csv.DictReader(open(sys.argv[1]))

for row in input_iter:
    print input_iter[3]

