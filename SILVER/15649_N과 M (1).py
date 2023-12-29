N, M =map(int, input().split())

from itertools import permutations
n=[i for i in range(1, N+1)]
for p in permutations(n, M):
    for pp in p:
        print(pp, end=' ')
    print()     