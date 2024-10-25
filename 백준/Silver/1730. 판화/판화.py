N = int(input())
order = input()
board = [["."]*N for _ in range(N)]
# print(board)
# print(order)

x = 0
y = 0
count = 2
key = True
for i in order :
    if i == "D" or i == "U" :
        if i == "U" and  x == 0 :
            continue
        elif i == "D" and x == N-1:
            continue
        for j in range(count) :                   
            if board[x][y]=="-":
                board[x][y]="+"
            elif board[x][y]==".":
                board[x][y]="|"
            if i =="D" :
                if j == 0 :
                    x+=1
            else:
                if j == 0 :
                    x-=1   
                
    else :
        if i == "L" and  y == 0 :
                continue
        elif i == "R" and y == N-1:
            continue
        for j in range(count) :
 
            if board[x][y]=="|":
                board[x][y]="+"
            elif board[x][y]==".":
                board[x][y]="-"
            if i =="R" :
                if j == 0 :
                    y+=1
            else:
                if j == 0 :
                    y-=1   
                
                
for i in range(N):
    for j in range(N):
        print(f'{board[i][j]}',end="")
    print()