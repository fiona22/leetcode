import sys

N = raw_input()

lines = map(int, sys.stdin.readline().strip().split())

sum1 = []
sum2 = []
i = 1
while (i<N):
    if lines[i]%2 == 1:
        sum1.append(lines[i])
        i += 1
        if i<N:
            sum1.append(i)
print sum(sum1)

