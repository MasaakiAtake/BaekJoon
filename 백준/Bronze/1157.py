from statistics import mode

li = input()
li_up = li.upper()
li_temp = mode(li_up)
if li_up.count(max(li_up)) >= 2:
    print("?")
else:
    (li_temp)


word = input().lower()
word_list = list(set(word))
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())