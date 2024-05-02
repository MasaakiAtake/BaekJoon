p = int(input())
q = int(input())

#인구 100만 명당, 환자 최대 50명 이하 / 입원환자 10명 이하
if p <= 50 and q <= 10:
    print("White")

#인구 100만 명당, 입원 환자 30명 초과
elif q > 30:
    print("Red")

# 그 외
else:
    print("Yellow")