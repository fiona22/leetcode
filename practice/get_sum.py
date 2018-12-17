#encoding=utf-8
import sys
import math

if __name__=="__main__":
    n, m = map(int, raw_input().split())
    temp = []
    temp.append(n)
    for i in range(1, m):
        temp.append(math.sqrt(temp[i-1]))
    s = sum(temp)

    print "%0.2f" % s








