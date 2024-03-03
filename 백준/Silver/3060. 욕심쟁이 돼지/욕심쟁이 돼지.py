for _ in range(int(input())):
    su = int(input())
    food = sum(list(map(int,input().split())))
    day = 1

    while su >= food:
        day += 1
        food *= 4
    print(day)