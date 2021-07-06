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
    median = 0
    window = deque(sorted(expenditure[0:d]),maxlen=d)

    for i in range(d, ll):

        ll_win = len(window)
        if ll_win % 2 == 0:
            median = (window[int(ll_win/2)-1] +  window[int(ll_win/2)+1]) / 2
        else:
            median = window[int((ll_win-1)/2)]

        if expenditure[i] >= 2 * median:
            notice += 1

        window.remove(expenditure[i-d])
        bisect.insort_left(window, expenditure[i])
    print(notice)



activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5],5)
activityNotifications([1,2,3,4,4],4)
'''
STDIN               Function
-----               --------
9 5                 expenditure[] size n =9, d = 5
2 3 4 2 3 6 8 4 5   expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
'''