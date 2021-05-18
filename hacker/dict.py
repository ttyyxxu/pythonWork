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
    dict_count = {}
    for num in arr:
        new_arr.append(int(math.log(num,r)))
    # i = 0..n-3,n-2,n-1
    # [1,2,3,3,4,4,5,5,6,6,6,7]
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


print(countTriplets([1,4,16,64],4))
print(countTriplets([1,3,9,9,27,81],3))