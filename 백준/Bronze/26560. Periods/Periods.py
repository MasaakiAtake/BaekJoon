def sol(s):
    if s[-1] != '.':
        return s + '.'
    else:
        return s
 
 
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print(sol(s))