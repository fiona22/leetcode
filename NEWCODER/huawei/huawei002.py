#encoding=utf-8
import sys
'''
def substring(input1,input2):
    str1 ="".join(input1)
    str2 = "".join(input2)
    tmp = []
    for i in str2:
        if str1.__contains__(i) == 0:
             tmp.append(0)
        else:
            tmp.append(1)
    if tmp.__contains__(0):
        return False
    else:
        return True


input1, input2 = map(str, raw_input().split(","))
if len(input1)<len(input2) and len(input1)<5 and len(input2)<5:
    print False
else:
    print substring(input1, input2)
'''

def isContain(A,B):
    a = list(A)
    b = list(B)
    if len(a)<5 and len(b)<5 and len(a)<len(b):
        return False
    else:
        fix = [0]*26
        for i in a:
            fix[ord(i)-ord('A')]=1
        for j in b:
            if (fix[ord(j)-ord('A')]==1):
                fix[ord(j)-ord('A')]=0

        for i in range(26):
            if fix[i]!=0:
                return False
            return True
A = raw_input()
B = raw_input()

print isContain(A, B)