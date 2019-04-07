# coding=utf-8
'''
牛牛有羊羊有了属于他们自己的飞机。于是他们进行几次连续的飞行。
f[i]表示第i次飞行所需的燃油的升数。飞行只能按照f数组所描述的顺序进行。
起初飞机里有s升燃油,为了正常飞行,每次飞行前飞机内燃油量应大于等于此处飞行所需要的燃油量。
请帮助他们计算在不进行加油的情况下他们能进行的飞行次数。

输入
7 10
1 2 3 4 5 6 7

输出
4
'''
import sys

n, s = map(int, sys.stdin.readline().split())
f = list(map(int, sys.stdin.readline().split()))
res = 0
for i in range(n):
    if s >= f[i]:
        res += 1
        s -= f[i]
    else:
        break
print res