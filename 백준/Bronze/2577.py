a = int(input())
b = int(input())
c = int(input())

x_num = list(str(a * b * c))

anslist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for num in x_num:
    anslist[int(num)] += 1
    
for ans in anslist:
    print(ans)