# coding=utf-8
# 一个好数，旋转之后，也一个数字，如2，5，6，9，注意0，10不是
def good_num(N):
    res = 0
    str1 =''
    for i in range(1, N+1):
        str1 = str(i)
        if(str1.count('3')==0 and str1.count('4')==0 and str1.count('7')==0):
            if str1.count('1')+str1.count('8')+str1.count('0')!=len(str1):
                res += 1
    return res

N=input()
print good_num(N)

