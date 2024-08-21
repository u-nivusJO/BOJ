from collections import deque
from copy import deepcopy

N = int(input())
rgb_painting = list()
rb_painting = list()

for _ in range(N):
    row = input()
    row = list(row)
    rgb_painting.append(row)
    
    rgb_row = deepcopy(row)
    for i in range(len(rgb_row)):
        if rgb_row[i]=='G':
            rgb_row[i]='R'        
    rb_painting.append(rgb_row)

def bfs(x, y, color, painting):
    dxs = [1, 0, -1, 0]
    dys = [0, -1, 0, 1]
    
    q = deque()
    q.append((x, y))
    painting[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + dxs[i]
            dy = y + dys[i]
            if 0<=dx<N and 0<=dy<N and painting[dx][dy]==color:
                q.append((dx, dy))
                painting[dx][dy] = 0

rgb_cnt = 0
rb_cnt = 0
for i in range(N):
    for j in  range(N):
        if rgb_painting[i][j] != 0:
            rgb_cnt += 1
            bfs(i, j, rgb_painting[i][j], rgb_painting)
        if rb_painting[i][j] != 0:
            rb_cnt += 1
            bfs(i, j, rb_painting[i][j], rb_painting)
print(rgb_cnt, rb_cnt)