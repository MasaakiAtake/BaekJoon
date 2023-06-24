import sys

word = list(map(int,sys.stdin.readline().strip()))
cun = 0

while len(word) > 1:
    cun += 1

    temp = []
    word = sum(word)

    for i in str(word):
        temp.append(int(i))
    
    word = temp

print(cun)

if word[0] % 3 == 0:
    print("YES")
else:
    print("NO")