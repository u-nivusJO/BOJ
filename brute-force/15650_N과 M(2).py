N, M =map(int, input().split())
from itertools import combinations
n=[i for i in range(1, N+1)]
for c in list(combinations(n, M)):
    for cc in c:
        print(cc, end=' ')
    print( )    