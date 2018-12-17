
import sys

def compare(a, b):
    la = a.split('.')
    lb = b.split('.')
    f = 0
    if len(a)>len(b):
        f = len(la)
    else:
        f = len(lb)
    for i in range(f):
        try:
            if int(la[i])>int(lb[i]):
                print 1
                return
            elif int(la[i])==int(lb[i]):
                continue
            else:
                print -1
                return
        except IndexError as e:
            if len(la)>len(lb):
                print 1
                return
            else:
                print -1
                return
m, n = map(str, sys.stdin.readline().strip('\n').split())
compare(m,n)



