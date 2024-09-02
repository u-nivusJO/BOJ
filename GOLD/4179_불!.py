from collections import deque

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
    
def fbfs():
    while fq:
        x, y = fq.popleft()
        for s in range(4):
            dx = x + dxs[s]
            dy = y + dys[s]
            if not (0<=dx<R and 0<=dy<C):
                continue
            if miro[dx][dy]=='#' or fire[dx][dy]:
                continue
            fire[dx][dy] = fire[x][y]+1
            fq.append((dx,dy))                

def jbfs():
    while jq:
        x, y = jq.popleft()
        for s in range(4):
            dx = x + dxs[s]
            dy = y + dys[s]
            if not (0<=dx<R and 0<=dy<C):
                print(jihoon[x][y])
                return
            if miro[dx][dy] == '#' or jihoon[dx][dy]:
                continue
            if fire[dx][dy]and jihoon[x][y]+1 >= fire[dx][dy]:
                continue
            jihoon[dx][dy] = jihoon[x][y] + 1
            jq.append((dx,dy))
    print("IMPOSSIBLE")
    return 


R, C = map(int,input().split())
miro = []
fq = deque()
jq = deque()

fire = [[0] * C for _ in range(R)]
jihoon = [[0] * C for _ in range(R)]

for i in range(R):
    miro.append(list(input()))
    for j in range(C):
        if miro[i][j] == "J":
            jq.append((i, j))
            jihoon[i][j]=1
        if miro[i][j] == "F":
            fq.append((i, j))
            fire[i][j] = 1

fbfs()
jbfs()