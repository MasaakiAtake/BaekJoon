A, B, C = map(int,input().split())
D = int(input())

if 59 < C:
    C = 0
    B += 1
if 59 < B:
    B = 0
    A += 1
if 23 < A:
    A = 0
    B = 0
    C = 0

print(A, B, C)