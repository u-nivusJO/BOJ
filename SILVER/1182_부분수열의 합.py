import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
result = []
cnt = 0

def dfs(start):
    global cnt, result
    if sum(result) == S and len(result) > 0:
        cnt += 1
        
    for i in range(start, N):
        result.append(numbers[i])
        dfs(i+1)
        result.pop()
dfs(0)
print(cnt)