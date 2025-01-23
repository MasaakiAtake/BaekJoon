import sys; input = sys.stdin.readline

while True:
    # EOF 처리
    try:
        n = int(input())
    except:
        break

    # 숫자를 문자열로 처리하여 나타나는지 확인할 것이기 때문에 dictionary 형태로 만들자.
    appear = {'0': False, '1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False, '8': False, '9': False}

    rest = 10 # 나타나지 않은 숫자의 개수
    # n, 2n, 3n, ..., kn 형태이므로 n을 더해주면서 자리마다 숫자를 체크해주자.
    S = k = 0

    # 나타나지 않은 숫자의 개수가 0이 될 때까지
    while rest:
        k += 1
        S += n
        for m in str(S): # 자리마다 체크
            if not appear[m]: # 만약 나타나지 않은 숫자이면 체크
                appear[m] = True
                rest -= 1
                if not rest: # 나타나지 않은 숫자가 없으면 탐색 중단
                    break
    print(k)