import sys
cun = 0
a, b, c = map(int,sys.stdin.readline().split())
d, e, f = map(int,sys.stdin.readline().split())

if a < d:
    cun += (d-a)
if b < e:
    cun += (e-b)
if c < f:
    cun += (f-c)

print(cun)