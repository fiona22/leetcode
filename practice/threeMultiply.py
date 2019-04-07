import sys
n = int(sys.stdin.readline())
A = map(int, sys.stdin.readline().strip().split())

if n < 3:
    print 0
arr = sorted(A)
res1 = arr[n-1]*arr[n-2]*arr[n-3]
res2 = arr[0]*arr[1]*arr[n-1]
print max(res1, res2)



