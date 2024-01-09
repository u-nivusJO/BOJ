# dfs
import sys
input = sys.stdin.readline

dxs = [1, 0, 0, -1]
dys = [0, 1, -1, 0]

sys.setrecursionlimit(10**6)
def dfs(x,y,cnt):
    graph[x][y]=0
    for i in range(4):
        dx = x + dxs[i]
        dy = y + dys[i]
        if 0<=dx<N and 0<=dy<N and graph[dx][dy]==1:
            cnt = dfs(dx,dy,cnt+1)
    return cnt

N = int(input())
graph = []
result = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
    
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            result.append(dfs(i,j,cnt=1))

print(len(result))
result = sorted(result)
for r in result:
    print(r)
    
    


# bfs
import sys
input = sys.stdin.readline

dxs = [1, 0, 0, -1]
dys = [0, 1, -1, 0]

from collections import deque
def bfs(x,y):
    global cnt
    q = deque()
    graph[x][y]=0
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + dxs[i]
            dy = y + dys[i]
            if 0<=dx<N and 0<=dy<N and graph[dx][dy]==1:
                graph[dx][dy]=0
                q.append((dx,dy))
                cnt += 1
    return cnt

N = int(input())
graph = []
result = []
cnt = 1
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
    
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            result.append(bfs(i,j))
            cnt = 1

print(len(result))
result = sorted(result)
for r in result:
    print(r)