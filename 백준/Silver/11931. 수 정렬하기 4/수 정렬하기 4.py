import sys

n = int(sys.stdin.readline())

num = []
for _ in range(0, n):
    num.append(int(sys.stdin.readline()))

num.sort()
num.reverse()
for i in range(0, n):
    print(num[i])