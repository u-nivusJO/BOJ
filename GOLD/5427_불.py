from collections import deque
import sys
input = sys.stdin.readline

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def fire_bfs():
    while fire_q:
        x, y = fire_q.popleft()
        for s in range(4):
            dx = x + dxs[s]
            dy = y + dys[s]
            if not (0<=dx<h and 0<=dy<w):
                continue
            if building_map[dx][dy] == '#' or fire[dx][dy]:
                continue
            fire[dx][dy] = fire[x][y] + 1
            fire_q.append((dx, dy))

def sk_bfs():
    while sk_q:
        x, y = sk_q.popleft()
        for s in range(4):
            dx = x + dxs[s]
            dy = y + dys[s]
            if not (0<=dx<h and 0<=dy<w):
                print(sk[x][y])
                return
            if building_map[dx][dy] == '#' or sk[dx][dy]:
                continue
            if fire[dx][dy] and fire[dx][dy] <= sk[x][y]+1:
                continue
            sk[dx][dy] = sk[x][y] + 1
            sk_q.append((dx, dy))
    print("IMPOSSIBLE")
    return 

T = int(input())

for _ in range(T):
    w, h = map(int, input().split())
    
    fire_q = deque()
    sk_q = deque()
    fire = [[0]*w for _ in range(h)]
    sk = [[0]*w for _ in range(h)]
    building_map = []
    
    for i in range(h):
        building_map.append(list(input()))
        for j in range(w):
            if building_map[i][j] == '*':
                fire_q.append((i, j))
                fire[i][j] = 1
            if building_map[i][j] == '@':
                sk_q.append((i, j))
                sk[i][j] = 1
    fire_bfs()
    sk_bfs()