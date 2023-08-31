import sys
input = sys.stdin.readline

# 테스트케이스
for _ in range(3):
    # 입력
    n = int(input())
    _sum = 0

    for _ in range(n):
        _sum += int(input())

    # 출력
    if _sum == 0:
        print(0)
    elif _sum < 0:
        print("-")
    else:
        print("+")