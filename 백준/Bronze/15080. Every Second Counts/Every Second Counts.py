start = list(map(int,input().split(':')))
end = list(map(int,input().split(':')))

res = 0

if start[2] <= end[2]:
    res += end[2] - start[2]
else:
    end[1] -= 1
    res += end[2] - start[2] + 60


if start[1] <= end[1]:
    res += (end[1] - start[1])*60
else:
    end[0] -= 1
    res += (end[1] - start[1] + 60)*60


if start[0] <= end[0]:
    res += (end[0] - start[0])*3600
else:
    end[0] += 24
    res += (end[0] - start[0])*3600

print(res)
