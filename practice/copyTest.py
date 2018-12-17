import copy

kvps = { '1' : 1, '2' : 2 }
theCopy = kvps.copy()
kvps['1'] = 5
sum = kvps['1'] + theCopy['1']
print sum

x = [1, 2, 3, [4, 5]]

c = copy.copy(x)
d = copy.deepcopy(x)
x.append(7)
x[3].append(6)

print x
print c
print d

