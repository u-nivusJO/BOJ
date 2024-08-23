from collections import deque
N = int(input())
danji = []
for _ in range(N):
    danji.append(list(input()))

def bfs(x, y):
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    q = deque()
    q.append((x, y))
    danji[x][y] = 0
    max_danji = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + dxs[i]
            dy = y + dys[i]
            if 0<=dx<N and 0<=dy<N and danji[dx][dy]=='1':
                danji[dx][dy] = 0
                max_danji += 1
                q.append((dx, dy))
    return max_danji

result = []
for i in range(N):
    for j in range(N):
        if danji[i][j]=='1':
            result.append(bfs(i, j))

print(len(result))
for r in sorted(result):
    print(r)
