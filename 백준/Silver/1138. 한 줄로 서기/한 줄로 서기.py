from sys import stdin,setrecursionlimit
input = stdin.readline

N = int(input()) # 사람의 수
N_list = list(map(int,input().split())) # 왼쪽에 키 큰사람 
cm = list(range(1,N+1)) # 1, 2, 3, 4 키순
result = []

j = -1
for i in range(N):
    result.insert(N_list[j], cm[j])
    j -=1

for i in result:
    print(i , end = ' ')