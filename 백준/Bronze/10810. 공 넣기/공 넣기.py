N, M = map(int, input().split())

baskets = [0] * N  # 초기 바구니 상태

for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):
        baskets[idx] = k

print(*baskets)