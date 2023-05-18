a, b, c = map(int, input().split())

if (a+b+c) < 100:
    if a == min(a, b, c):
        print("Soongsil")
    if b == min(a, b, c):
        print("Korea")
    if c == min(a, b, c):
        print("Hanyang")


else:
    print("OK")