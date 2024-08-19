from collections import deque

M, N, K = map(int, input().split())
graph = [[0]*(N) for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for i in range(y1, y2):
            graph[i][j] = '*'

def bfs(x, y):
    dxs = [1, 0, -1, 0]
    dys = [0, -1, 0, 1]
    q = deque()
    q.append((x, y))
    graph[x][y] = 1
    max_squre = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + dxs[i]
            dy = y + dys[i]
            if 0<=dx<M and 0<=dy<N and graph[dx][dy]==0:
                max_squre += 1 
                q.append((dx, dy))
                graph[dx][dy] = max_squre
    return max_squre

cnt = 0
result = []
for i in range(M):
    for j in range(N):
        if graph[i][j]==0:
            cnt += 1
            result.append(bfs(i,j))
print(cnt)
result_sort = sorted(result)
for i in result_sort:
    print(i, end=' ')
print()