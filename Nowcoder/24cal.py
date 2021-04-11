import re
import itertools

numbers = ['1','3','4','5']
def calc24(numbers):
    for num in itertools.permutations(numbers):
        for cal in itertools.product(['+','-','*','/'],repeat=3):
            expr = '(('+num[0]+cal[0]+num[1]+')'+cal[1]+num[2]+')'+cal[2]+num[3]
            if eval(expr) == 24:
                return expr

    return None

print(calc24(numbers))

