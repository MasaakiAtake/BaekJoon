def mul(s):
    res = 1
    for c in s:
        res *= int(c)
    return res
    
n = input()

check = False
for i in range(1, len(n)):
    s1 = n[:i]
    s2 = n[i:]
    res1 = mul(s1)
    res2 = mul(s2)
    if res1 == res2:
        check = True
        break

if check == True:
    print("YES")
else:
    print("NO")