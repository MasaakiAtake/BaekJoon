for _ in range(3):
    s = input()
    len_max = 0
    cnt = 1
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            cnt += 1
        else:
            cnt = 1

        if cnt > len_max:
            len_max = cnt
    print(len_max)