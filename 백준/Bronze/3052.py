li = []
cut = 0
for i in range(10):    
    a = int(input())
    li.append(a%42)
arr = set(li)
print(len(arr))