'''
This is the initial function, which runs slowly
as it clearly shows each step
but the exercise only needs a number of steps
'''
def miniswap1(arr):
    steps = 0
    for i in range(len(arr)):
        if arr[i] != i + 1:
            pos = arr.index(i + 1)
            arr[pos], arr[i] = arr[i], arr[pos]
            steps += 1
            # print(steps, arr)
    return steps

'''
Optimized efficiency with a mapping list.
'''
def miniswap(arr):
    steps = 0
    mapping = [0]*(len(arr)+1)
    for pos, i in enumerate(arr):
        mapping[i] = pos

    print(mapping)

    for i in range(len(arr)):
        if arr[i] != i + 1:
            pos = mapping[i+1]
            mapping[arr[i]] = pos
            arr[pos], arr[i] = arr[i], arr[pos]
            steps += 1
            # print(steps, arr)
    return steps


# long list should be 91 swaps
longlist = [8, 45, 35, 84, 79, 12, 74, 92, 81, 82, 61, 32, 36, 1, 65, 44, 89, 40, 28, 20, 97, 90, 22, 87, 48, 26, 56, 18, 49, 71, 23, 34, 59, 54, 14, 16, 19, 76, 83, 95, 31, 30, 69, 7, 9, 60, 66, 25, 52, 5, 37, 27, 63, 80, 24, 42, 3, 50, 6, 11, 64, 10, 96, 47, 38, 57, 2, 88, 100, 4, 78, 85, 21, 29, 75, 94, 43, 77, 33, 86, 98, 68, 73, 72, 13, 91, 70, 41, 17, 15, 67, 93, 62, 39, 53, 51, 55, 58, 99, 46]
longlist1 = [8, 45, 35, 84, 79, 12, 74, 92, 81, 82, 61, 32, 36, 1, 65, 44, 89, 40, 28, 20, 97, 90, 22, 87, 48, 26, 56, 18, 49, 71, 23, 34, 59, 54, 14, 16, 19, 76, 83, 95, 31, 30, 69, 7, 9, 60, 66, 25, 52, 5, 37, 27, 63, 80, 24, 42, 3, 50, 6, 11, 64, 10, 96, 47, 38, 57, 2, 88, 100, 4, 78, 85, 21, 29, 75, 94, 43, 77, 33, 86, 98, 68, 73, 72, 13, 91, 70, 41, 17, 15, 67, 93, 62, 39, 53, 51, 55, 58, 99, 46]

print(miniswap([7, 1, 3, 2, 4, 5, 6]))
print(miniswap1([7, 1, 3, 2, 4, 5, 6]))

print(miniswap([2, 3, 4, 1, 5]))
print(miniswap1([2, 3, 4, 1, 5]))

print(miniswap(longlist))
print(miniswap1(longlist1))
print(miniswap([2,1,4,3]))

'''
Let's focus on a more efficient way
we divide it into 3 types
1. good one, no need to swap
2. can be swap with pairs
3. not in pairs

Yet later on, I find no shortcut to get the steps
'''

# def minimunswap(arr):
#     steps = 0
#     no_pairs = 0
#     pairs = 0
#     for i in range(len(arr)) :
#         if arr[i] != i + 1:
#             if arr[arr[i]-1] == i+1:
#                 pairs += 1
#                 arr[arr[i] - 1] = arr[i]
#             else:
#                 no_pairs += 1
#     if no_pairs > 0:
#         return no_pairs-1 + pairs
#     else:
#         return pairs
