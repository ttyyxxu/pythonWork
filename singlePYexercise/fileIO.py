import pandas as pd
import numpy as np
import re
# file_DF = pd.read_csv("fileIO.txt", sep='\s+')
# print(file_DF)

dict_a = {}

regex = re.compile(r'([0-9]+)\s+([0-9a-z]+)\s+([0-9a-z]+)',flags=re.IGNORECASE)
with open("fileIO.txt", 'r') as fh:
    for line in fh:
        # print(line)
        m = regex.match(line)
        if m != None:
            qq, name, age = m.groups()
            dict_a[qq]=(name,age)
print(dict_a)