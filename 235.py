list = []
for i in range(1, 2042):
    if i%2==0 or i%3==0 or i%5==0:
        list.append(i)
print len(list)