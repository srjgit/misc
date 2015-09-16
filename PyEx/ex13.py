from sys import argv

script, fname = argv

txt = open(fname)
print txt

fname2 = raw_input("> ")
txt2 = open(fname2)

print txt2
