n = int(input())
result_a = 0
result_b = 0

for i in range(n):
    a, b = map(int,input().split())
    if a > b:
        result_a += (a+b)
    elif a == b:
        result_a += a
        result_b += b
    else:
        result_b += (a+b)
print(result_a, result_b)