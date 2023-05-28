n = int(input())

for _ in range(n):
    inp = list(map(int,input().split()))
    temp = []
    for i in inp:
        if i % 2 == 0:
            temp.append(i)
    print(sum(temp),min(temp))