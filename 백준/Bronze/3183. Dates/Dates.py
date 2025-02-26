import sys

def is_leap_year(y):
    
    if y % 4 == 0 and y % 100 != 0:
        return True
    
    if y % 4 == 0 and y % 400 == 0:
        return True
    
    return False

date_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date_range = dict(zip(list(range(1, 12 + 1)), date_list))

while True:
    dd, mm, yyyy = map(int, sys.stdin.readline().split())

    if dd == mm == yyyy == 0:
        break

    is_valid = True

    if mm in date_range:
        s, e = 1, date_range[mm]

        if mm == 2 and is_leap_year(yyyy):
            e += 1
        
        if dd < s or e < dd:
            is_valid = False
    else:
        is_valid = False

    if is_valid:
        print('Valid')
    else:
        print('Invalid')