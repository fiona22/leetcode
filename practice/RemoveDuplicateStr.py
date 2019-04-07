import sys
str = sys.stdin.readline().strip()
tmp = []
for i in str:
    tmp.append(i)

res = []
for j in tmp:
    if j not in res:
        res.append(j)
print "".join(res)

