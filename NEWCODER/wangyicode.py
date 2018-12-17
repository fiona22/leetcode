# coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line1 = sys.stdin.readline().strip()
    # 把这一行的数字分隔后转化成int列表
    values = map(int, line1.split())

    m = int(sys.stdin.readline().strip())
    line2 = sys.stdin.readline().strip()
    nums = map(int, line2.split())

    for num in nums:
        for i in range(n):
            if num > values[i]:
                num = num - values[i]
            else:
                print i + 1
                break








