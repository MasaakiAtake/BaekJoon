import sys
a, b, c = map(int,sys.stdin.readline().split())
cal = max([a, b, c])*3 - sum([a, b, c])
print(cal)