import math

n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    my_lcm = math.lcm(a, b)
    print(my_lcm)