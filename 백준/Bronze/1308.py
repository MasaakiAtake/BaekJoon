import datetime
import sys

a, b, c = map(int,sys.stdin.readline().split())
x = datetime.date(a, b, c)
d, e, f = map(int,sys.stdin.readline().split())
y = datetime.date(d, e, f)

dday = y - x
if dday.days >=365242:
    print("gg")
else:
    print("D-"+str(y-x)[0]+str(y-x)[1])