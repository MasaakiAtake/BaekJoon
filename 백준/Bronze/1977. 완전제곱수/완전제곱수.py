m = int(input())
n = int(input())

sum = 0
min = float("inf")

for i in range(m, n + 1):
  if i ** 0.5 == int(i ** 0.5):
    sum += i
    if i < min:
      min = i

if sum == 0:
  print(-1)
else:
  print(sum)
  print(min)