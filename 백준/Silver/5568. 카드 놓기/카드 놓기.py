import sys
n = int(input())
k = int(input())
nums = [sys.stdin.readline().strip() for _ in range(n)]

answer = []
arr = []
visited = [False] * n
def dfs(depth):
    if depth==k:
        answer.append(''.join(arr))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(nums[i])
            dfs(depth+1)
            arr.pop()
            visited[i] = False
dfs(0)
print(len(set(answer)))