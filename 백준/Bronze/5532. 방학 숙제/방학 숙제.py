l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

cut1 = 0
cut2 = 0

cut1 += a//c
if (a%c != 0):
    cut1 += 1

cut2 += b//d
if (b%d != 0):
    cut2 += 1

temp = l - max(cut1, cut2)

print(temp)