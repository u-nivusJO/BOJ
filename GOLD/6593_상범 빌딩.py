from collections import deque

def bfs(L, R, C, x, y, z):
    dxs = [1, -1, 0, 0, 0, 0]
    dys = [0, 0, 1, -1, 0, 0]
    dzs = [0, 0, 0, 0, 1, -1]
    
    q = deque()
    q.append((x, y, z))
    building[z][x][y] = 0
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            dx = x + dxs[i]
            dy = y + dys[i]
            dz = z + dzs[i]
            if 0<=dx<R and 0<=dy<C and 0<=dz<L:
                if building[dz][dx][dy]=='E':
                  return building[z][x][y] + 1
                if building[dz][dx][dy]=='.':
                    q.append((dx, dy, dz))
                    building[dz][dx][dy] = building[z][x][y] + 1
    return False

while True:
    L, R, C = map(int, input().split()) # z, x, y
    if L == R == C == 0:
        exit()
    else:
        building = []
        for _ in range(L):
            temp_floor = []
            for _ in range(R):
                 temp_floor.append(list(input()))
            input()
            building.append(temp_floor)
        result = 0
        for k in range(L):
            for i in range(R):
                for j in range(C):
                    if building[k][i][j]=='S':
                        result = bfs(L, R, C, i, j, k)
        if result != False:
            print(f"Escaped in {result} minute(s).")
        else:
            print("Trapped!")