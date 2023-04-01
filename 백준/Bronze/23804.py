import sys
input=sys.stdin.readline

N = int(input())

for i in range(5*N) :
    if i < N :
        for j in range(5*N) :
            print("@", end="")

    if i >= (5*N) - N :
        for j in range(5*N) :
            print("@", end="")

    if i >= N and i < (5*N) - N :
        for j in range(N) :
            print("@", end="")

    print()