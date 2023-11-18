import sys

def Josephus(queue, K):
    result = list()
    num = K - 1
    for i in range(len(queue)):
        if (len(queue)>num):
            result.append(queue.pop(num))
            num += K - 1
        elif (len(queue) <= num):
            num = num%len(queue)
            result.append(queue.pop(num%len(queue)))
            num += K - 1
    return result

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    queue = list()
    for i in range(1, N + 1):
        queue.append(i)
    result = Josephus(queue, K)
    print('<', end='')
    for i in range(N):
        if (i != N -1):
            print(f'{result[i]}, ', end="")
        else:
            print(f'{result[i]}', end="")
    print('>', end="")