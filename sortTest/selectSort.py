__author__ = 'Administrator'
def selectSort(array):
    n= len(array)
    for i in range(0, n-1):
        min = i
        for j in range(i+1,n):
            if array[j] < array[min]:
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp
         #exchange array[min] and array[i]
    return array

array = [9,3,4,5,1,5,7,3]
print selectSort(array)