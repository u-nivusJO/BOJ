from collections import deque

M, N, H = map(int, input().split())
tomatos = []
for _ in range(H):
    one_box = []
    for _ in range(N):
        one_box.append(list(map(int, input().split())))
    tomatos.append(one_box)

def bfs():
    dxs = [1, -1, 0, 0, 0, 0]
    dys = [0, 0, 1, -1, 0, 0]
    dzs =[0, 0, 0, 0, 1, -1]
    
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            dx = x + dxs[i]
            dy = y + dys[i]
            dz = z + dzs[i]
            if 0<=dx<N and 0<=dy<M and 0<=dz<H and tomatos[dz][dx][dy]==0:
                tomatos[dz][dx][dy] = tomatos[z][x][y] + 1
                q.append((dx, dy, dz))

q = deque()
for i in range(N):
    for j in range(M):
        for k in range(H):
            if tomatos[k][i][j] == 1:
                q.append((i, j, k))
bfs()

max_day = 0
for hight in tomatos:
    for row in hight:
        if 0 in row:
            print(-1)
            exit()
        else:
            max_day = max(max_day, max(row))
print(max_day-1)