import sys
n = input(sys.stdin.readline())
lst = [0]*26

for i in range(len(n)):
    lst[ord(i)-97] = n.count(i)

for i in lst:
    print(i, end=" ")