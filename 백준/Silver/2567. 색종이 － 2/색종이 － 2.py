N = int(input())
arr=[[False for _ in range(101)] for _ in range(101)]  #가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지
for _ in range(N):
    x,y=map(int,input().split())
    for i in range(x,x+10):  # 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이
        for j in range(y,y+10): # 좌표가 아니라 영역이므로 range는 y~y+9
            arr[j][i] = True  # 색종이 영역 칠하기

total=0  # 둘레값 
dx=[0,0,1,-1]  # 4방향
dy=[1,-1,0,0]
for i in range(101):    # 흰색 도화지에서 색종이 영역 찾기
    for j in range(101):
        if arr[j][i] == True:  # 한점이 1일때
            tmp=0
            for k in range(4):
                if arr[j+dy[k]][i+dx[k]] == True:
                    tmp+=1
            # 그점의 4방향이 모두 1가 아니라면 그점은 둘레값
            if tmp == 3:  # 3방향이 1 라면 변의 길이
                total +=1
            elif tmp == 2: # 2방향이 1 라면 모서리의 길이 -> ㄱ 자 모양 => 가로, 세로 둘다 존재 하므로 +2
                total +=2

print(total)