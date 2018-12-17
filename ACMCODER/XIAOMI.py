# coding=utf-8
# 找出旋转数组中最小的值
'''
def find_min(arr):
    low = 0
    high = len(arr)-1

    while(low<high):
        if high - low == 1:
            return arr[high]

        mid = int(low+high)/2
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low = mid+1
        else:
            high = mid
    return arr[low]

str = map(int, raw_input().split(" "))

print find_min(str)
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        target = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < target:
                return nums[i]
sol = Solution()
print sol.findMin([3, 4, 5, 1, 2])

