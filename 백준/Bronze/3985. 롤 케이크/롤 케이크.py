L = int(input())
N = int(input())

rollCake = [0] * (L + 1)
received = [0] * (N + 1)
maxPieces, wantMaxNum = 0, 0

for i in range(1, N + 1):
    cnt = 0
    P, K = map(int, input().split())

    # 가장 많은 조각을 받을 것으로 기대한 방청객 번호
    wantPieces = K - P
    if maxPieces < wantPieces:
        maxPieces = wantPieces
        wantMaxNum = i

    # 해당 번호의 롤케이크 있으면 제공
    for j in range(P, K + 1):
        if rollCake[j] == 0:
            rollCake[j] = i
            cnt += 1
    received[i] = cnt

print(wantMaxNum)
print(received.index(max(received)))