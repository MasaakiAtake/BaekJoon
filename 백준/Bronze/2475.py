a, b, c, d, e = list(map(int, input().split()))
a1 = a*a
b1 = b*b
c1 = c*c
d1 = d*d
e1 = e*e
result = (a1+b1+c1+d1+e1)%10
print(result)