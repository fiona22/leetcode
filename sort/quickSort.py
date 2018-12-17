__author__ = 'Administrator'
def quickSort(array, left, right):
    if left >= right:
        return
    key = array[left]
    low = left
    high = right

    while(left<right):
        while(left<right and array[right]>=key):
            right -= 1
        array[left] = array[right]
        while(left<right and array[left]<=key):
            left += 1
        array[right] = array[left]
    array[left] = key

    quickSort(array, low, left-1)
    quickSort(array, left+1, high)
    return array

array=[4,2,5,1,3,7,6]
low = 0
high = len(array)-1
print quickSort(array, low, high)



