import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    ans = []
    for i in range(N):
        line = list(sys.stdin.readline().strip())
        for j in range(len(line)):
            if len(line) >= 3 and j+2 < len(line) and line[j]==line[j+1]==line[j+2]:
                del line[j+2]
            if len(line) >= 4 and j+3 < len(line) and line[j] == line[j+1] and line[j+2] == line[j+3]:
                del line[j+3]
        print "".join(line)










