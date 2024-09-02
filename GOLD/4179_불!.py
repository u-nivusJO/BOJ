from collections import deque
R, C = map(int,input().split())
miro = []
for _ in range(R):
    miro.append(list(input()))

miro_jh = [[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if miro[i][j]=="J":
            miro[i][j]='.'
            miro_jh[i][j]=1
            Jh_i, jh_j = (i,j)
            break

def bfs1(x, y):
    q = deque()
    q.append((x,y))
    miro[x][y]=1
    dxs=[1,-1,0,0]
    dys=[0,0,1,-1]
    while q:
        x,y=q.popleft()
        for s in range(4):
            dx = x+dxs[s]
            dy = y+dys[s]
            if 0<=dx<R and 0<=dy<C and miro[dx][dy]=='.':
                miro[dx][dy]=miro[x][y]+1
                q.append((dx,dy))
                

def bfs2(x, y):
    q = deque()
    q.append((x,y))
    dxs=[1,-1,0,0]
    dys=[0,0,1,-1]
    while q:
        x,y=q.popleft()
        for s in range(4):
            dx = x+dxs[s]
            dy = y+dys[s]
            if 0<=dx<R and 0<=dy<C:
                if miro[dx][dy] == '.':
                    miro_jh[dx][dy]=miro_jh[x][y]+1
                    q.append((dx,dy))
                elif miro[dx][dy] != '#' and (miro_jh[x][y]+1)<miro[dx][dy]:
                    miro_jh[dx][dy]=miro_jh[x][y]+1
                    q.append((dx,dy))
                if 0==dx or dx==(R-1) or 0==dy or dy==(C-1):
                    return miro_jh[dx][dy]
            

for i in range(R):
    for j in range(C):
        if miro[i][j]=="F":
            bfs1(i, j)

result = bfs2(Jh_i, jh_j) 
print(result)
print(miro_jh)
         
if result:
    print(result)
else:
    print('IMPOSSIBLE')