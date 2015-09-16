def list_sum(num_list):
    sum = 0
    for num in num_list:
        sum = sum + num

    return sum

i = 0
def rec_list_sum(num_list):
    global i 
    i+=1
    print "iter: %d" %(i)
    if len(num_list) == 1:
        return num_list[0]

    return num_list[0] + rec_list_sum(num_list[1:]) 

def call_fact():
    num = int(input('enter a number:'))
    if num == 0:
        print "fact of 0 is 1"
    elif num < 0:
        print "cannot compute fact for negative num"
    else:
        print "fact of %d is %d" %(num, rec_fact(num))

def rec_fact(num):
    if num == 1:
        return 1
    else:
        return num*rec_fact(num - 1)

def rec_prime(n, i):
    if n == 0 or n == 1 or n < 0: 
        return False
    elif i == n:
        return True
    elif n % i == 0:
        return False
    else:
        return rec_prime(n, i + 1)

def count_vowels(str):
    vowels = set('aeiou')
    vcounter = {}.fromkeys(vowels, 0)
    str = str.lower()

    for c in str: 
        if c in vowels:
            vcounter[c] += 1
    return vcounter

def is_palindrome(str):
    l = len(str)
    for i in xrange(l/2):
        print i, str[i], str[l-i-1]
        if str[i] != str[l-i-1]:
            return False
    return True    

print list_sum([1, 2, 5])
print rec_list_sum([1, 2, 5])
#call_fact()
print rec_prime(17, 2)
print count_vowels('Anoushka Nair')
print is_palindrome('malayalamm')

