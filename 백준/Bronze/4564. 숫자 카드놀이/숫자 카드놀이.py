# 0을 입력할 때까지 계속 테스트 케이스를 반복합니다.
while True:
    # 시작값 S를 입력합니다.
    # 1 <= S <= 100,000
    S = input()

    # 0을 입력하면
    if S == '0':
        # 마지막 입력이므로 반복문을 탈출합니다.
        break

    # 각 테스트 케이스에서 시작값 S도 출력해야합니다.
    # 그리고 밑줄로 내리지 않기 위해 end=' '로 마지막에 한 칸을 띄어주는 처리를 해줍니다.
    print(S, end=' ')

    # 만약 시작값이 숫자 하나라면
    if len(S) == 1:
        # 그 자체로 끝이므로 출력 형식에서 밑줄로 내려줍니다.
        print()
        # 그리고 다음 테스트 케이스로 넘어갑니다.
        continue
    # 만약 시작값이 숫자 2자리 이상이라면
    else:
        # 한 자리 숫자가 될 때까지 카드놀이를 반복합니다.
        while True:
            # 각 자리 숫자를 모두 곱한 결과를 출력하는 변수를 선언합니다.
            result = 1

            # 시작값 S에서 각 자리 숫자마다 반복합니다.
            for i in S:
                # 각 자리 숫자를 모두 result 변수에 곱합니다.
                result *= int(i)

            # 각 자리 숫자를 모두 곱한 결과를 출력하고 출력 형식에 맞게 한 칸을 띄어줍니다.
            print(result, end=' ')

            # 이번에 나왔던 결과를 시작값 S 변수에 덮어쓰기합니다.
            S = str(result)

            # 각 자리 숫자를 모두 곱한 결과의 길이가 숫자 한 개라면
            if len(S) == 1:
                # 반복문을 탈출합니다.
                break

    # 한 줄마다 각각의 테스트 케이스의 결과를 출력하므로 한 줄 내려주는 처리를 합니다.
    print()