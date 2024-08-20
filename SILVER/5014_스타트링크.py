from collections import deque
F, S, G, U, D = map(int, input().split())
elevator = [0]*(F+1)
elevator[G] == '*'

def bfs():
    q = deque()
    q.append(S)
    elevator[S] = 1
    
    while q:
        N = q.popleft()
        if N == G:
            return elevator[N]-1
        for move in (U, -D):
            if 1<=(N+move)<=F and elevator[N+move]==0:
                elevator[N+move] = elevator[N]+1
                q.append(N+move)
    return "use the stairs"
if S == G:
    print(0)
else:
    print(bfs())