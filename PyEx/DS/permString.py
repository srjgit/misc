 
def permutations(word):
    if len(word) <= 1:
        return [word]

    perms = permutations(word[1:])
    #print '--------word: '+word+' perms: '+str(perms)
    char = word[0]
    result = []
    for perm in perms:
        print 'word: '+word+' perm: '+str(perm)
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])

    return result

def permute(str):
    for i in range(len(str)):
        for j in range(len(str)):
            tgt = list(str)
            tgt[i], tgt[j] = tgt[j], tgt[i]
            print ''.join(tgt)

if __name__ == '__main__':
    #permute('abcd')
    print permutations('abcd')

