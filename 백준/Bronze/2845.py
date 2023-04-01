A, B = map(int, input().split())
temp = A * B
li = list(map(int, input().split()))

for i in li:
    print(i - temp, end=' ')