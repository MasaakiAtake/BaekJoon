n, m = map(int,input().split())
ans = 0
priceli = []

for _ in range(m):
    price = tuple(map(int,input().split()))
    priceli.append(price)

sixli = sorted(priceli, key=lambda x : x[0])
oneli = sorted(priceli, key=lambda x : x[1])

if sixli[0][0] <= oneli[0][1]* 6:
    ans = sixli[0][0] * (n//6)+oneli[0][1]*(n%6)
    if sixli[0][0] < oneli[0][1] * (n%6):
        ans = sixli[0][0] * (n//6+1)

else:
    ans = oneli[0][1] * n

print(ans)