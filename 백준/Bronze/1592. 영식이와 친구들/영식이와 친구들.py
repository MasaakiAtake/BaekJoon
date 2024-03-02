n, m, l = map(int,input().split())
li = [0]*n
cnt = i = 0
while li[i] < m-1:
    li[i] += 1
    cnt += 1
    i = (i&l)%n if li[i]&2 == 1 else (i-l)%n
print(cnt)