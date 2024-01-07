dxs = [1,0,0,-1]
dys = [0,-1,1,0,]
   
# bfs
from collections import deque
def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + dxs[i]
            dy = y + dys[i]
            if 0<=dx<N and 0<=dy<M and graph[dx][dy]==1:
                graph[dx][dy] = graph[x][y] + 1
                q.append((dx, dy))
            

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            bfs(i,j)
print(graph[-1][-1])
    