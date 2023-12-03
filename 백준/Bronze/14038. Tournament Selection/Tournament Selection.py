temp = 0

for i in range(6):
    n = input()
    if n == 'W':
        temp += 1

if temp == 1 or temp == 2:
    print(3)
elif temp == 3 or temp == 4:
    print(2)
elif temp == 5 or temp == 6:
    print(1)
else:
    print(-1)