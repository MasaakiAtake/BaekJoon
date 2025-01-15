def is_palindrome(a):
    return a == a[::-1]

def jinsu(n, m):
    hihi = []
    while True:
        if n // m == 0:
            hihi.append(n)
            break
        hihi.append(n%m)
        n = n // m
    hihi.reverse()
    return "".join(map(str,hihi))
    
n = int(input())
printed = False
for i in range(2, 11):
    if is_palindrome(jinsu(n,i)):
        printed = True
        print(i, jinsu(n, i))
        
if not printed:
    print("NIE")