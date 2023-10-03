N, M = map(int,(input().split()))

d = list(map(int, input().split()))

result = 0
Max = 0

for i in range(N-2): 
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if d[i]+d[j]+d[k] > M:
                continue
            else:
                result = d[i]+d[j]+d[k]
                if Max <= result: 
                    Max = result

print(Max)