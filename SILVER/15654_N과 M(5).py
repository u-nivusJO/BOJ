N, M = map(int, input().split())
n=list(map(int, input().split()))
n.sort()
from itertools import permutations
for p in permutations(n, M):
    for pp in p:
        print(pp, end=' ')
    print( )

# 백트래킹
N, M = map(int, input().split())
raw_numbers = list(map(int, input().split()))
numbers = sorted(raw_numbers)
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return
    for n in numbers:
        if n not in result:
            result.append(n)
            dfs()
            result.pop()

dfs()