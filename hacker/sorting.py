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

def countInversions_wrong(arr):

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


def countInversions(myList):
    swaps = 0
    if len(myList) == 1:
        return 0
    elif len(myList) == 2:
        if myList[0] > myList[1]:
            myList[0], myList[1] = myList[1], myList[0]
            return 1
        else:
            return 0
    mid = len(myList) // 2
    left = myList[:mid]
    right = myList[mid:]

    # Recursive call on each half
    swaps += countInversions(left)
    swaps += countInversions(right)

    # Two iterators for traversing the two halves
    i = 0
    j = 0

    # Iterator for the main list
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # The value from the left half has been used
            myList[k] = left[i]
            # Move the iterator forward
            i += 1
        else:
            myList[k] = right[j]
            swaps += (len(left) - i)
            j += 1
        # Move to the next slot
        k += 1

    # For all the remaining values
    while i < len(left):
        myList[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        myList[k] = right[j]
        j += 1
        k += 1
    # print(swaps,myList,left,right)
    return swaps

print(countInversions([7,5,3,1]))

print(countInversions([2,1,3,1,2]))