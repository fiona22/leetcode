#
str = raw_input()
a = list(str.split(","))
b = map(int, a)
res = []
for i in range(len(b)-1):
    if sum(b[0:i]) == sum(b[i+1:len(b)]):
        res.append(b[i])
if len(res)==0:
    print "False"
else:
    print res[0]


'''
str = raw_input()
a = list(str.split(","))
b = map(int, a)


for i in range(len(b)-1):
    if sum(b[0:i]) == sum(b[i+1:len(b)]):
        print b[i]
'''