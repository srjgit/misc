
def removeDupChars(str):
    bFlags = [False]*128
    retstr = ''
    for c in str:
        if not bFlags[ord(c)]:
            retstr = retstr+c
            bFlags[ord(c)] = True

    return retstr

def removeDupChars2(str):
    seenChar = {}
    retstr = ''
    for c in str:
        if not seenChar.has_key(c):
            seenChar[c] = 1
            retstr = retstr+c
    return retstr

if __name__ == '__main__':
    print removeDupChars2('hello yellow')
