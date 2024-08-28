N, M =map(int, input().split())
from itertools import product
n=[i for i in range(1, N+1)]
for p in list(product(n, repeat=M)):
    for pp in p:
        print(pp, end=' ')
    print( )     

# 백트래킹 1
N, M = map(int, input().split())
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return
    for n in range(1, N+1):
        result.append(n)
        dfs()
        result.pop()

dfs()