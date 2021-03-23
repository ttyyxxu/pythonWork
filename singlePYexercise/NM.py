def baseN(num, b):
    res = ""
    if num > 0:
        while num:
            res = "0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZ"[num % b] + res
            num = num // b
        return res
    else:
        num = -num
        while num:
            res = "0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZ"[num % b] + res
            num = num // b
        return "-" + res

a, b = 17, 3
#a, b = map(int, input().split())
print(baseN(a, b))


if __name__ == '__main__':
    print('if, PyCharm',__name__)
else:
    print("else", __name__)