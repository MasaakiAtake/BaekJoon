n, m = map(int, input().split()) 
count = 0
result = ''
d = []
for i in range(n):
    d.append(input())

for i in range(m):
    A = [0,0,0,0] # a,c,g,t
    for j in range(n):
        if d[j][i] == 'A':
            A[0]+=1
        elif d[j][i] == 'C':
            A[1]+=1
        elif d[j][i] == 'G':
            A[2]+=1
        elif d[j][i] == 'T':
            A[3]+=1
    idx = A.index(max(A))
    if idx == 0:
        result += 'A'
    elif idx==1:
        result += 'C'
    elif idx==2:
        result += 'G'
    elif idx==3:
        result += 'T'  
    count += n - max(A)

print(result)
print(count)