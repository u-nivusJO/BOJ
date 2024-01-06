dxs = [1,0,0,-1]
dys = [0,1,-1,0]

# dfs
import sys 
sys.setrecursionlimit(10**6) 

def dfs(x, y):
    graph[x][y]=0
    for i in range(4):
        dx = x+dxs[i]
        dy = y+dys[i]
        if 0<=dx<N and 0<=dy<M and graph[dx][dy]==1:
            dfs(dx, dy)

# bfs
from collections import deque
def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y]=0
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + dxs[i]
            dy = y + dys[i]
            if 0<=dx<N and 0<=dy<M and graph[dx][dy]==1:
                q.append((dx,dy))
                graph[dx][dy]=0
    
    

T = int(input())
for t in range(T):
    result = 0
    M, N, K = map(int, input().split())
    graph =[[0]*M for _ in range(N)]
    for k in range(K):
        Y, X = map(int, input().split())
        graph[X][Y] = 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(i,j)
                # bfs(i,j)
                result += 1
    print(result)
    
