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


print(list(itertools.permutations(range(5),3)))

print(list(itertools.combinations(range(5),3)))