n = input()
f = int(input())

temp = int(n[:-2] + '00')

while True:
    if temp % f == 0:
        break
    temp += 1

print(str(temp)[-2:])