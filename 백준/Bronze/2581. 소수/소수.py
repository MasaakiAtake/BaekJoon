# 素数を判定する関数
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 2つの数を入力する
a = int(input())
b = int(input())

# 소수의 합과 최소값을 저장하는 변수 초기화
prime_sum = 0
min_prime = 10001

# M 이상 N 이하의 자연수 중 소수인 것을 찾아 prime_sum과 min_prime 계산
for num in range(a, b+1):
    if is_prime(num):
        prime_sum += num
        min_prime = min(min_prime, num)

# 소수가 없는 경우 -1 출력, 그 외에는 prime_sum과 min_prime 출력
if prime_sum == 0:
    print(-1)
else:
    print(prime_sum)
    print(min_prime)