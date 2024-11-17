import sys
N = int(sys.stdin.readline())
dx = [0,0,-1,1,1,1,-1,-1]
dy = [1,-1,0,0,-1,1,1,-1]

def find_mine_count(x,y): # 주위 8방향에 지뢰의 개수 찾기
    count = 0
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=N:
            continue

        if pan[nx][ny]=='*':
            count += 1
    return count

def game_over(): # 지뢰 밟았을 때 시행되는 함수
    for i in range(N):
        for j in range(N):
            if pan[i][j]=='*':
                open[i][j] = '*'
       
pan = [] #지뢰 위치담을 배열
open = [] #열린칸 위치담을 배열
 
for i in range(N): # 입력값 받기
    line = list(map(str, sys.stdin.readline().strip()))
    pan.append(line)
for i in range(N):
    line = list(map(str, sys.stdin.readline().strip()))
    open.append(line)

for i in range(N):
    for j in range(N):
        if open[i][j]=='x':#열린칸이라면
            open[i][j] = find_mine_count(i,j) #주위 8방향에 지뢰의 개수가 들어가야한다.
            if pan[i][j]=='*': #근데 만약에 열린칸이 지뢰였다면
                game_over() #지뢰 밟은고임
               

for l in open: #출력
    for i in l:
        print(i,end='')
    print()