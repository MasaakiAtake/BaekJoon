s = input()

cun = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cun += 1

print((cun+1)//2)