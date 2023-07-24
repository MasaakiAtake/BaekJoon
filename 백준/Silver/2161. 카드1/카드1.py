n = int(input())
li = []
new_li = []

for i in range(1,n+1):
    li.append(i)
li.sort()

while True:
    new_li.append(li.pop(0))
    if not li:
        break
    li.append(li.pop(0))

print(*new_li)