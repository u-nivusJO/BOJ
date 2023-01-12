import sys
input=sys.stdin.readline
from itertools import accumulate
N,M=map(int,input().split())
array={0:[0]*(M+1)}
for n in range(1, N+1):
    array[n]=list(map(int, input().split()))
    array[n]=[0]+list(accumulate(array[n]))
    for m in range(1, M+1):
        array[n][m]+=array[n-1][m]
K=int(input())
for k in range(K):
    x1, y1, x2, y2= map(int, input().split())
    answer=array[x2][y2]-array[x1-1][y2]-array[x2][y1-1]+array[x1-1][y1-1]
    print(answer)