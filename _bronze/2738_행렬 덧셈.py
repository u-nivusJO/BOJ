import sys
input=sys.stdin.readline
N,M=map(int, input().split())
a,b=[],[]
for _ in range(N):
    i=list(map(int,input().split()))
    a.append(i)
for n in range(N):
    i=list(map(int,input().split()))
    b.append(i)
for n in range(N):
    for m in range(M):
        print(a[n][m]+b[n][m], end=' ')
    print()          