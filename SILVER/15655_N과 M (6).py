N, M= map(int, input().split())
n=list(map(int, input().split()))
n.sort()
from itertools import combinations
for c in list(combinations(n, M)):
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
    for n in range(start, N):
        if numbers[n] not in result:
            result.append(numbers[n])
            dfs(n)
            result.pop()
dfs(0)