__author__ = 'Administrator'
import sys
def sumAB(X,Y):
    A = list(X)
    B = list(Y)
    A.reverse()
    B.reverse()
    print A
    print B

    sum = []
    num = abs(len(A)-len(B))
    print num
    if len(A)<len(B):
        A.extend([0]*num)
        print A
    else:
        B.extend([0]*num)
    for i in range(len(A)):
        c = ord(A[i])+ord(B[i])
        carry = c/26
        res=(ord(A[i])+ord(B[i]))%26
        sum.append(res+'a')
        if carry == 1 :
            sum.append(B)
    return str(sum.reverse())

A = raw_input()
B = raw_input()
sumAB(A, B)




