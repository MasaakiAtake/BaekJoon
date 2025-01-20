A, a, B, b, P = map(int, input().split())

# 두 고리 중 하나라도 판보다 크다면 불가능하다.
if A > P or B > P:
    print('No')

# 두 고리를 나란히 자르는 경우
elif A + B <= P:
    print('Yes')

# 고리 A 안에 고리 B가 포함되는 경우
elif a >= B:
    print('Yes')

# 고리 B 안에 고리 A가 포함되는 경우
elif b >= A:
    print('Yes')

# 위 세 경우에 포함되지 않으면 불가능하다.
else:
    print('No')