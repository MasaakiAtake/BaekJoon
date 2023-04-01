import math
def lcm(n, m):
    return (n/ math.gcd(n, m)) * m

n, m = map(int, input().split())
print(math.gcd(n, m))
print(math.floor(lcm(n, m)))