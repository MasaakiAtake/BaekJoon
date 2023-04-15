N = int(input())
S = input()
cut = 0

for i in range(N):
    if S[i] == 'a' or S[i] == 'i' or S[i] == 'u' or S[i] == 'e' or S[i] == 'o':
        cut += 1
print(cut)