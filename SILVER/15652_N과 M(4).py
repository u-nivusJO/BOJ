N,M=map(int, input().split())
from itertools import combinations_with_replacement
n=[i for i in range(1, N+1)]
for c in list(combinations_with_replacement(n, M)):
    for cc in c:
        print(cc, end=' ')
    print( )    

# 백트래킹 1
N, M = map(int, input().split())
result = []

def dfs(start):
    if len(result) == M:
        if sorted(result) == result:
            print(*result)
            return
    for i in range(start, N+1):
        if sorted(result) == result:
            result.append(i)
            dfs(start)
            result.pop()
dfs(1)

# 백트래킹 2
N, M = map(int, input().split())
result = []

def dfs(start):
    if len(result) == M:
        print(*result)
        return
    for i in range(start, N+1):
        result.append(i)
        dfs(i)
        result.pop()

dfs(1)