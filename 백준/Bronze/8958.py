N = int(input())
for _ in range(N):
    score = 0
    cnt = 0
    ox = input()
    for j in range(len(ox)):
        if ox[j] == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)