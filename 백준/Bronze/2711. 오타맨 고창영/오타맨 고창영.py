for _ in range(int(input())):
    a, b = map(str,input().split())
    res = list(b)
    res.pop(int(a)-1)
    print("".join(res))