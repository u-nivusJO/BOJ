N,M=map(int, input().split())
from itertools import combinations_with_replacement
n=[i for i in range(1, N+1)]
for c in list(combinations_with_replacement(n, M)):
    for cc in c:
        print(cc, end=' ')
    print( )    
