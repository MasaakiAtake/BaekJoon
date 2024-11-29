# 30840KB 696ms

N = int(input())

types = set()
arr = []

for _ in range(N):
    a = input()
    types.add(a)
    arr.append(a)

longlines = 0

if len(types) == 1:
    print(len(arr))
else:
    for i in types:
        tmparr = arr[:]
        line = 0

        while i in tmparr:
            tmparr.remove(i)
        for i in range(1,len(tmparr)):
            if tmparr[i-1] == tmparr[i]:
                line += 1
            else:
                longlines = max(longlines, line)
                line = 0

            longlines = max(longlines, line)

    print(longlines+1)