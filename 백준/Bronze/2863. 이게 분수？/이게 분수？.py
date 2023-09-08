def swap(l):
    temp = l[0][0]
    l[0][0] = l[1][0]
    l[1][0] = l[1][1]
    l[1][1] = l[0][1]
    l[0][1] = temp
    return l

def cal(l):
    return l[0][0] / l[1][0] + l[0][1] / l[1][1]


l = [list(map(int, input().split())) for x in range(2)]
result = [cal(l)]
count = 0
for i in range(3):
    result.append(cal(swap(l)))
print(result.index(max(result)))