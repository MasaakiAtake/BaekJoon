import sys
from itertools import combinations

input = sys.stdin.readline
n, b = map(int, input().split())
arr = [int(input()) for _ in range(n)]
num = 10000000000001

for i in range(1, n+1):
    lst = list(combinations(arr, i))
    for j in lst:
        sum_num = sum(j)
        if sum_num >= b:
            num = min(num, sum_num)
print(num-b)