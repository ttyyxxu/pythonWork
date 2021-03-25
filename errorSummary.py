import re
from collections import deque


class errorandCount(object):
    def __init__(self, error, count):
        self.error = error
        self.count = count

    def add1(self):
        self.count += 1

    def __str__(self):
        return self.error + " " + str(self.count)


ERRORs = r'''D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645
E:\je\rzuwnjvnuz 633
C:\km\tgjwpb\gy\atl 637
F:\weioj\hadd\connsh\rwyfvzsopsuiqjnr 647
E:\ns\mfwj\wqkoki\eez 648
D:\cfmwafhhgeyawnool 649
E:\czt\opwip\osnll\c 637
G:\nt\f 633
F:\fop\ywzqaop 631
F:\yay\jc\ywzqaop 631'''
q = deque(maxlen=8)
for i in range(8):
    q.append(errorandCount("",0))

for error in re.findall(r'[a-zA-Z0-9]+\s[0-9]+', ERRORs):
    for i in range(8):
        if q[i].error == error:
            q[i].add1()
            break
    else:
        q.append(errorandCount(error,1))

for ii in q:
    print(ii)
