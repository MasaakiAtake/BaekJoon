import sys
a, b, c, d = map(int,sys.stdin.readline().split())
e, f, g, h = map(int,sys.stdin.readline().split())
S = a+b+c+d
T = e+f+g+h

if S > T or S==T:
    print(S)
else:
    print(T)