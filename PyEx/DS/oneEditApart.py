import sys

def OneEditApart(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    maxlen = len(str2) if len(str2) > len(str1) else len(str1)

    set1 = set(str1)
    set2 = set(str2)
    interset = set1.intersection(set2)
    print maxlen, len(interset), interset

    if len(interset) == maxlen:
        return False
    elif len(interset) == maxlen-1:
        return True
    else:
        return False


if __name__ == "__main__":
    print OneEditApart(sys.argv[1], sys.argv[2])

