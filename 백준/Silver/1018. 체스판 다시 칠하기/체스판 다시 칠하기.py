n, m = map(int,input().split())
bor = []
result = []

for i in range(n):
    bor.append(input())

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0:
                    if bor[a][b] != 'B':
                        draw1 += 1
                    if bor[a][b] != 'W':
                        draw2 += 1
                else:
                    if bor[a][b] != 'W':
                        draw1 += 1
                    if bor[a][b] != 'B':
                        draw2 += 1
        result.append(draw1)
        result.append(draw2)

print(min(result))