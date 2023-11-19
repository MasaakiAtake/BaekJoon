import sys

while 1:
	a = sys.stdin.readline().rstrip()
	if not a:
		break
	n, m = map(int,a.split())
	cnt = 0
	for i in range(n,m+1):
		dic = {}
		flag = 0
		for j in str(i):
			if j in dic:
				flag = 1
				break
			else:
				dic[j] = 1

		if flag == 0:
			cnt += 1
	print(cnt)