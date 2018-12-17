# coding=utf-8
# 给定一个数字矩阵，请设计一个算法从左上角开始顺时针打印矩阵元素
import sys
import numpy as np

def MatrixOrder(matrix):
    res = []
    if len(matrix) == 0:
        return res
    rowStart = 0
    rowEnd = len(matrix)-1

    colStart = 0
    colEnd = len(matrix[0])-1

    while rowStart <= rowEnd and colStart <= colEnd:
        for i in range(colStart, colEnd+1):
            res.append(matrix[rowStart][i])
        rowStart += 1
        for i in range(rowStart, rowEnd+1):
            res.append(matrix[i][colEnd])
        colEnd -= 1

        if rowStart <= rowEnd:
            for i in range(colEnd, colStart-1, -1):
                res.append(matrix[rowEnd][i])
        rowEnd -= 1
        if colStart <= colEnd:
            for i in range(rowEnd, rowStart-1, -1):
                res.append(matrix[i][colStart])
        colStart += 1
    return res

X = []
M, N = map(int, sys.stdin.readline().strip('\n').split())
for i in range(M+1):
    line = map(int, sys.stdin.readline().strip('\n').split())
    if map(int, line)[0]!=-1 and map(int, line)[1]!=-1:
        X.append(line)
    else:
        break

#Y = np.array(X)
#print X
Z = MatrixOrder(X)

for i in range(len(Z)-1):
    print str(Z[i])+",",
print str(Z[-1])
