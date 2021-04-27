def miniswap(arr):
    steps = 0
    for i,num in enumerate(arr):
        if num != i+1:
            arr[arr.index(i+1)], arr[i] = arr[i], arr[arr.index(i+1)]
            steps += 1
            print(steps,arr)

miniswap([7,1,3,2,4,5,6])

miniswap([2,3,4,1,5])