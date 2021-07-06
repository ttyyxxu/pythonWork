import statistics
def activityNotifications(expenditure, d):
    notice = 0
    ll = len(expenditure)
    for i in range(d,ll):
        if expenditure[i] >= 2 * statistics.median(expenditure[i-d:i]):
            print(expenditure[i], expenditure[i-d:i], statistics.median(expenditure[i-d:i]))
            notice+=1
    return notice

activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5],5)
activityNotifications([1,2,3,4,4],4)
'''
STDIN               Function
-----               --------
9 5                 expenditure[] size n =9, d = 5
2 3 4 2 3 6 8 4 5   expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
'''