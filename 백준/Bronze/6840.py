import sys
from statistics import median

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
result = list(median(a, b, c))

print(result)