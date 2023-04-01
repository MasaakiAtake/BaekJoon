a, b = map(int,input().split())
add = a + b
sub = a - b
if add > sub:
    print(add)
    print(sub)
else:
    print(sub)
    print(add)