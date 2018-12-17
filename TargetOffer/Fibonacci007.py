# -*- coding:utf-8 -*-
'''
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n<=0:
            return 0
        elif n==1:
            return 1
        else:
            return Fibonacci(n-1)+Fibonacci(n-2)
'''
class Solution:
    def Fibonacci(self, n):
        a=1
        b=1
        if n<=0:
            return 0
        if n<2:
            return 1
        for i in range(2, n+1):
            a, b = b, a+b
        return a


sol = Solution()
print sol.Fibonacci(3)