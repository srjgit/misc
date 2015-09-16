a = [2, 12, 22, 36]
b = [3, 10, 21, 39]
c = []

def mergesorted(a, b):
    i = j = 0
    while (i < len(a) and j < len(b)):
        #print 'i = %d, j = %d' %(i, j)
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    return c

print mergesorted(a, b)
