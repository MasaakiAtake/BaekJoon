import sys
inp = sys.stdin.readline()
inp = int(inp)
line = 1

while inp > line:
    inp -= line
    line += 1

if line % 2 == 0:
    a = inp
    b = line -inp + 1
elif line % 2 == 1:
    a = line - inp + 1
    b = inp
print(f'{a}/{b}')