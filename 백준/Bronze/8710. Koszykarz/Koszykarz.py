k, w, m = map(int, input().split())

if k >= w:
    print("0")
else:
    height = w - k

    hits = height // m
    if height % m != 0:
        hits += 1

    print(hits)