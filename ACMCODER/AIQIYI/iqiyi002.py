# coding=utf-8
# 面条放在数轴上，每根面条对应数轴上的两个点，他想知道在任意两根面条不重叠（端点可以重叠）的情况下，最多能选出多少根面条来
# 1<=n<=100
# -999<a<b<=999
'''
N = int(raw_input())
a = []
b = []
for i in range(N):
    str = raw_input().split(" ")
    a.append(str[0])
    b.append(str[1])


for i in range(N):
    if a[i] > b[i]:
        a[i], b[i] = b[i], a[i]
count = []
dict = {}

for i in range(N):
    key=a[i]
    value=b[i]
    dict[key]=value

new_a=[]
new_b=[]
for key,value in sorted(dict.items()):
    new_a.append(key)
    new_b.append(value)

for i in range(N-1):
    for j in range(i+1, N):
        if new_a[j] >= new_b[i]:
            count.append(1)
print len(count)+1
'''

n=input()
num = []
for i in range(n):
    str=raw_input().split(" ")
    a = str[0]
    b = str[1]
    if a>b:
        a,b = b,a
    num.append(a,b)
num = sorted(num, key = lambda x:x[1])

ans = 0

if n:
    ans=1
    t = num[0][1]
    for i in range(n):
        if num[i][0]>=t:
            t = num[i][1]
            ans+=1
print ans