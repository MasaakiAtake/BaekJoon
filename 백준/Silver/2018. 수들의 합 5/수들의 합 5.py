n = int(input())
i, j = 1, 2
total = 3
temp = 0

while i <= n-1 and j <= n:
    if total < n:
        j += 1
        total += j
    else:
        if total == n:
            temp += 1
        i += 1
        total -= i-1
print(temp + 1)

