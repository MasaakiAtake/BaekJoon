datalis = []
cun = 0
for i in range(5):
    datalis.append(input())
for j in range(len(datalis)):
    if "FBI" in datalis[j]:
        print(j+1, end=" ")
        cun = 1
if cun == 0:
    print('HE GOT AWAY!')