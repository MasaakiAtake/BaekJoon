# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 테스트 케이스의 개수를 입력합니다.
# 정수형으로 변환합니다.
test_case = int(stdin.readline())

# 테스트 케이스의 개수만큼 반복합니다.
for test_case_idx in range(test_case):
    # 12개의 실수들을 공백으로 구분해 입력합니다.
    # 각각 실수형으로 변환하고 리스트 변수에 넣어줍니다.
    floats = list(map(float, stdin.readline().split(' ')))
    # 첫 번째 플레이어의 점수를 저장할 변수를 선언합니다.
    N = 0
    # 두 번째 플레이어의 점수를 저장할 변수를 선언합니다.
    M = 0
    # 게임을 승리한 사람에 대한 문구를 저장할 변수를 선언합니다.
    winner = None

    # 12개의 실수들에서 한 쌍이 x, y 거리를 의미하므로
    # 2개씩 건너뛰면서 반복해봅니다.
    for idx in range(0, 12, 2):
        # 현재 다트의 점수를 저장할 변수를 선언합니다.
        point = 0
        # 중심으로부터 현재 다트의 거리를 저장하는 변수를 선언합니다.
        # 거리 계산 시, 마지막 루트 처리는 하지 않습니다.
        distance = floats[idx] ** 2 + floats[idx+1] ** 2

        # distance가 9보다 작거나 같다면
        if distance <= 9:
            # 현재 다트의 점수에 100점을 더합니다.
            point += 100
        # distance가 9보다 크고 36보다 작거나 같다면
        elif 9 < distance <= 36:
            # 현재 다트의 점수에 80점을 더합니다.
            point += 80
        # distance가 36보다 크고 81보다 작거나 같다면
        elif 36 < distance <= 81:
            # 현재 다트의 점수에 60점을 더합니다.
            point += 60
        # distance가 81보다 크고 144보다 작거나 같다면
        elif 81 < distance <= 144:
            # 현재 다트의 점수에 40점을 더합니다.
            point += 40
        # distance가 144보다 크고 225보다 작거나 같다면
        elif 144 < distance <= 225:
            # 현재 다트의 점수에 20점을 더합니다.
            point += 20

        # 현재 다트가 첫 번째 플레이어의 다트라면
        if 0 <= idx <= 4:
            # 첫 번째 플레이어의 점수에 현재 다트의 점수를 더해줍니다.
            N += point
        # 현재 다트가 두 번째 플레이어의 다트라면
        else:
            # 두 번째 플레이어의 점수에 현재 다트의 점수를 더해줍니다.
            M += point

    # 첫 번째 플레이어의 점수가 두 번째 플레이어의 점수보다 크다면
    if N > M:
        # winner에 PLAYER 1 WINS를 저장합니다.
        winner = "PLAYER 1 WINS"
    # 첫 번째 플레이어의 점수가 두 번째 플레이어의 점수보다 작다면
    elif N < M:
        # winner에 PLAYER 2 WINS를 저장합니다.
        winner = "PLAYER 2 WINS"
    # 두 선수의 점수가 같다면
    else:
        # winner에 TIE를 저장합니다.
        winner = "TIE"

    # 출력 형식에 맞게 출력합니다.
    print(f'SCORE: {N} to {M}, {winner}.')