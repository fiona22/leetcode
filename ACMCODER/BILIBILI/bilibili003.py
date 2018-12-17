__author__ = 'Fiona'
x = raw_input()
list2 = []
for i in range(int(x)):
    m = raw_input()
    mlist = m.split(',')
    list1 = []
    for j in range(int(x)):
        list1.append(int(mlist[j]))
    list2.append(list1)

for i in range(1, int(x)):
    list2[0][i] = list2[0][i-1]+list2[0][i]

for i in range(1, int(x)):
    list2[i][0] = list2[i][0] + list2[i-1][0]

for i in range(1,int(x)):
    for j in range(1, int(x)):
        list2[i][j] = list2[i][j]+min(list2[i-1][j], list2[i][j-1])
print list2[int(x)-1][int(x)-1]
