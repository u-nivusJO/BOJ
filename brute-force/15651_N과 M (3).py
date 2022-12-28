N, M =map(int, input().split())
from itertools import product
n=[i for i in range(1, N+1)]
for p in list(product(n, repeat=M)):
    for pp in p:
        print(pp, end=' ')
    print( )     