import sys
from itertools import accumulate
input=sys.stdin.readline
N,M=map(int, input().split())
graph={}
sum_graph={0:[0]*(N+1)}

for row in range(N):
    graph[row+1]=[0]+list(map(int, input().split()))
    sum_graph[row+1]=list(accumulate(graph[row+1]))
    for y in range(1, N+1):
        sum_graph[row+1][y]+=sum_graph[row][y] 
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer=sum_graph[x2][y2]-sum_graph[(x1-1)][y2]-sum_graph[x2][(y1-1)]+sum_graph[(x1-1)][(y1-1)]
    print(answer)    
        