import sys
input = sys.stdin.readline

def sol(board):
    cnt = 0

    for idx, val in enumerate(board):
        if val == 'X':
            cnt += 1
        else:
            if cnt == 0:
                continue
            else:
                if cnt % 2 == 0:
                    board = board[:idx].replace('X', 'A', 4 * (cnt//4)) + board[idx:]
                    board = board[:idx].replace('X', 'B') + board[idx:]
                    cnt = 0
                else:
                    return -1

    return board

if __name__ == '__main__':
    board = input()

    print(sol(board))