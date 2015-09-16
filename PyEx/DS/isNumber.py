import re

def isNum(str):
    if re.match(r'[+-]?\d+\.?\d+$', str):
        return 1
    else:
        return 0

if __name__ == '__main__':
    print isNum('123S004')
