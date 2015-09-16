import random

def rand7():
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    return (a + b) % 7

print rand7()
print rand7()
print rand7()
print rand7()
