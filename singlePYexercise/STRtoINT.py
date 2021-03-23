import re
def STRtoINT (s):
    regex = re.compile(r'^\s*[+|-]?[0-9]+')
    num = regex.search(s)
    if num != None:
        num_int = int(s[num.start():num.end()].lstrip(" +"))
        if num_int < -2 ** 31:
            return -2 ** 31
        elif num_int > 2 ** 31-1:
            return 2 ** 31-1
        else:
            return num_int
    else:
        return 0

print(STRtoINT(" wer -013"))