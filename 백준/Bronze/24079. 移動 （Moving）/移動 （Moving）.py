x = int(input())
y = int(input())
z = int(input())

temp = (x*60) + (y*60)
limit = (z*60 + 30)

if temp <= limit:
    print(1)
else:
    print(0)