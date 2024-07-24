from datetime import datetime

def year_2009(D, M):
    weekday_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    return weekday_list[datetime(year=2009, month=M, day=D).weekday()]


if __name__ == "__main__":
    D, M = map(int, input().split())
    print(year_2009(D, M))