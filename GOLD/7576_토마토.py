M, N = map(int, input().split())
tomatos = []
for _ in range(N):
    tomatos.append(list(map(int, input().split())))
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

# BFS
from collections import deque
def bfs():
    while q:
        x, y = q.popleft()
        for s in range(4):
            dx = x + dxs[s]
            dy = y + dys[s]
            if 0<=dx<N and 0<=dy<M and tomatos[dx][dy]==0:
                    tomatos[dx][dy]=tomatos[x][y]+1
                    q.append((dx,dy))

q = deque()                    
for i in range(N):
    for j in range(M):
        if tomatos[i][j]==1:
            q.append((i,j))

bfs()
day = 0
for row in tomatos:
    for tomato in row:
        if tomato==0:
            print(-1)
            exit()
    day = max(day, max(row))
print(day-1)