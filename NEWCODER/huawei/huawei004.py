# meeting arrangement
import sys
'''
data=raw_input().split(',')
list1=[]
list2=[]
dict={}

if(int(data[1])>int(data[0])):
    dict[int(data[0])] = int(data[1])-int(data[0])
while(int(data[0])!=0 or int(data[1])!=0):
    data = raw_input().split(',')
    if(int(data[1])>int(data[0])):
        dict[int(data[0])] = int(data[1]) - int(data[0])

sorted(dict.keys())
out1=[]
out2=[]
#for key, value in dict.items():
k = dict.keys()[0]
res = str(int(k))+","+str(int(k)+int(dict[k]))
print res
'''

data=raw_input().split(',')
list1=[]
list2=[]
dict={}

if(int(data[1])>int(data[0])):
    dict[int(data[0])] = int(data[1])-int(data[0])
while(int(data[0])!=0 or int(data[1])!=0):
    data = raw_input().split(',')
    if(int(data[1])>int(data[0])):
        dict[int(data[0])] = int(data[1]) - int(data[0])

sorted(dict.keys())
out1=[]
out2=[]
for key,value in dict.items():
    out1.append(key)
    out2.append(value)
for i in range(0,len(out1)):
    if i+1<len(out1) and out1[i+1]>=out1[i] and out1[i+1]<(out1[i]+out2[i]):
        out1.pop(i+1)
        out2.pop(i+1)
j=0
tem1 = []
tem2 = []
while(j<len(out1)):
    k=0
    k=j+1
    tem1.append(out1[j])
    tem2.append(out2[j])
    while((k<len(out2) ) and (out2[j]==out2[k]) ):
        tem1.append(out1[k])
        tem2.append(out2[k])
        k=k+1
    sorted(tem1)
    for m in range(0, len(tem1)):
        print str(tem1[m])+','+str(tem1[m] + tem2[m])
    j=k
    tem1 = []
    tem2 = []