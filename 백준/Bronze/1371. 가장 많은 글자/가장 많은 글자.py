import sys

s = sys.stdin.read()
li = [0]*26
for i in s:
    if i.islower():
        li[ord(i)-97] += 1

for k in range(26):
    if li[k] == max(li):
        print(chr(97+k), end='')