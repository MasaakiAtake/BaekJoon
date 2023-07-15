N = int(input())
first = 666#처음 666인 수
while N != 0:# N 이 0이 아니면 계속 반복
    if '666' in str(first): # 만약 666이란 문자열이 문자열(first)안에 있으면
        N = N-1# N을 1 감소시키고
        if N == 0:# 만약 N 이 0이면
            break# 반복문을 탈출한다.
    first = first + 1#first의 값을 1 증가시킨다.
print(first)