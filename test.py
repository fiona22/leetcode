# coding=utf-8
b = [0]*4
a = []
for i in range(3):
    a.append(b)
print a

# 列表生成法
test = [[0 for i in range(4)] for j in range(3)]
print test