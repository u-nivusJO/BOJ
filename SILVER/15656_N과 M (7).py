'''N, M=map(int, input().split())
n=list(map(int, input().split()))
n.sort()
from itertools import product
for p in (product(n, repeat=M)):
    for pp in p:
        print(pp, end=' ')
    print( ) '''

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
        result.append(n)
        dfs()
        result.pop()
dfs()