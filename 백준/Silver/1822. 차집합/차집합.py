a, b = map(int, input().split())
A, B = {}, {}
for n in map(int, input().split()):
    A[n] = 1
for n in map(int, input().split()):
    B[n] = 1

# 리스트로 풀면 시간초과가 나지만 해쉬로 풀면 문제를 해결할 수 있다.
C = []
for i in A:
    if i not in B:
        C += [i]

print(len(C))
print(*sorted(C))
