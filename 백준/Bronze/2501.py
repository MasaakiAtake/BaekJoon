import sys
arr = []
p, q = map(int,sys.stdin.readline().split())
cnt = 0

for i in range(1, p+1):
    if p % i == 0:
        arr.append(i)
    cnt += 1
if q > len(arr):
    print(0)
else:
    print(arr[q-1])