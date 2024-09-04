while True :
    lst = list(map(int, input().split()))
    if sum(lst) == 0 : break
    score = sum(lst) - max(lst) - min(lst)
    if score / 4 % 1 == 0 : print(score // 4)
    else : print(score / 4)