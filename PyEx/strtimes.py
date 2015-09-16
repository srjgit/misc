def string_times(str, n):
    return str*n

def string_splosion(str):
    res = ''
    for i in range(len(str)):
        res += str[:i+1]
    return res

def readfile(file):
    f = open(file, "r")
    while(1):
        c = f.read()
        if not c: break
        print c + '='
    f.close()


#print string_times("Hi", 3)

#print string_splosion("Code")

readfile('tstfil')
