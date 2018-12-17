__author__ = 'Fiona'
import sys
n = input()
X = []
Y = []
for i in range(n-1):
    lines = sys.stdin.readline().strip('\n')
    values = map(int, lines.split())
    X.append(values[0])
    Y.append(values[1])
len = len(X)

if X==[1]*(len):
    print 2*(n-1)-1
else:
    for i in range(n):
        if Y[0] == X[1]:
            continue
        else:
            break
    print n-1
