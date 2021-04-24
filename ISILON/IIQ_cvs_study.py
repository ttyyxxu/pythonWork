import csv
import re
from collections import abc

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, abc.Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x, ignore_types)
        else:
            yield x

with open('ext_net_client_taisilon1_1618560860.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        pass
        # print(row)
# print(headers)

## 利用flatten
# IPs = flatten([re.findall(r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)',ip) for ip in headers])
# print([ip for ip in IPs])

IPs = [x[0] for x in [re.findall(r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)',ip) for ip in headers] if len(x) ==1]
print(len(IPs))

IPs_10_33 = [x[0] for x in [re.findall(r'(10\.33\.[0-9]+\.[0-9]+)',ip) for ip in headers] if len(x) ==1]
print(len(IPs_10_33))