n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()
temp = 1

while temp <= n and a[temp - 1] + 1 > temp:
    temp = a[temp - 1] + 1
print(temp)