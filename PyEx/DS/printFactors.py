
def printFactors(num):
    i = num/2
    while i>= 2:
        if num%i == 0:
            print i, num/i
        i -= 1

if __name__ == '__main__':
    printFactors(12)

