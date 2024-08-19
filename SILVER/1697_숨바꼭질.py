from collections import deque
N, K = map(int, input().split())
max = 10**5 # N, K의 최댓값
line = [0] * (max+1)

def bfs(N):
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x==K:
            print(line[x])
            break
        for dx in (x-1, x+1, 2*x):
            if 0<=dx<=max and not line[dx]:
                line[dx] = line[x]+1
                q.append(dx)
bfs(N)