
n = input()
n = n+1
a = list(range(1, n))

global m;
m = 7;

A = list(range(n+1, m))
C = list(range(1, m))

b = [i for i in A]
def LCM(B):
    start = B[0]
    for key in B[1:]:
        if start != key:
            return False
    return True

while not LCM(A):
    min_num = min(A)
    for index, item in enumerate(A):
        if item == min_num:
            A[index]+=b[index]

print A[0]/5
