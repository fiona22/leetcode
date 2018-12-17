while 1:
    arr = []
    s = raw_input()
    if s != " ":
        for x in s.split(' '):
            arr.append(int(x))

temp = 0
for i in arr:
    temp ^= i
a1, a2 = 0, 0
tag = 1
while temp & tag == 0:
    tag <<= 1
for i in arr:
    if i & tag == 0:
        a1 ^= i
    else:
        a2 ^= i
print a1, a2






