
'''
arr = [2, 4, 5, 1, 9, 12, 3]
k = 6
[(2,4), (5,1)]
'''

def getSumPairs(arr, k):
    results = []

    for i in arr:
        numpair = k - i
        if numpair in arr:
            results.append((i, numpair))

    return results

if __name__ == '__main__':
    arr = [2, 4, 5, 1, 9, 12, 3]
    print getSumPairs(arr, 6)

