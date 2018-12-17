n, m = map(int, raw_input().split())
v = list(map(int, raw_input().split()))

en = []
en2 = []
i = 0
k = 0

while i < n-1:
    for j in range(m):
        en.append(v[i]+v[i+1])
        i += 2

while k < len(v)-1:
    for j in range(m):
        en2.append(v[k]+v[k+1])
        if en2[k] > v[k+1]+v[k+2]:
            en2.append(v[k+1]+v[k+2])



print en
print v
