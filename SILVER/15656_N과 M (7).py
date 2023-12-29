N, M=map(int, input().split())
n=list(map(int, input().split()))
n.sort()
from itertools import product
for p in (product(n, repeat=M)):
    for pp in p:
        print(pp, end=' ')
    print( )    