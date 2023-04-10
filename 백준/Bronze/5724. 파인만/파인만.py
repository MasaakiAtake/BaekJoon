def count_squares(n):
    count = 0
    for i in range(1, n+1):
        count += (n-i+1)**2
    return count

while True:
    a = int(input())
    if a == 0:
        break
    print(count_squares(a))