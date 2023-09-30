n = int(input())
for i in range(1, n+1):
    num = sum(map(int,str(i)))
    num_aum = i + num

    if num_aum == n:
        print(i)
        break
    if i == n:
        print(0)