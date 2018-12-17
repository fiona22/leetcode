#!/usr/bin/python
import sys,time

'''
string = input()
n = len(string)
ans=""

if pro == "C":
    i = 0
    while i < n:
        j = i+1
        con = 1
        while j < n and string[j]== string[i]:
            con += 1
            j += 1
        if con == 1:
            ans = ans + string[i]
        else:
            new = "%d%s" % (con, string[i])
            ans = ans + new
        i = j
'''
string = str(raw_input())
n = len(string)
ans = ""

i=0
while i < n-1:
    j = i + 1
    if string[i].isdigit():
        while string[j].isdigit():
            j+=1
        num = int(string[i:j])
        new = string[j] * num
        ans = ans + new
        i = j + 1
    else:
        ans = ans + string[i]
        i = j
print ans
