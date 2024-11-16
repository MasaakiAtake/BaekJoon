n, m, k = map(int, input().split())
singer = [0 for _ in range(n)]

for _ in range(m):
  score = list(input().split())
  for i in range(0, len(score), 2):
    if singer[int(score[i])-1] < float(score[i+1]):
      singer[int(score[i])-1] = float(score[i+1])

singer.sort(reverse=True)
singer = singer[:k]

print(round(sum(singer),1))