N, M=map(int, input().split())
n=list(map(int, input().split()))
n.sort()
from itertools import combinations_with_replacement
for c in combinations_with_replacement(n ,M):
    for cc in c:
        print(cc, end=' ')
    print( )
