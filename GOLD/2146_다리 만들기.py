import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
island_map = []
result = sys.maxsize
for _ in range(N):
    temp_map = list(map(int, input().split())) 
    island_map.append(temp_map)

def bfs1(x, y, cnt):
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    q = deque()
    q.append((x, y))
    island_map[x][y] = cnt

    while q:
        x, y = q.popleft()
        for s in range(4):
            dx = x + dxs[s]
            dy = y + dys[s]
            if 0<=dx<N and 0<=dy<N and island_map[dx][dy]==1:
                q.append((dx, dy))
                island_map[dx][dy] = cnt

def bfs2(island):
    global result
    bridge = [[-1]*N for _ in range(N)]
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    q = deque()
    
    for i in range(N):
        for j in range(N):
            if island_map[i][j] == island:
                bridge[i][j] = 0
                q.append((i, j))
                
    while q:
        x, y = q.popleft()
        for s in range(4):
            dx = x + dxs[s]
            dy = y + dys[s]
            if 0<=dx<N and 0<=dy<N:
                if island_map[dx][dy] != 0 and island_map[dx][dy] != island:
                    result = min(result, bridge[x][y])
                    return
                elif island_map[dx][dy] == 0 and bridge[dx][dy] == -1:
                    bridge[dx][dy] = bridge[x][y] + 1
                    q.append((dx, dy))
                 

cnt = 1
for i in range(N):
    for j in range(N):
        if island_map[i][j] == 1:
            cnt += 1
            bfs1(i, j, cnt)

for island in range(2, cnt):
    bfs2(island)

print(result)