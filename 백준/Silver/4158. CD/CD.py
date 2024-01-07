import sys

while True:
    a, b = map(int,input().split())
    if a==0 and b ==0:
        break
    dic = {}
    CD_count = 0
    for _ in range(a):
        cd = int(sys.stdin.readline())
        dic[cd] = 1

    for i_ in range(b):
        cd = int(sys.stdin.readline())
        if cd in dic:
            CD_count += 1

    print(CD_count)