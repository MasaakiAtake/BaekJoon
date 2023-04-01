autput = []
for _ in range(2):
    a, b, c, d, e = list(map(int,input().split()))
    autput.append((a*6)+(b*3)+(c*2)+d+(e*2))
for i in autput:
    print(i, end=" ")