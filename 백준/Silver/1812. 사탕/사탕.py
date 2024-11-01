import sys
n = int(input())
lst = [int(sys.stdin.readline()) for i in range(n)]
result = []
first = 0

for idx, val in enumerate(lst):
    if idx % 2 == 0:
        first += val
    else:
        first -= val
result.append(first//2)

for i in range(n-1):
    result.append(lst[i]-result[i])

for i in result:
    print(i)