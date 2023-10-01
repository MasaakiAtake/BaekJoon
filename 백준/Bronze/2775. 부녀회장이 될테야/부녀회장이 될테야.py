inp = int(input())

for _ in range(inp):
    floa = int(input())
    room = int(input())
    f0 = [x for x in range(1, room+1)]
    for k in range(floa):
        for i in range(1, room):
            f0[i] += f0[i-1]
    print(f0[-1])