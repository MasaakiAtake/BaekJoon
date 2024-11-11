'''
신호등 개수 N, 도로의 길이 L
신호등의 위치 D, 빨간불 지속시간 R, 파란불 지속 시간 G

* 1초에 1m씩 움직인다.
'''

from sys import stdin

N,L = map(int, stdin.readline().split())
## 총 걸린 시간(현재 시간)
total = 0

previous_D = 0
for _ in range(N):
    D,R,G = map(int, stdin.readline().split())
    ## 처음으로 신호등을 만났을 경우
    if previous_D == 0:
        total += D
        previous_D = D
    ## 두번째 이상 신호등을 만났을 경우
    else:
        # N-1번 째 신호등에서 N번째 신호등으로 이동한 시간 더하기
        total += D - previous_D
        # 새로운 이전 신호등의 위치 기록
        previous_D = D
    
    ##신호등을 기다린 시간 추가
    # 현재 신호등 불 판별
    remainder = total % (R+G)
    if remainder- R > 0:    #초록불이 켜짐
        pass
    else:   # 빨간불 켜짐
        total += R - remainder 
        
# 나머지 거리를 가는 시간 추가
total += L - previous_D
print(total)