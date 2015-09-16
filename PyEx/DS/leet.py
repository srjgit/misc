from collections import defaultdict

class Solution:
    def __init__(self):
        self.idxpair = defaultdict(int)
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        for i in xrange(len(num)):
            self.idxpair[num[i]] = i
        for i in xrange(len(num)):
            num2 = target - num[i]
            if num2 != num[i] and num2 in self.idxpair and num2 != num[i]:
                return (i, self.idxpair[num2])

s = Solution()
#print s.twoSum([2, 7, 11, 15], 13)
print s.twoSum([0,4,3,0], 0)

