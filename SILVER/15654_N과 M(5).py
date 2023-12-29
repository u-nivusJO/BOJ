N, M = map(int, input().split())
n=list(map(int, input().split()))
n.sort()
from itertools import permutations
for p in permutations(n, M):
    for pp in p:
        print(pp, end=' ')
    print( )    