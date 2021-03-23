
def findLongestSub(s):
    if len(s) < 2:
        return len(s)
    longestSub = ""
    curr_sub = ""
    for i in range(len(s)):
        idx_dup = curr_sub.find(s[i])
        if idx_dup == -1:
            curr_sub = curr_sub + s[i]
        else:
            if len(curr_sub) > len(longestSub):
                longestSub = curr_sub
            if idx_dup < len(curr_sub) - 1:
                curr_sub = curr_sub[idx_dup+1::]+s[i]
            else:
                curr_sub = s[i]
    return max(len(longestSub), len(curr_sub))


print(findLongestSub("a123456ab2cddg"))



