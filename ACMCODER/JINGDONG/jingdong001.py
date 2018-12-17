#!/bin/python
# -*- coding: utf8 -*-
# coding=utf-8
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************

'''
def solve(a, b):
    c = [0]*len(a)
    d = [0]*len(b)
    for i in range(len(a)):
        c[i] = ord(a[i])-97
    for i in range(len(b)):
        d[i] = ord(b[i])-97

    num = 0
    for i in range(len(a)-len(b)+1):
        flag = -1
        for j in range(len(b)):
            now = c[i+j]
            for k in range(len(b)-j-1):
                if d[j]==d[j+k+1]:
                    if c[i+j+k+1]==c[i+j]:
                        break
                    else:
                        flag=1
                        break
        if flag==-1:
            num += 1
    return num

'''

vocabulary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def  solve(S, T):

    result = 0
    T_len = len(T)
    S_len = len(S)
    for i in range(S_len-T_len):
        str = S[i:i+T_len]
        for j in range(26):

            sign = 0

            for k in range(T_len):

                if vocabulary[(j+vocabulary.index(str[k]))%26] != str[k]:

                    break

                else:

                    sign =sign+1

            if sign == T_len:

                result += 1

                break

    return result





try:
    S = raw_input()
except:
    S = None

try:
    T = raw_input()
except:
    T = None
res = solve(S, T)

print str(res) + "\n"

'''
def solve(S, T):
    res = []
    A = list(S)
    B = list(T)
    if len(A) >= len(B):
        for i in range(len(B)):
            A[i] = B[i]
        for i in range(len(B)):
            if A[i]==B[i]:
                break
        res.append(1)
    return len(res)
'''