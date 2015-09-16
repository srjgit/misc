import csv

new_addr = set([record[0] for record in csv.reader(open('newadd.csv'))])

old_addr = set([line.strip() for line in open('oldadd.txt')])

print old_addr.intersection( new_addr )
