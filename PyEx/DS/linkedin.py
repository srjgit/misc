import re
from collections import deque

class Node:
    data = None
    left = None
    right = None
    q = deque()

    def __init__(self, data):
        self.data = data

    def addNode(self, data):
        if data <= self.data :
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.addNode(data)

        elif data > self.data :
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.addNode(data)

    def dfs(self):
        if self:
            print self.data, " "
            if self.left:
                self.left.dfs() 
            if self.right:
                self.right.dfs() 

    def bfs(self):
        print 'printing bfs.......'
        if self:
            self.q.append(self)
        while(len(self.q)>0):
            #print self.data
            curr = self.q.popleft()
            print curr.data
            if curr.left:
                self.q.append(curr.left)
            if curr.right:
                self.q.append(curr.right)

    def searchTree(self, key):
        curr = self
        while curr: 
            if curr.data == key:
                return 1
            elif key <= curr.data:
                curr = curr.left
            elif key >= curr.data:
                curr = curr.right
        return 0

    def getFirstCommonAncestor(root, A, B):
        if root is None:
            return None                
       
        if(root.left.searchTree(A) and root.right.searchTree(B)):
            return root
       
        L = getFirstCommonAncestor(root.left, A, B)
        R = getFirstCommonAncestor(root.right, A, B)
       
        if L != None:
            return L
        if R != None:
            return R
   
        return None
        

def recIsPalindrome(str):
    if len(str) <= 1:
        return 1
    if str[0] == str[-1] and recIsPalindrome(str[1:-1]):
        return 1
    else:
        return 0

def isPalindrome(str):
    i, j = 0, len(str)-1
    while i<j:
        if not str[i] == str[j]:
            return 0
        print i, j 
        i += 1; j -= 1
    return 1


def findPalindrome(str):
    i, j, k = 0, len(str), 0
    lPal = ''
    while k<len(str)-1:
        while j>=k:
            if isPalindrome(str[k:j]) and len(lPal) < len(str[k:j]):
                lPal = str[k:j]
            #print 'processing ',str[k:j], lPal
            j -= 1
        k += 1
        j = len(str)
    return lPal
        
def isNumber(str):
    #if re.match(r'[+-]?\d+\.?\d+$', str):
    #    return 1
    #else:
    #    return 0
    flag = True
    for c in str:
        if not (ord(c) >= ord('0') and ord(c) <= ord('9')):
            flag = False
    return flag

def findElemSortedArr(arr, num):
    low, high = 0, len(arr)
    
    while low <= high:
        mid = (low+high)/2
        if arr[mid] == num:
            return mid
        if arr[low] <= arr[mid]: #left half is sorted
            if arr[low] <= num and num <= arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid] < num and num <= arr[high-1]:
                low = mid+1
            else:
                high = mid-1

    return None

def findTriangleEdges(arr):
    i,j,k = 0,1,2
    arr = sorted(arr)
    while True:
        if i > len(arr)-3:
            break

        if (arr[i] + arr[j] > arr[k]) and \
            (arr[j] + arr[k] > arr[i]) and \
            (arr[i] + arr[k] > arr[j]):
            return [arr[i], arr[j], arr[k]]

        i += 1; j += 1; k += 1

    return []

def findMaxSum(arr):
    currSum = 0
    maxSum = 0
    for num in arr:
        currSum += num
        maxSum = max(maxSum, currSum)
        if currSum <= 0:
            currSum = 0
        
    return maxSum

def maxSumSubSeq(arr):
    currSum, maxSum = 0, arr[0]

    for i, num in enumerate(arr):
        currSum += num
        if currSum <= 0:
            currSum = 0
        else:
            maxSum = max(currSum, maxSum)
    return maxSum


def minDistance(str, w1, w2):
    for w in str.split():
        print w

def parenMatch(str, prev):
    if(len(str) >= 1):

        ch = str[0]
        if ch == '(':
            return parenMatch(str[1:], ch)
        elif ch == ')':
            if len(str) >= 2:
                return parenMatch(str[1:], ch)
            else:
                return 1
        if ch == prev:
            return 1
        else:
            return 0

        
if __name__ == '__main__':
    arr = [10, 2, -7, 6, 4, 5]
    #print findTriangleEdges(arr)
    #print findElemSortedArr([6,7,8,2,3,4], -3)
    #print isNumber('1235')
    #print 'found lPal: '+findPalindrome('abxcba')
    #print 'recursive isPalindrome: ',recIsPalindrome('civic')

    tree = Node(20)
    tree.addNode(30)
    tree.addNode(15)
    tree.addNode(10)
    tree.addNode(22)
    #tree.dfs()
    tree.bfs()
    #tree.getFirstCommonAncestor(10, 22)
    #print 'search22 - ',tree.searchTree(222)
    #print tree.data, tree.left.data, tree.left.left.data, tree.right.data

    #print 'maxSum:', findMaxSum(arr)
    #minDistance("hello how are you", 'hello', 'you')
    #print 'maxSumSubSeq:', maxSumSubSeq(arr)
    #print parenMatch('(((())))') 
    print parenMatch('(()', '') 
     
