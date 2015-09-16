def gcd(a, b):
    gcdnum = 1
    for i in xrange(1, min(a, b)+1):
        print a, b, i
        if a%i == 0 and b%i == 0:
            gcdnum = i
    return gcdnum

print gcd(13, 24)

