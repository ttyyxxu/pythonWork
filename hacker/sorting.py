import bisect
import statistics
from collections import deque
def activityNotifications_normal_yet_slow(expenditure, d):
    notice = 0
    ll = len(expenditure)
    for i in range(d,ll):
        if expenditure[i] >= 2 * statistics.median(expenditure[i-d:i]):
            print(expenditure[i], expenditure[i-d:i], statistics.median(expenditure[i-d:i]))
            notice+=1
    return notice

def activityNotifications(expenditure, d):
    notice = 0
    ll = len(expenditure)

    window = list(sorted(expenditure[0:d]))

    for i in range(d, ll):

        ll_win = len(window)
        if ll_win % 2 == 0:
            median = window[ll_win//2-1] + window[ll_win//2]
        else:
            median = window[ll_win//2] * 2

        if expenditure[i] >= median:
            notice += 1

# this is the magic part, bisect or insort are log(n).
        rem = bisect.bisect_left(window,expenditure[i-d])
        window.pop(rem)
        bisect.insort_left(window, expenditure[i])
    return notice



activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5],5)
activityNotifications([1,2,3,4,4],4)
'''
STDIN               Function
-----               --------
9 5                 expenditure[] size n =9, d = 5
2 3 4 2 3 6 8 4 5   expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
'''

'''
O(n^2)
'''
def countInversions_n_n_slow(arr):
    swaps = 0
    for i in range(len(arr)):
        for j in range(1,len(arr)-i):
            if arr[j-1] > arr[j]:
                swaps += 1
                arr[j-1], arr[j] = arr[j], arr[j-1]
                print(arr)
    print(swaps)
def countInversions(arr):

    if len(arr) == 1:
        return 0
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return 1
        else:
            return 0
    swaps = 0
    bigger = []
    smaller = []
    for i in range(len(arr) // 2):
        if arr[2*i] > arr[2*i+1]:
            swaps += 1
            bigger.append(arr[2*i])
            smaller.append(arr[2*i+1])
        else:
            bigger.append(arr[2*i+1])
            smaller.append(arr[2*i])
        print(i,bigger,smaller)

    if len(arr) % 2 ==1:
        bigger.append(arr[-1])
    # print(swaps,bigger,smaller)

    return swaps + countInversions(bigger) + countInversions(smaller)

print(countInversions([7,5,3,1]))
