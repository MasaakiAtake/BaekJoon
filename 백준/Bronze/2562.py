list1 = [[]]
for i in range(9):
    list1.append(int(input()))
    for j in range(9):
        list1.append(int(input()))
print(max(list1))
print(list1.index(max(list1))+1, list1.index(max(list1))+1)