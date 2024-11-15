N = int(input())
friend = [list(map(int, input().split('/'))) for _ in range(N)]
friend_split = [0, 0, 0]

for f in friend:
    if f[1] == 2:
        friend_split[0] += 1
    elif f[0] == 1:
        friend_split[1] += 1
    else:
        friend_split[2] += 1

result = 0

# 3/4와 1/4를 최대한
result += friend_split[2]
friend_split[1] -= friend_split[2]

# 1/2와 1/4를 최대한
if friend_split[1] > 0 and friend_split[0] > 0:
    tmp = friend_split[1] // 2 if friend_split[1] // 2 < friend_split[0] else friend_split[0]

    result += tmp
    friend_split[0] -= tmp
    friend_split[1] -= tmp * 2
    if friend_split[1] > 0:
        result += friend_split[1]
        friend_split[0] -= friend_split[1]
        friend_split[1] = 0

# 1/2 끼리
if friend_split[0] > 0:
    result += friend_split[0] // 2
    result += friend_split[0] % 2

# 1/4 끼리
if friend_split[1] > 0:
    result += friend_split[1] // 4
    result += 1 if friend_split[1] % 4 else 0

print(result)