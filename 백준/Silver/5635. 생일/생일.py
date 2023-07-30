import sys
input = sys.stdin.readline

n = int(input())
st = []
for _ in range(n):
    n, d, m, y = input().split()
    st.append([n, int(d), int(m), int(y)])  # 2차원으로 리스트 추가
st.sort(key=lambda x: (x[3], x[2], x[1]))   # 년,월,일 순으로 정렬
print(st[-1][0])    # 가장 나이 적은 사람
print(st[0][0]) 