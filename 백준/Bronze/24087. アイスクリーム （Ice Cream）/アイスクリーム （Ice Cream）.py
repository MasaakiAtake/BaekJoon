s = int(input())
a = int(input())
b = int(input())
temp = 250

while True:
    if a >= s:
        break
    a += b
    temp += 100

print(temp)