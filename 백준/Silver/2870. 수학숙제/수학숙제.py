import sys

n = int(sys.stdin.readline())

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

res = []

# 반복문을 통해 각 줄을 확인
for _ in range(n):
    m = list(map(str, sys.stdin.readline().strip("\n")))
    temp = []
    cnt = ""

    # 반복문을 통해 줄의 한단어씩 확인
    for i in m:
        # 단어가 숫자이면 cnt에 더한다.
        if i in nums:
            cnt += i

        # 단어가 숫자가 아니고 cnt에 숫자가 담겨있으면 temp에 추가한다.
        else:
            if cnt:
                temp.append(int(cnt))
                cnt = ""

    # 모든 단어를 확인 후에 cnt에 숫자가 담겨있으면 temp에 추가한다.
    if cnt:
        temp.append(int(cnt))

    # 모든 숫자를 res에 더한다.
    res += temp

# 오름차순으로 정렬 후 출력
res.sort()
for j in res:
    print(j)