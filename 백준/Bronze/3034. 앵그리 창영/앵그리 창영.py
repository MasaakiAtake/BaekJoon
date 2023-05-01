a,b,c = map(int,input().split())
for i in range(a):
    n = int(input())
    l = (b**2+c**2) ** 0.5
    if n <= l:
        print("DA")
    else:
        print("NE")