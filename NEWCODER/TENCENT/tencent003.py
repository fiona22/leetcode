# coding=utf-8
'''
input:
3
91 16 5
58 16 0
96 12 4

要求：ABC可以选择若干个数字，但这些数字必须为　A的倍数，并且至少选择一个数字
问是否存在一种选择方案使得这些数字的和对B取余结果为C，如果存在输出YES,否则输出NO

output:
YES
YES
NO
'''

n = input()
A = []
B = []
C = []
for i in range(n):
    num = raw_input()
    a = num.split(" ")[0]
    b = num.split(" ")[1]
    c = num.split(" ")[2]
    A.append(int(a))
    B.append(int(b))
    C.append(int(c))



for i in range(n):
    mod = A[i] % B[i]
    for j in range(B[i]):
        if mod*j%B[i]==C[i]:
            pass
    print "YES"



