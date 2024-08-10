dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

# DFS 
import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    area = 1
    graph[x][y]=0
    for s in range(4):
        dx = x + dxs[s]
        dy = y + dys[s]
        if 0<=dx<n and 0<=dy<m and graph[dx][dy]==1:
            area += dfs(dx,dy)
    return area

# BFS
from collections import deque
def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y]=0
    area = 1
    while q:
        x, y = q.popleft()
        for s in range(4):
            dx = x + dxs[s]
            dy = y + dys[s]
            if  0<=dx<n and 0<=dy<m and graph[dx][dy]==1:
                q.append((dx,dy))
                graph[dx][dy]=0
                area += 1
    return area
     

n, m = map(int, input().split())
graph = []
count = 0
area = [0]
for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            count += 1
            # area.append(dfs(i,j)) # dfs
            area.append(bfs(i,j)) # bfs

print(count)
print(max(area))