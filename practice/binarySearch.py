__author__ = 'Administrator'
# -*- coding: utf-8 -*-
def binarySearch(array, key):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low+high)/2
        if array[mid] < key:
            low = mid+1
        elif array[mid] > key:
            high = mid-1
        else:
            return array[mid]
    return -1

def binary_search_2(alist, item):
    n = len(alist)
    if 0 == n:
        return -1
    mid = n // 2
    if alist[mid] == item:
        return alist[mid]
    elif item < alist[mid]:
        return binary_search_2(alist[:mid], item)
    else:
        return binary_search_2(alist[mid + 1:], item)

if __name__ == "__main__":
    print binarySearch([1, 2, 3, 4, 5, 6, 7], 2)
    print binary_search_2([1, 2, 3, 4, 5, 6, 7], 3)

