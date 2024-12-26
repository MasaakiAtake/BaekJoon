from sys import stdin

def distance(p1,p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

T = int(stdin.readline())
for _ in range(T):
    arr = []
    for _ in range(4):
        x,y = map(int,stdin.readline().split())
        arr.append((x,y))
    arr.sort()    
    # 가장 x 좌표가 작은 점, x 좌표가 같다면 y 좌표가 작은 점
    p = arr[0]
    # 반시계 방향으로 정렬
    arr[2],arr[3] = arr[3],arr[2]
    # 변의 길이
    d = distance(p,arr[1])
    # 대각선의 길이
    l = distance(p,arr[2])
    ans = 1
    for i in range(1,4):
        if d != distance(arr[i],arr[(i+1)%4]):
            ans = 0
    if l != distance(arr[1],arr[3]):
        ans = 0
    print(ans)