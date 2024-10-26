import sys
input = sys.stdin.readline
N = int(input())
data = list(map(int, input().split()))
dp = [1]*N
dp2 = [1]*N
for i in range(N-1):
    if data[i+1] >= data[i]:
        dp[i+1] += dp[i]
for i in range(N-1):
    if data[i+1] <= data[i]:
        dp2[i+1] += dp2[i]
max1 = max(dp)
max2 = max(dp2)
print(max(max1, max2))