import sys
while 1:
    a, b, c = map(int,sys.stdin.readline().split())
    if a==b==c==0:
        break
    if b-a == c-b:
        print("AP", c + c-b)
    else:
        print("GP", c * (c//b))