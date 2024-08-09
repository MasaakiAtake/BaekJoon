while True :
    a, b = input().split()
    ah, am = map(int, a.split(":"))
    bh, bm = map(int, b.split(":"))
    if ah == am == bh == bm == 0 : break
    ft, fm = ah + bh, am + bm
    if fm > 59 :
        ft += 1
        fm -= 60
    if ft > 23 : print("{0}:{1} +{2}".format(str(ft % 24).zfill(2), str(fm).zfill(2), ft // 24))
    else : print("{0}:{1}".format(str(ft).zfill(2), str(fm).zfill(2)))