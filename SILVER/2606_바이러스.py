N = int(input())
M = int(input())
graph = [[False]*(N+1) for i in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
visited = [False]*(N+1)

# dfs
def dfs(V):
    visited[V]=True
    for i in range(1, N+1):
        if not visited[i] and graph[V][i]:
            dfs(i)
dfs(1)


# bfs
from collections import deque
def bfs(V):
    q = deque([V])
    visited[V]=True
    while q:
        V = q.popleft()
        for i in range(1, N+1):
            if not visited[i] and graph[V][i]:
                visited[i]=True
                q.append(i)
bfs(1)


print(visited.count(True)-1)