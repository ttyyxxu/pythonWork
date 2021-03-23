def findMedianSortedArrays(nums1, nums2):
    list_merge = []
    list_merge.extend(nums1)
    list_merge.extend(nums2)
    list_merge.sort()
    print(list_merge)
    if list_merge == []:
        return None
    if len(list_merge) % 2 == 1:
        return list_merge[int((len(list_merge)-1)/2)]
    else:
        return (list_merge[int(len(list_merge)/2)] + list_merge[int(len(list_merge)/2 - 1)]) / 2


print(findMedianSortedArrays([1,2,3,4,7,8,100],[0,2,3,4,22,33,467]))