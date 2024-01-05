# bfs
from collections import deque

def find_land(x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(8):
            dx = x + dxs[i]
            dy = y + dys[i]
            if 0<=dx<h and 0<=dy<w and graph[dx][dy]==1:
                q.append((dx,dy))
                graph[dx][dy] = 0

# dfs
import sys
sys.setrecursionlimit(10**6)

# dfs
def find_land(x,y):
    graph[x][y] = 0
    for i in range(8):
        dx = x + dxs[i]
        dy = y + dys[i]
        if 0<=dx<h and 0<=dy<w and graph[dx][dy]==1:
            find_land(dx,dy)



dxs = [-1, -1, -1, 0, 0, 1, 1, 1]
dys = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    result = 0
    w, h = map(int, input().split())
    if w == h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                find_land(i, j)
                graph[i][j] = 0
                result += 1
    print(result)