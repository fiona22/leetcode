# -*- coding:utf-8 -*-
from operator import *
class Solution:
    def NumberOf1(self, n):
        if n >= 0:
            n = str(bin(n))
            res = n.count("1")
        num = 0
        if n < 0:
            n = str(bin(2**32+n))
            res = n.count("1")
        return res


sol = Solution()

print sol.NumberOf1(-2)

