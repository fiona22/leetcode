__author__ = 'Administrator'
def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array

array = [9,3,1,4,2,7,8,6,5]
print bubbleSort(array)



