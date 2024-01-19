n = int(input())
obN = list(bin(n)[2:])[::-1]
t, ans = 1, 0
for a in obN:
    ans += int(a)*t
    t *= 3
print(ans)