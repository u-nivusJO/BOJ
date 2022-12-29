N, M= map(int, input().split())
n=list(map(int, input().split()))
n.sort()
from itertools import combinations
for c in list(combinations(n, M)):
    for cc in c:
        print(cc, end=' ')
    print( )    