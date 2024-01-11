import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0]*(n+1)


# dfs
sys.setrecursionlimit(10**6)
def dfs(v):
    for i in graph[v]:
       if visited[i] == 0:
           visited[i] = visited[v]+1
           dfs(i)
dfs(a)


# bfs
from collections import deque
def bfs(v):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                q.append(i)
bfs(a) 


if visited[b] > 0:
    print(visited[b])
else: 
    print(-1)
        