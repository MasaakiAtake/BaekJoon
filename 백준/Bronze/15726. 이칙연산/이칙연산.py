a, b, c = map(int,input().split())

temp1 = a*b/c
temp2 = a/b*c

if temp1 < temp2:
    print(int(temp2))
else:
    print(int(temp1))