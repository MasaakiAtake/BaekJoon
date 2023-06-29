from collections import Counter

N = int(input())
prize=[]
for n in range (N):
    dice = list(map(int, input().split()))
    cnt = Counter(dice)
    if 3 in cnt.values():
        prize.append(10000+1000*dice[0])
    elif 2 in cnt.values():
        for i in cnt.keys():
            if cnt[i]==2:
                prize.append(1000+100*i)
    else:
        prize.append(max(dice)*100)

    
print(max(prize))