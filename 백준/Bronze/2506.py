N = int(input())
nline = list(map(int, input().split()))
cut = 0
point = 0

for i in range(N):
    if nline[i] == 1:
        cut += 1
        point += cut
    else:
        cut = 0
print(point)