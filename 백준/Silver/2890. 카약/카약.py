r, c = map(int,input().split())
x = []
result = []
check = []
rank = 1
result_team = []
# 각 레일별 팀들의 위치를 입력받는다
for i in range(r):
    x.append(list(input()))
# 3개의 숫자 중 앞의 숫자 2개를 지워준다
for i in range(r):
    cnt = 0
    for j in range(c):
        if x[i][j] != "S" and x[i][j] != "." and x[i][j] != "F":
            del x[i][j]
            cnt += 1
        if cnt == 2:
            break
# 선수가 없는 빈 레일을 지워준다
for i in x:
    check.append(len(i))
for i in range (len(check)):
    if check[i] == max(check):
        delete = i
del x[delete]

# 결승지점으로부터 가까이 있는 팀들에게 순위를 부여하고 그 팀의 번호를 저장한다
for i in range(1,c-1):
    cnt = 0
    for j in range(r-1):
        if x[j][-i] != "F" and x[j][-i] != "." and x[j][-i] != "S":
            result.append(rank) # result 배열에 순위를 저장
            result_team.append(int(x[j][-i])) # result_team에 팀의 번호를 저장
            cnt += 1
    if cnt > 0:
        rank += 1
# 1번팀부터 9번팀까지 그에 맞는 순위를 출력한다
for i in range(1,10):
    print(result[result_team.index(i)])