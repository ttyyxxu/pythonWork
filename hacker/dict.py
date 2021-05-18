import math
import os
import random
import re
import sys


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

print(checkMagazine("give me one grand today night","give one grand today"))
print(checkMagazine("two times three is not four","two times two is four"))

print(checkMagazine("ive got a lovely bunch of coconuts","ive got some coconuts"))
