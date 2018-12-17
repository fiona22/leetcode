# coding=utf-8
# 比较字符串长短
line = raw_input()
str=line.split(" ")
print str
length = []


dict = {}

for i in str:
    dict.update({i: len(i)})

items = dict.items()
items.sort()
items.reverse()
print dict
