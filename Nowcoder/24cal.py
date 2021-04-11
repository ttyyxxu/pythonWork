import re
import itertools

numbers = ['106','100','204','200']
def calc24(numbers):
    for num in itertools.permutations(numbers):
        for ops in itertools.product(['+','-','*','/'],repeat=3):
            exp1 = '({0}{4}{1}){5}({2}{6}{3})'.format(*num, *ops)
            expr = '(('+num[0]+cal[0]+num[1]+')'+cal[1]+num[2]+')'+cal[2]+num[3]
            try:
                if eval(expr) == 24:
                    return expr
            except ZeroDivisionError:
                print("i got zero devision, pass")
                continue

    return None

print(calc24(numbers))

# print(calc24(numbers).replace('(','').replace(')',''))


