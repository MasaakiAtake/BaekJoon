# 문자열이 꼭 중앙에 위치해야 하는 것은 아님
# 문자열의 길이는 100이하 자연수 이므로 홀수가 올 수도 있음

def S_sum(S):        # 좌우 구간 각각의 합을 비교하는 함수
    S_L_sum = sum(int(num) for num in S[:len(S) // 2])
    S_R_sum = sum(int(num) for num in S[len(S) // 2:])
    if S_L_sum == S_R_sum:
        return True


def S_sliced_len(S):
    L = len(S)
    if L % 2:        # 문자열의 길이가 홀수일 경우
        S1 = S[:-1]
        S2 = S[1:]
        for i in range(0, L, 2):
            for j in range(0, i + 1, 2):
                S_sliced = S1[j:L - 1 - i + j]
                if S_sum(S_sliced):
                    result = len(S_sliced)
                    return result
            for j in range(0, i + 1, 2):
                S_sliced = S2[j:L - 1 - i + j]
                if S_sum(S_sliced):
                    result = len(S_sliced)
                    return result

    else:            # 문자열의 길이가 짝수일 경우
        for i in range(0, L + 1, 2):    # 부분 문자열 길이에 대한 for문
            for j in range(0, i + 1):    # 부분 문자열 위치에 대한 for문
                S_sliced = S[j:L - i + j]
                if S_sum(S_sliced):        # 부분 문자열 좌우구간 합이 같으면 실행
                    return len(S_sliced)


S = input()
print(S_sliced_len(S))