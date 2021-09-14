from statistics import median
# Mean, Median, and Mode
'''
N = int(input())
X_str = input().split(" ")

# N = 3
# X_str = ["12","22","6"]
X = [int(x) for x in X_str]

mean = round(sum(X)/N, 1)
print(mean)

X.sort()
print(X)
if N % 2 == 0:
    median = (X[int(N/2)] + X[int(N/2)-1])/2
else:
    median = X[int((N-1)/2)]
print(median)
freq = 0
Uniq_X = sorted(set(X))
for x in Uniq_X:
    if X.count(x) > freq:
        freq = X.count(x)
        mode = x
print(mode)
'''

# Weighted X
'''
N = int(input())
X_str = input().split(" ")
W_str = input().split(" ")
X = [int(x) for x in X_str]
W = [int(w) for w in W_str]

Total = 0
for i in range(0,N):
    Total += X[i] * W[i]

print(round(Total/sum(W),1))
'''

def Median():
    N = int(input())
    X = list(map(int, input().strip().split()))
    X.sort()
    if N%2 == 0:
        L = X[:int(N/2)]
        R = X[int(N/2):]
    else:
        L = X[:int((N-1)/2)]
        R = X[int((N+1)/2):]
    print(X,L,R)
    print(median(L))
    print(median(X))
    print(median(R))

def substring(str,l):
    assert l <= len(str)
    for i in range(0, len(str)-l+1):
        yield str[i:i+l]


def FindmissingWord(s,t):
    '''
    :param s: longer string to examine
    :param t: subsequence of s
    :return:  list of missing words

    '''
    s_list = s.strip().split()
    t_list = t.strip().split()
    start = 0
    indicies = set(range(len(s_list)))
    word_in_t_list = []
    for word in t_list:
        idx = s_list[start::].index(word) + start
        word_in_t_list.append(idx)
        start = idx+1
    print(indicies, word_in_t_list, sep='\n')
    missing_words = indicies - set(word_in_t_list)
    return [s_list[x] for x in missing_words]

def Interquartile_Range(N,X,F):
    # N = int(input())
    # X = list(map(int, input().strip().split()))
    # F = list(map(int, input().strip().split()))
    S = []
    for i in range(N):
        S.extend([X[i]] * F[i])
    S.sort()

    N = len(S)
    if N%2 == 0:
        Q1 = S[:int(N/2)]
        Q3 = S[int(N/2):]
    else:
        Q1 = S[:int((N-1)/2)]
        Q3 = S[int((N+1)/2):]
    return round(median(Q3) - median(Q1) + 0.0,1)

#print(list(substring("sbdnfmmass",4)))

s="Prior to saving data, consider planning the directory structure for your Isilon IQ cluster. A well designed directory structure can ease administration"
t="to saving data, consider planning the structure for your Isilon IQ cluster. directory structure administration"
# print(FindmissingWord(s,t))

print(Interquartile_Range(5,[10,40,30,50,20],[1,2,3,4,5]))