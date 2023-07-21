t = int(input())
for i in range(t):
    t = list(int(x) for x in input().split())
    t.sort()
    print(t[-3])