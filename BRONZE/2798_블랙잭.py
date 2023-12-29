import sys
input=sys.stdin.readline
N, M=map(int, input().split())
n=list(map(int, input().split()))

from itertools import combinations        
com_n=list(combinations(n,3))
check=0
for c in com_n:
    if sum(c)==M:
        check=M
        break
    elif sum(c)<M:
        check=max(check,sum(c))
print(check)        