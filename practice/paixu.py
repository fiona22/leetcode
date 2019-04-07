# coding=utf-8
'''
牛牛有一个长度为n的整数序列,牛牛想对这个序列进行重排为一个非严格升序序列。
牛牛比较懒惰,他想移动尽量少的数就完成重排,请你帮他计算一下他最少需要移动多少个序列中的元素。
(当一个元素不在它原来所在的位置,这个元素就是被移动了的)
输入
3
3 2 1
输出2
'''
import sys
n = int(sys.stdin.readline().strip())
x = map(int, sys.stdin.readline().strip().split())
y = sorted(x)

res = 0
for i in range(len(x)):
    if x[i] == y[i]:
        res += 1

print len(x)-res



