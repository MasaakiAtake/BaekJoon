N, M = map(int,input().split())
A = [[] for _ in range(N)]

for i in range(N):
    A[i] = list(map(int,input()))

ans = []

if N >= M:
    size = M
else:
    size = N

i = 0
j = 0

#A는 A[11][10] 크기임 -> 사실은 A[10][9]까지 밖에 없음.
while size > 0:
    
    if A[i][j] == A[i+size-1][j] == A[i][j+size-1] == A[i+size-1][j+size-1]:
        ans.append(size**2)
    
    j += 1
    
    if j+size-1 >= M:
        j = 0
        i += 1
        
    if i+size-1 >= N:
        size -= 1
        i = 0
        j = 0
        
print(max(ans))