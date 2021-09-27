def stepPerms_inner(n,d):
    if n in d.keys():
        return d[n]
    else:
        value = stepPerms_inner(n-3,d)+stepPerms_inner(n-2,d)+stepPerms_inner(n-1,d)
        d[n] = value
        return value


def stepPerms(n):
    return stepPerms_inner(n,{1:1, 2:2, 3:4})


print(stepPerms(35))