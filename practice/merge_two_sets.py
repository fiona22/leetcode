import sys


n, m = map(int, raw_input().split())
A = sys.stdin.readline().strip().split(" ")
B = sys.stdin.readline().strip().split(" ")
print " ".join(sorted(set(A+B), key=int))

