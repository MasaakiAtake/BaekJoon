n = int(input())
cun_0 = 0
cun_1 = 0

for _ in range(n):
    inp = int(input())
    if inp == 0:
        cun_0 += 1
    if inp == 1:
        cun_1 += 1
if cun_0 > cun_1:
    print("Junhee is not cute!")
if cun_0 < cun_1:
    print("Junhee is cute!")