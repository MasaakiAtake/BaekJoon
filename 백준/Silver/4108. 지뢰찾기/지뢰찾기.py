import sys; input = sys.stdin.readline

# 12시 방향부터 시계 방향으로 8방향
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

while True:
    R, C = map(int, input().split())
    if not R: break
    matrix = [input().strip() for _ in range(R)]

    # 주위 지뢰의 개수를 저장할 행렬
    result = [[0] * C for _ in range(R)]

    # 지뢰가 있는 칸을 찾아 인접해 있는 칸에 1을 더하자.
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '*':
                for di, dj in dir:
                    if 0 <= i + di < R and 0 <= j + dj < C:
                        result[i + di][j + dj] += 1

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '*': # 지뢰가 있는 칸
                print('*', end = '')
            else: # 지뢰가 없는 칸
                print(result[i][j], end = '')
        print()