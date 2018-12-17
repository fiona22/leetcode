# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表

    def Find(self, target, array):
        row = len(array)
        col = len(array[0])

        i = col-1  # 从左下角开始查找
        j = 0

        while i >= 0 and j < row:
            if array[j][i] < target:
                j += 1
            elif array[j][i] > target:
                i -= 1
            else:
                return True
        return False



sol = Solution()
print sol.Find(15,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])



