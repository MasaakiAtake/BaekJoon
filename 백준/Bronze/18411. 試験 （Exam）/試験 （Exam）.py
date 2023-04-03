from statistics import median

a = list(map(int,input().split()))
fa = max(a)
sec = median(a)
print(fa + sec)