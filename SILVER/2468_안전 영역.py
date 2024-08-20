from collections import deque
def bfs(N, x, y, hight, area, check_area):
    dxs = [1, 0, -1, 0]
    dys = [0 , 1, 0, -1]
    
    q = deque()
    q.append((x, y))
    check_area[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + dxs[i]
            dy = y + dys[i]
            if 0<=dx<N and 0<=dy<N and area[dx][dy]>hight and check_area[dx][dy]==0:
                q.append((dx, dy))
                check_area[dx][dy] = 1

N = int(input())
area = []
min_hight = 101
max_hight = 0
for _ in range(N):
    row = list(map(int, input().split()))
    min_hight = min(min_hight, min(row))
    max_hight = max(max_hight, max(row))
    area.append(row)

result = [1]
for hight in range(min_hight, max_hight):
    check_area = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if area[i][j]>hight and check_area[i][j]==0:
                cnt += 1
                bfs(N, i, j, hight, area, check_area)
    result.append(cnt)
print(max(result))

