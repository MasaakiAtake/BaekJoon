if __name__ == '__main__':
    for i in range(int(input())):
        input()
        N = int(input())
        candy = 0
        for j in range(N):
            candy += int(input())
        if candy % N == 0:
            print("YES")
        else:
            print("NO")