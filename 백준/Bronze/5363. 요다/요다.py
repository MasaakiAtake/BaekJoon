import sys
for _ in range(int(sys.stdin.readline())):
    tmp = list(sys.stdin.readline().split())
    for i in range(2, len(tmp)):
        print(tmp[i], end=' ')
    print(tmp[0], end=' ')
    print(tmp[1],end='')
    print()