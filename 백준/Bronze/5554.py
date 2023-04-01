import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

temp = a+b+c+d
x = temp/60
y = temp%60

print(math.floor(x))
print(y)