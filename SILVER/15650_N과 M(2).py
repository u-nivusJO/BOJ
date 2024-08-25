# combinations 이용
N, M =map(int, input().split())
from itertools import combinations
n=[i for i in range(1, N+1)]
for c in list(combinations(n, M)):
    for cc in c:
        print(cc, end=' ')
    print( )    
    
# 백트래킹
N, M = map(int, input().split())
result = []

def dfs(start):
    global result
    if len(result) == M:
        print(' '.join(map(str, result)))
    for i in range(start, N+1):
        if i not in result:
            result.append(i)
            dfs(i)
            result.pop()

dfs(1)