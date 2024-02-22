n = int(input())
li = ['.' * (n+2)] + ['.' + input()+'.' for _ in range(n)] + ['.'*(n+2)]
res = []
for i in range(n):
    i += 1
    s = ''
    for j in range(n):
        j += 1
        if ord('0') <= ord(li[i][j]) <= ord('9'):
            s += '*'
        else:
            bomb = 0
            for a in range(i-1, i+2):
                for b in range(j-1, j+2):
                    if ord('0') <= ord(li[a][b]) <= ord('9'):
                        bomb += int(li[a][b])
            s += str(bomb) if bomb < 10 else "M"
    res.append(s)
for s in res:
    print(s)