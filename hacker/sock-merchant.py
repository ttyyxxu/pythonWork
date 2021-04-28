import math
import os
import random
import re
import sys

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

def sockMerchant(n, ar):
    pairs = 0
    counted_colors = []
    for sock in ar:
        if sock not in counted_colors:
            pairs += math.floor( ar.count(sock) / 2)
            counted_colors.append(sock)
    return pairs

# print(sockMerchant(9, ar))


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes_old(q):
    bribes = 0
    for i in range(len(q)):
        climb = q[i] - (i+1)
        if climb > 2:
            print("Too chaotic")
            return
        elif climb > 0:
            bribes += climb
    print(int(bribes))

def minimumBribes(q):
    L = len(q)
    bribes = 0
    for pos,i in enumerate(q):
        climb = 0
        for j in range(pos+1,L):
            if i > q[j]:
                climb +=1
            if climb > 2:
                print("Too chaotic")
                return
        bribes += climb
    print(bribes)


minimumBribes([5,1,2,3,7,8,6,4])
minimumBribes([1,2,5,3,7,8,6,4])
