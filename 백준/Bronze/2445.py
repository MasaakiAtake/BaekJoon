N = int(input())
for i in range(N):
    print("*" * i + " " * 2*(N-i) + "*" * i )
for j in range(N):
    print("*"* (N-j) + " " * 2*j + "*" * (N-j))