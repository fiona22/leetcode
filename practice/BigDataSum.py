# coding=utf-8
# 大数相加减

S = raw_input()

L1 = S.strip().split(" ")[0]
L2 = S.strip().split(" ")[1]

max_len = len(L1) if len(L1) > len(L2) else len(L2)
if max_len<1 or max_len>100:
    print "error"

l1 = L1.zfill(max_len)
l2 = L2.zfill(max_len)  # 返回指定长度的字符串，原字符串右对齐，前面填充0

if l1.isdigit()==True and l2.isdigit()==True:
    a1 = list(l1)
    a2 = list(l2)
    a1.reverse()
    a2.reverse()

    a3 = [0]*(max_len+1)
    flag = [0]*(max_len+1)  # 进位

    for i in range(0, max_len):
        i_sum = flag[i] +int(a1[i])+int(a2[i])
        if i_sum > 10:
            flag[i+1] = 1
        else:
            flag[i+1] = 0
        a3[i] = i_sum % 10
    if flag[max_len-1] == 1:
        a3[max_len] = 1
    else:
        a3[max_len] = 0

    a3 = list(reversed(a3))
    if a3[0] == 0:
        a3.pop(0)
    res = [str(i) for i in a3]
    print ''.join(res)
else:
    print "error"



# 大数相乘
'''
def mul(n1,n2):
    n1.reverse()
    n2.reverse()
    n3 = []
    print n1, n2
    for i0 in xrange(len(n1)+len(n2)):
        n3.append(0)
    for i1 in xrange(len(n1)):
        for i2 in xrange(len(n2)):
            n3[i1+i2] += n1[i1]*n2[i2]
    for i3 in xrange(len(n3)):
        if(n3[i3]>9):
            n3[i3+1] += n3[i3]/10
            n3[i3] = n3[i3]%10
    n3.reverse()
    return n3
print mul([2,4,5,6,6],[4,5,2,0,5,3])

'''

