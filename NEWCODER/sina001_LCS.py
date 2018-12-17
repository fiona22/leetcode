# coding=utf-8
# 最长公共字串，要求是连续的
# 解法就是用一个矩阵来记录两个字符串中所有位置的两个字符之间的匹配情况，若是匹配则为1,否则为0。
# 然后求出对角线最长的1的序列，其对应的位置就是最长匹配子串的位置。
'''
def find_lcs(str1,str2):
    m = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    mmax = 0  # 记录长度
    p = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i]==str2[j]:
                m[i+1][j+1]=m[i][j]+1
                if m[i+1][j+1]>mmax:
                    mmax = m[i+1][j+1]
                    p = i+1
    return str1[p - mmax:p], mmax

print find_lcs("ABCDE","ABC")
'''

# 最长公共子序列
def find_lcseque(x, y):
    m = [[0 for i in range(len(y) + 1)] for j in range(len(x) + 1)]
    d = [[None for i in range(len(y) + 1)] for j in range(len(x) + 1)]

    for p1 in range(len(x)):
        for p2 in range(len(y)):
            if x[p1] == y[p2]:
                m[p1 + 1][p2 + 1] = m[p1][p2] + 1
                d[p1 + 1][p2 + 1] = 'ok'
            elif m[p1 + 1][p2] > m[p1][p2 + 1]:
                m[p1 + 1][p2 + 1] = m[p1 + 1][p2]
                d[p1 + 1][p2 + 1] = 'left'
            else:
                m[p1 + 1][p2 + 1] = m[p1][p2 + 1]
                d[p1 + 1][p2 + 1] = 'up'
    (p1, p2) = (len(x), len(y))

    s = []
    while m[p1][p2]:
        c = d[p1][p2]
        if c == 'ok':
            s.append(x[p1 - 1])
            p1 -= 1
            p2 -= 1
        if c == 'left':
            p2 -= 1
        if c == 'up':
            p1 -= 1
    s.reverse()
    return len(s)

x=raw_input()
y=raw_input()
print find_lcseque(x, y)
