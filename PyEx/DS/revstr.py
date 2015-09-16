import sys

def revstr(str):
    rev = []
    for c in str[::-1]:
        rev.append(c)
    return rev

print ''.join(revstr(sys.argv[1]))
