n, r, c = map(int,input().split())

ans = 0

while n!= 0:
    n -= 1
    #第二
    if r < 2 ** n and c < 2 ** n:
        ans += (2**n) * (2**n) * 0
    #第一
    elif r < 2 ** n and c >= 2 ** n:
        ans += (2**n) * (2**n) * 1
        c -= (2**n)
    #第3
    elif r >= 2 ** n and c < 2 ** n:
        ans += (2**n) * (2**n) * 2
        r -= (2**n)
    #第4
    else:
        ans += (2**n) * (2**n)*3
        r -= (2**n)
        c -= (2**n)

print(ans)