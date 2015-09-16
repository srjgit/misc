
def largestContinuousSum(arr):
    currMax = arr[0]
    for num in arr[1:]:
        if currMax < currMax+num:
            currMax += num

def largestSum(arr):
    if len(arr) == 0:
        return

    maxSum = currentSum = arr[0]
    for num in arr[1:]:
        currentSum = max(currentSum+num, num)
        maxSum = max(currentSum, maxSum)

    return maxSum

if __name__ == '__main__':
    arr = [2, 4, -5, 1, -1, 12, 3]
    #print largestContinuousSum(arr)
    print largestSum(arr)

