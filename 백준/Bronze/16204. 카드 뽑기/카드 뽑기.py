n, m, k = map(int, input().split())
ans = min(m, k) + min(n-m, n-k)
print(ans)