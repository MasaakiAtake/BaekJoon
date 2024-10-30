import sys
input = sys.stdin.readline
N = int(input())
# i을 마지막으로 하는 수들의 곱에서 최대값
dp = [float(input()) for _ in range(N)]

# 1부터 시작해야 dp[i-1]에서 dp[-1]으로 잘못 곱해지지 않음
for i in range(1, N):
    dp[i] = max(dp[i], dp[i]*dp[i-1])
print('%0.3f' % max(dp))