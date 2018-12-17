# coding=utf-8
# 分发糖果的问题，使用贪心算法，首先将小盆友的胃口gi和糖果的尺寸si排序
# 然后循环比较，如果第一块糖满足不了第一个小盆友就往后+1，如果能满足，就小盆友和糖位置都加1，另外记录count+1
# 用到的是贪心算法。

gi = list(map(int, raw_input().split(" ")))
si = list(map(int, raw_input().split(" ")))
gi.sort()
si.sort()

count = 0
countChild = 0
countSuagr = 0
while(countChild<len(gi) and countSuagr<len(si)):
    if si[countSuagr] >= gi[countChild]:
        count += 1
        countChild += 1
        countSuagr += 1
    else:
        countSuagr+=1

print count