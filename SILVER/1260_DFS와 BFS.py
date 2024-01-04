from collections import deque
N, M, V = map(int, input().split())
graph = [[False]*(N+1) for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    
visited_dfs = [False]*(N+1)
visited_bfs = [False]*(N+1)

def dfs(V):
    print(V, end=' ')
    visited_dfs[V] = True
    for i in range(1, N+1):
        if not visited_dfs[i] and graph[V][i]:
            dfs(i)

def bfs(V):
    que = deque([V])
    visited_bfs[V] = True
    while que:
        V = que.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if not visited_bfs[i] and graph[V][i]:
                que.append(i)
                visited_bfs[i] = True

dfs(V)
print()
bfs(V)