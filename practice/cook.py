# coding=utf-8

import sys
a=[]
for line in sys.stdin:
    if line.strip() == '':
        break
    a.extend(line.split())
print len(set(a))



