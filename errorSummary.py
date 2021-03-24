import re
from collections import deque

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
q = deque([0,0]*8,maxlen=8)
for i in range(8):
    q.append([0,0])

for error in re.findall(r'[a-zA-Z0-9]+\s[0-9]+',ERRORs):
    for i in range(8):
        if q[i][0] == error:
            q[i][1] += 1
            break
    else:
        q.append([error,1])

for ii in q:
    print(ii)