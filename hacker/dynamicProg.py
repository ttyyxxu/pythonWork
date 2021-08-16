import itertools

def maxSubsetSum(arr):
    pass

def maxPos(arr):
    sum = 0
    n = len(arr)
    maximun = (n + 1) // 2
    minimun = (n + 2) // 3

    for length in range (minimun, maximun+1):
        for indices in itertools.combinations(range(n),length):
            for ll in range(length):
                pass

def find_max_sum(arr):
    incl = 0
    excl = 0

    for i in arr:
        # Current max excluding i (No ternary in
        # Python)
        new_excl = excl if excl > incl else incl

        print("excl:",excl,"   incl:",incl)
        # Current max including i
        incl = excl + i
        excl = new_excl

    # return max of incl and excl
    return excl if excl > incl else incl


# Driver program to test above function
arr = [-100, 5, 10, 100, 10, 5, -200]
print(find_max_sum(arr))