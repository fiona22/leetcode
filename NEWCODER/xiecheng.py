#!/usr/bin/env python
# coding=utf-8
# 计算单变量的信息增益
import sys
import numpy as np
def cal_ent(x):
    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        p = float(x[x==x_value].shape[0])/x.shape[0]
        logp = np.log2(p)
        ent -= p*logp
    return ent
def cal_condition_ent(x,y):
    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        sub_y = y[x==x_value]
        tmp_ent = cal_ent(sub_y)
        ent += (float(sub_y.shape[0])/y.shape[0])*tmp_ent
    return ent

def cal_ent_gain(x, y):
    base_ent = cal_ent(y)
    condition_ent = cal_condition_ent(x,y)
    ent_gain = base_ent - condition_ent
    return ent_gain

#x=np.array([1,1,2,0,3])
#y=np.array([1,1,0,0,0])
n = input()
x = []
y = []
for i in range(n):
    lines = sys.stdin.readline().strip()
    values = map(int, lines.split(","))
    x.append(values[0])
    y.append(values[1])
x = np.array(x)
y = np.array(y)

print "%.2f" %(cal_ent_gain(x, y))