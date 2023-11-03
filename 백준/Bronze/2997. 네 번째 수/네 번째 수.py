li = list(map(int,input().split()))
li.sort()

d = min(li[1]-li[0], li[2]-li[1])

for i in range(len(li)):
    temp = li[i]

    if temp+d not in li:
        print(temp+d)
        break