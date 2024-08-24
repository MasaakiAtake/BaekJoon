import sys

while True:
    try:
        result_x = 0 #4번째 점의 x좌표
        result_y = 0 #4번째 점의 y좌표
        common = [] # 두 변의 공통된 좌표가 저장된다
        x= list(map(float,sys.stdin.readline().split())) #주어진 좌표를 입력 받는다
        
        # 두 변의 공통된 좌표를 common에 저장한다.
        for i in range(2,4):
            if x[0]==x[2*i] and x[1] == x[(2*i)+1]:
                common = [x[2*i],x[(2*i)+1]]
            elif x[2] == x[2*i]  and x[3] == x[2*i+1]:
                common = [x[2*i],x[2*i+1]]
		
        # 배열 x에 저장된 공통좌표를 제거한다.
        for i in range(2,-1,-1):
            if common[0] == x[2*i] and common[1] == x[2*i+1]:
                x.pop(2*i)
                x.pop(2*i)
		
        result_x = common[0] - (x[0]+x[2])
        result_y = common[1] - (x[1]+x[3])
        
        # 대칭이동
        if result_x !=0:
            result_x = -result_x
        if result_y !=0:
            result_y = -result_y
        
        print("%.3f" % result_x, "%.3f" % result_y)

    except:
        break