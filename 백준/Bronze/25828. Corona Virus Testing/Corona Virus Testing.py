g,p,t = map(int, input().split())
s1,s2 = g*p, g + p*t
if s1 < s2:
    print(1)
elif s1 > s2:
    print(2)
else:
    print(0)