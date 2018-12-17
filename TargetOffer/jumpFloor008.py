# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        a=1
        b=2
        if number<=0:
            return 0
        if number<2:
            return 1
        for i in range(2, number+1):
            a, b = b, a+b
        return a

class Solution:
    def jumpFloorII(self, number):
        a = 1
        b = 2
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        else:
            for i in range(2,number+1):
                b = 2*a
                a = b
            return b

