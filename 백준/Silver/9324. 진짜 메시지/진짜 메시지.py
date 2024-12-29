def sol(s):
    alpha = [0] * 26
    check = False
 
    for i in range(len(s)):
        if check:
            check = False
            continue
        alpha[ord(s[i]) - 65] += 1
 
        if alpha[ord(s[i]) - 65] == 3:
            if i == len(s) -1:
                return 'FAKE'
            if s[i] != s[i+1]:
                return 'FAKE'
 
            check = True
            alpha[ord(s[i]) - 65] = 0
 
    return 'OK'
 
t = int(input())
for i in range(t):
    s = input()
    print(sol(s))