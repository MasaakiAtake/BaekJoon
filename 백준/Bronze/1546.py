N = int(input())
temp = 0
li = list(map(int,input().split()))
M = max(li)
for i in li:
    temp += i / M * 100
print(temp/N)