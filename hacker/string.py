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

print(makeAnagram('cde','dcf'))
print(makeAnagram('cde','abc'))