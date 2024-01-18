n = int(input())
cun = 0
for i in range(1, 500):
    a = (i**2 + n) **0.5
    if a%1 == 0:
        cun += 1
print(cun)