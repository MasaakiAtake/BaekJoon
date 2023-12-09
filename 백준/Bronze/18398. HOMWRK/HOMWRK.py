T = int(input())
for i in range(T):
    N = int(input())
    for j in range(N):
        a, b = map(int, input().split())
        print(a+b, a*b)