n = int(input())
con = list(map(int,input().split()))

max_true = -1

for i in range(n+1):
    true_con = con.count(i)

    if true_con == i:
        max_true = max(max_true, i)

print(max_true)