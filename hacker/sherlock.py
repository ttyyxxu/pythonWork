def getsubstring(s="abcmdaba"):
    n = len(s)
    for ll in range(n-1,0,-1):
        print("len=",ll)
        for i in range(n-ll+1):
            yield(s[i:i+ll])
print(list(getsubstring("kkkk")))

a: 0,5,7
b: 1,6
c: 2
m: 3
d: 4
