A, B = map(int, input().split())
C = int(input())
print(A+B if C*2 > A+B else (A+B)-(C*2))