T = int(input())
A = 300
B = 60
C = 10
a_count = 0
b_count = 0
c_count = 0

if T % C == 0:
    while T >= A:
        a_count += 1
        T -= A
    while T >= B:
        b_count += 1
        T -= B
    while T >= C:
        c_count += 1
        T -= C
    print(a_count, b_count, c_count)
else:
    print(-1)