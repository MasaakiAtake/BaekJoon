import sys

n, m = map(int, sys.stdin.readline().split())
p = [int(sys.stdin.readline()) for _ in range(m)]
p.sort() 
res = 0 
target = 0 
for i in range(m):
    egg = min(m - i, n) 

    
    if res < p[i] * egg:
        res = p[i] * egg 
        target = p[i] 

print(target, res)