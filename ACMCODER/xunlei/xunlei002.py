# coding=utf-8
# 和最大的K个数
import numpy as np
str = raw_input()

array1 = list(str.split("-")[0])
for i in array1:
    if i == ",":
        array1.remove(i)
array1 = map(int, array1)


str2 = str.split("-")[1]
array2 = list(str2.split(":")[0])
for i in array2:
    if i == ",":
        array2.remove(i)
array2 = map(int, array2)


k = int(str2.split(":")[1])

res = []
for i in array1:
    for j in array2:
        res.append(i+j)

res.sort(reverse=True)

print res[0:k]



