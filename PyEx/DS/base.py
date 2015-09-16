class Stack:
    stk = []
    __priv = 10

    def __init__(self):
        pass

    def push(self, n):
        self.stk.append(n)
        return n
    
    def pop(self):
        if len(self.stk) >= 1:
            item = self.stk[-1] 
            del self.stk[-1]
            return item
        else:
            return None

    def __str__(self):
        return str(self.stk)

    def getPriv(self):
        return self.__priv

stk = Stack()
stk.push(2)
stk.push(3)
stk.push(6)
stk.pop()
stk.pop()
stk.push(9)
print stk
print stk.getPriv()

