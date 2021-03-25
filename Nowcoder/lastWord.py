import re

LINES = r'''D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645
E:\je\rzuwnjvnuz 633
C:\km\tgjwpb\gy\atl 637
F:\weioj\hadd\connsh\rwyfvzsopsuiqjnr 647
E:\ns\mfwj\wqkoki\eez 648
D:\cfmwafhhgeyawnool 649
E:\czt\opwip\osnll\c 637
G:\nt\f 633
F:\fop\ywzqaop 631
F:\yay\jc\ywzqaop 631'''


# def lastWord(words):
#     return len(re.findall(r'[a-zA-Z]+',words)[-1])
#
# print(lastWord("hello nowcoder"))
#
#
# def reverseSentence(sentence):
#     print(" ".join(re.findall(r'[a-zA-Z]+', sentence)[::-1]))
#
#
# reverseSentence("I am a boy")


# def errorSummary(lines):

re.findall(r'\[a-zA-Z]+\s[0-9]+',LINES)