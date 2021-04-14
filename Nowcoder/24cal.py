import re
import itertools

numbers = ['5','5','5','1']
def calc24(numbers):
    for num in itertools.permutations(numbers):
        for ops in itertools.product(['+','-','*','/'],repeat=3):
            exp1 = '({0}{4}{1}){5}({2}{6}{3})'.format(*num, *ops)
            exp2 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*num, *ops)
            exp3 = '{0}{4}({1}{5}({2}{6}{3}))'.format(*num, *ops)
            # expr = '(('+num[0]+cal[0]+num[1]+')'+cal[1]+num[2]+')'+cal[2]+num[3]
            for expr in exp1,exp2,exp3:
                try:
                    if abs(eval(expr) - 24) < 0.000001:
                        return expr
                except ZeroDivisionError:
                    # print("i got zero devision, pass")
                    continue
    return None

print(calc24(numbers))

# print(calc24(numbers).replace('(','').replace(')',''))


