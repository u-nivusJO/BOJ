N, M=map(int, input().split())
n=list(map(int, input().split()))
n.sort()
from itertools import combinations_with_replacement
for c in combinations_with_replacement(n ,M):
    for cc in c:
        print(cc, end=' ')
    print( )

# 백트래킹
N, M = map(int, input().split())
raw_numbers = list(map(int, input().split()))
numbers = sorted(raw_numbers)
result = []

def dfs(start):
    if len(result) == M:
        print(*result)
        return
    for i in range(start, N):
        result.append(numbers[i])
        dfs(i)
        result.pop()
dfs(0)