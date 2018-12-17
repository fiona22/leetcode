#!/usr/bin/python
#encoding=utf-8
import sys
import numpy as np
# 使用sys.stdin.readline()方法读入用户输入的一行
line = sys.stdin.readline()
# 使用while循环读入用户的输入，直到用什么都不输入时跳出while
# 这里line如果是空字符串，则表示逻辑False了

'''
while line:
    # 打印用户的输入，注意这里读入的文本最后一个字符是换行符，所以在print的时候舍弃了最后一个字符
    print line[:-1]
    # 读取下一行
    line = sys.stdin.readline()
'''
n = input()
x = []
y = []
for i in range(n):
    lines = sys.stdin.readline().strip() #readline, 一行一行读
    values = map(int, lines.split(","))
    x.append(values[0])
    y.append(values[1])
x = np.array(x)
y = np.array(y)