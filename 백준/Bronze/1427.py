n = input()
OrgList = []

for i in range(len(n)):
    OrgList.append(n[i])
OrgList.sort(reverse=True)
for i in OrgList:
    print(i, end="")