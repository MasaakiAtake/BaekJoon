count = [0] * (1000 + 1)
sum = 0
for _ in range(10):
    num = int(input())
    sum += num
    count[num] += 1

print(sum // 10)
print(count.index(max(count)))