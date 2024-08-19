from collections import deque

def bfs():
    dxs = [1, 2, 2, 1, -1, -2, -2, -1]
    dys = [2, 1, -1, -2, -2, -1, 1, 2]
    
    q = deque()
    q.append((start_x, start_y))
    while q:
        x, y = q.popleft()
        for i in range(8):
            dx = x + dxs[i]
            dy = y + dys[i]
            if 0<=dx<l and 0<=dy<l and chess[dx][dy]==0:
                chess[dx][dy] = chess[x][y]+1
                q.append((dx, dy))
            if dx==final_x and dy==final_y:
                return chess[dx][dy]

N = int(input())
for _ in range(N):
    l = int(input())
    chess = [[0]*l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    final_x, final_y = map(int, input().split())
    if start_x == final_x and start_y == final_y:
        print(0)
    else:
        print(bfs())