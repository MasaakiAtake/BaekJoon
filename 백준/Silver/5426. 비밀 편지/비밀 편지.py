for i in range(int(input())):
    s = input()
    l = []
    for j in range(0, len(s), int(len(s) ** (0.5))):
        l.append(s[j:j+int(len(s) ** 0.5)])

    for j in range(int(len(s)**(0.5)) -1, -1, -1):
        for k in range(int(len(s)**(0.5))):
            print(l[k][j], end="")
    print("")