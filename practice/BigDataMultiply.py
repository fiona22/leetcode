# coding=utf-8
# 大数相乘
import sys



def mul(n1, n2):
    n1.reverse()
    n2.reverse()
    n3 = []
    print n1, n2
    for i0 in xrange(len(n1)+len(n2)):
        n3.append(0)
    for i1 in xrange(len(n1)):
        for i2 in xrange(len(n2)):
            n3[i1+i2] += n1[i1]*n2[i2]
    for i3 in xrange(len(n3)):
        if(n3[i3]>9):
            n3[i3+1] += n3[i3]/10
            n3[i3] = n3[i3]%10
    n3.reverse()
    return n3

line = sys.stdin.readline().strip().split()
m = line[0]
n = line[1]
print mul(m, n)

