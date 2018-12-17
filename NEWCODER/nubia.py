import numpy as np

n, m = map(int, raw_input().split(","))

if m==0:
    path = 0
if m==1:
    path = n
if m==2:
    path = 2*n

if m>2:
    path = n+2*n-n/(np.power(2, m-2))
print '%.1f' %path
