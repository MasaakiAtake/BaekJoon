n = int(input())

for _ in range(n):
	s = []
	N, M = map(list, input().split())
	for i in range(len(N)):
		if ord(N[i]) <= ord(M[i]):
			s.append(ord(M[i]) - ord(N[i]))
		else:
			s.append(ord(M[i]) + 26 - ord(N[i]))
	print('Distances: ', end ='')
	for i in s:
		print(i, end=' ')
	print()