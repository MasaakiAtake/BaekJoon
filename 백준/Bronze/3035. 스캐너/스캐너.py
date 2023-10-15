r, c, zr, zc = map(int,input().split())
paper = []
scanner = []

for _ in range(r):
    paper.append(input())
for i in range(r):
    row = []
    for j in range(c):
        row.append(paper[i][j] * zc)

    for _ in range(zr):
        scanner.append(row)
for s in scanner:
    print(''.join(s))