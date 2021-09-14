import zipfile
import string
import itertools
import os
filename = "fail.zip"

chars = string.digits + string.ascii_lowercase

def unzip (filename, password):
    try:
        with zipfile.ZipFile(filename) as zfile:
            zfile.extractall("./", pwd=password.encode('utf-8'))
        return True
    except:
        return False

for cc in itertools.permutations(chars, 3):
    secret = "".join(cc)
    if unzip (filename, secret):
        print(f"succeed with {secret}")
        break
    else:
        print(f"failed with {secret}")

