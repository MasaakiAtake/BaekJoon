N = int(input())
li = list(map(int, input().split()))
sorted_li = sorted(li)
res = [i for i in range(N) if li[i] != sorted_li[i]]
print(len(res))