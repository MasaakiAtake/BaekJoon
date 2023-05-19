N = int(input())
file_names = [input() for _ in range(N)]

pattern = ''
for i in range(len(file_names[0])):
    char = file_names[0][i]
    for j in range(1, N):
        if file_names[j][i] != char:
            pattern += '?'
            break
    else:
        pattern += char

print(pattern)