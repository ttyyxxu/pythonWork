import pandas as pd


# aa = pd.Series({"asdf":123,32:"ddd"})
# print(aa)

def isPalindrome(x: int):
    if x < 0:
        return False
    x_list = list(str(x))
    while len(x_list) >= 2:
        if x_list[0] == x_list[-1]:
            x_list = x_list[1:-1]
        else:
            return False
    return True



print(isPalindrome(1000021))

# 1 liner
# return str(x) == str(x)[::-1]