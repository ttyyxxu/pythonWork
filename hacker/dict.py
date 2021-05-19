import math
import os
import random
import re
import sys
import itertools


def checkMagazine(magazine, note):
    mag_dict = {}
    for s in magazine:
        if s in mag_dict:
            mag_dict[s] += 1
        else:
            mag_dict[s] = 1

    for t in note:
        if t in mag_dict and mag_dict[t] > 0:
            mag_dict[t] -= 1
        else:
            return "No"

    return "Yes"

# print(checkMagazine("give me one grand today night","give one grand today"))
# print(checkMagazine("two times three is not four","two times two is four"))
#
# print(checkMagazine("ive got a lovely bunch of coconuts","ive got some coconuts"))


def countTriplets(arr, r):
    # [1,1,1,1,1,1,1]
    if r == 1:
        l = len(arr)
        print(l)
        return int(l*(l-1)*(l-2)/6)

    count = 0
    new_arr = []
    list_count = []
    dict_count = {}
    for num in arr:
        x = math.log(num,r)
        if float.is_integer(round(x,10)):
            new_arr.append(int(x))
    # i = 0..n-3,n-2,n-1
    # [1,2,3,3,4,4,5,5,6,6,6,7]
    print(new_arr)

    for n in new_arr:
        if n in dict_count:
            dict_count[n] += 1
        else:
            dict_count[n] = 1
    for m in set(new_arr):
        if m+1 in dict_count and m+2 in dict_count:
            count += dict_count[m]*dict_count[m+1]*dict_count[m+2]
    return count

    # for i in range(n-2):
    #     for j in range(i+1,n-1):
    #         if new_arr[i] + 1 != new_arr[j]:
    #             continue
    #         for k in range(j+1,n):
    #             if new_arr[j] + 1 == new_arr[k]:
    #                 count += 1
    #             elif new_arr[j] + 1 < new_arr[k]:
    #                 break

a = "1 17 80 68 5 5 58 17 38 81 26 44 38 6 12 11 37 67 70 16 19 35 71 16 32 45 7 39 2 14 16 78 82 5 18 86 61 37 12 8 27 90 13 26 57 24 36 4 52 67 71 71 11 51 48 42 57 16 43 58 29 58 8 20 24 25 15 84 61 78 53 49 39 66 75 6 51 72 9 13 49 79 45 21 1 2 63 20 17 67 39 45 86 46 26 19 70 2 64 2 79 78 51 28 53 87 85 14 68 55 78 78 5 32 9 57 85 71 76 11 9 25 17 4 32 42 74 64 5 47 65 83 34 77 72 49 73 66 24 13 82 11 90 86 4 8 53 88 40 38 8 48 24 76 13 56 79 86 29 83 4 3 37 38 42 19 48 24 46 71 36 38 81 88 85 46 57 47 43 7 85 50 16 70 87 29 35 75 24 63 67 28 28 13 27 69 83 36 54 39 16 52 38 58 49 32 13 15 79 55 73 35 66 89 14 62 79 11 46 64 73 74 1 62 86 79 40 79 24 4 79 1 17 26 58 65 19 32 79 59 86 62 55 23 22 31 84 10 41 1 73 75 74 36 47 70 76 48 20 62 13 8 62 29 85 82 3 65 23 44 34 71 67 88 3 50 28 49 59 30 49 3 15 85 90 23 26 76 70 45 9 45 14 70 35 60 23 90 34 46 43 29 78 71 79 42 30 16 52 50 8 63 52 22 57 14 6 82 89 37 88 7 81 11 38 26 32 61 77 27 68 81 56 17 61 44 58 52 21 20 11 28 82 24 11 10 37 16 1 87 53 50"
list_a = list(map(int,a.split()))

print(countTriplets([1,4,16,64],4))
print(countTriplets([1,3,9,9,27,81],3))
print(countTriplets([1,5,5,25,125],5))
print(countTriplets(list_a,3))

# what about [0, 4, 3, 2, 0, 2, 2, 1, 4, 3, 0, 0, 0, 1, 1, 1, 2, 4, 3, 4, 0]