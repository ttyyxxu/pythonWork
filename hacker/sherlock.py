def getsubstring(s="abcmdaba"):
    n = len(s)
    count = 0
    for ll in range(1,n):
        # print("len=",ll)
        d = {}
        for i in range(n-ll+1):
            ss = s[i:i+ll]
            sorted_ss = ''.join(sorted(ss))
            for kk in d.keys():
                if sorted_ss == kk:
                    d[kk] += 1
                    break
            else:
                d[sorted_ss] = 1
        # print(d)
        for v in d.values():
            if v > 1:
                count += v * (v-1) / 2
    return int(count)

print(getsubstring("cdcd"))
print(getsubstring("kkkk"))
print(getsubstring("ifailuhkqq"))
'''
a: 0,5,7
b: 1,6
c: 2
m: 3
d: 4
'''