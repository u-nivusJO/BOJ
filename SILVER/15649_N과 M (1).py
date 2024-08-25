# permutations 이용
N, M = map(int, input().split())

from itertools import permutations
n = [i for i in range(1, N+1)]
for p in permutations(n, M):
    for pp in p:
        print(pp, end=' ')
    print()     
    
# 백트래킹
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result =[]

def backtracking():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            backtracking()
            result.pop()
            
backtracking()