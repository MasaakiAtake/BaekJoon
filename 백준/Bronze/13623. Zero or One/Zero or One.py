a, b, c = map(int, input().split())
if a==b and b==c:
    print("*")
elif a==c:
    print("B")
elif b==c:
    print("A")
elif a==b:
    print("C")