from collections import Counter
from itertools import combinations

def makeAnagram(a,b):
    delete_needed = 0
    char_checked = []
    for s in a:
        if s in char_checked:
            continue
        else:
            delete_needed += abs(a.count(s) - b.count(s))
            char_checked.append(s)

    for t in b:
        if t not in char_checked:
            delete_needed += abs(a.count(t) - b.count(t))

    return delete_needed

# print(makeAnagram('cde','dcf'))
# print(makeAnagram('cde','abc'))


def isValid(s):
    word_counts = Counter(s)
    if len(s) <= 1:
        return "YES"
    freq = sorted(word_counts.values())

    if freq[0] == freq[-1]:
        return "YES"
    elif freq[0] == freq[-2] and freq[-2] == freq[-1] - 1:
        return "YES"
    elif freq[1] == freq[-1] and freq[0] == 1:
        return "YES"
    else:
        return "NO"


# print(isValid('aabbcd'))
# print(isValid('abcdefghhgfedecba'))


def substrCount(n, s):
    count = n
    for x in range(n):
        y = x
        while y < n - 1:
            y += 1
            if s[x] == s[y]:
                count += 1
            else:
                if s[x:y] == s[y+1:2*y-x+1]:
                    count += 1
                break

    return count

## logic is simple but very very slow
def commonChild_slow(s1, s2):
    s1_new = ''
    s2_new = ''
    for char1 in s1:
        if char1 in s2:
            s1_new = s1_new + char1
    for char2 in s2:
        if char2 in s1:
            s2_new = s2_new + char2

    for i in range(min(len(s1_new),len(s2_new)),0,-1):
        for child in combinations(s1_new,i):
            if child in combinations(s2_new,i):
                # print(child)
                return i
    return 0

def commonChild_too_hard_to_implement(s1, s2):
    longest = 0
    for pos_in_s1, start in enumerate(s1):
        child = ''
        pos_in_s2 = s2.find(start)
        if pos_in_s2 == -1:
            continue
        else:
            child = child + start
            for char in s1[pos_in_s1+1::]:
                new_pos_in_s2 = s2[pos_in_s2+1::].find(char)
                if new_pos_in_s2 != -1:
                    pos_in_s2 = new_pos_in_s2 + pos_in_s2 +1
                    child += char
                    print(child,pos_in_s2)
            if len(child) > longest:
                longest = len(child)
                print(child)
    return longest

def commonChild_still_too_slow(s1, s2):
    s1_new = ''
    s2_new = ''
    longest = 0
    for char1 in s1:
        if char1 in s2:
            s1_new = s1_new + char1
    for char2 in s2:
        if char2 in s1:
            s2_new = s2_new + char2
    print(s1_new,s2_new)
    for i in range(min(len(s1_new),len(s2_new)),0,-1):
        for child in combinations(s1_new,i):
            start = 0
            for char in child:
                shift = s2_new[start::].find(char)
                if shift == -1:
                    break
                else:
                    start += shift
            else:
                # print(child)
                if len(child) > longest:
                    return len(child)
    return 0

print(commonChild("AA","BB"))
print(commonChild("WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS","FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC"))