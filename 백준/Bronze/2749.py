import sys

def Fib(n):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n-2):
            a, b = b, a + b
        return b
n = int(sys.stdin.readline())
result = Fib(n+1)
print(result % 1000000)