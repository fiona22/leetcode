def insertSort(arr):
    length = len(arr)
    for i in range(1, length):
        x = arr[i]
        j = i-1
        while(j>=0 and x<arr[j]):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = x


def printArr(arr):
    for item in arr:
        print(item)

arr = [4,7,8,9,0,1]
insertSort(arr)
printArr(arr)

