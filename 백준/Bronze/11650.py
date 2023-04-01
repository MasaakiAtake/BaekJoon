N = int(input())
xlis = []
ylis = []

for i in range(N):
    x, y = list(map(int,input().split()))
    xlis.append(x)
    ylis.append(y)
lx = sorted(xlis)
ly = sorted(ylis)

for i in range(N):
    print(lx[i], ly[i])

import sys
input=sys.stdin.readline
N = int(input())
li = []
for _ in range(N):
    x, y = map(int, input().split())
    li.append([x,y])
li.sort(key = lambda x : (x[0], x[1]))

for i in range(N):
    print(li[i][0], li[i][1])