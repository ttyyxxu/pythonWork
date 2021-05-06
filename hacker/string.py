from collections import Counter

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


print(isValid('aabbcd'))
print(isValid('abcdefghhgfedecba'))
