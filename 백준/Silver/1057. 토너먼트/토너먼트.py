n, a, b = map(int,input().split())
r = 0
while a != b:
    a -= a // 2
    b -= b // 2
    r += 1
print(r)