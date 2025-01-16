import sys


while True:
    g, t, a, d = map(int, sys.stdin.readline().split())
    if (g == -1):
        break
	
    # 조별예선 경기의 수
    pre = t*(t-1)//2*g
	
    # 토너먼트에 진출하는 팀의 수
    knockout = g*a+d
    
    # X: 총 경기 수, Y: 추가해야하는 팀 수
    x, y = 0, 0
    temp = 1
    while knockout > temp:
        x += temp
        temp *= 2
    
    y += temp-knockout
    x += pre

    print(f"{g}*{a}/{t}+{d}={x}+{y}")