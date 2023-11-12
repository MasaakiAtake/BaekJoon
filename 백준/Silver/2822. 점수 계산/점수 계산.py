score = []
for i in range(8):
    score.append(int(input()))
temp = []
ans = 0

for i in range(5):
    ans += max(score)
    temp.append(score.index(max(score)) + 1)
    score[score.index(max(score))] = -1
temp.sort()
print(ans)
print(*temp)