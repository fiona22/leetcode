# coding=utf-8
# 跳台阶问题，一次可以一步或者两步，不用递归，否则超时
def get_step(n):
    if n<0:
        return -1
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        n1, n2 = 1, 2
        step = 0
        for i in range(3, n+1):
            step = n1+n2
            n1 = n2
            n2 = step
        return step

n=input()

print get_step(n)