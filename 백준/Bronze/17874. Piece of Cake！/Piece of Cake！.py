n, h,v = map(int,input().split())
re = max(v, n-v) * max(h, n-h)
print(re*4)