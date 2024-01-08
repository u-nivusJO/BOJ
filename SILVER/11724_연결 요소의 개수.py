# dfs
import sys
sys.setrecursionlimit(10**6)
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i]==False:
            dfs(i)
# bfs
from collections import deque
def bfs(v):
    q = deque([v])
    visited[v]=True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i]==False:
                visited[i]=True
                q.append(i)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
visited =[False]*(N+1)
result = 0
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for v in range(1, N+1):
    if visited[v]==False:
        # dfs(v)
        bfs(v)
        result+=1
print(result)


