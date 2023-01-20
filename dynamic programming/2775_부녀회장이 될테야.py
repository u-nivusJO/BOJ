import sys
input=sys.stdin.readline
from itertools import accumulate
T=int(input())

for _ in range(T):
    k=int(input())
    n=int(input())
    if k==0:
        print(n)
    else:
        people=[p for p in range(1,n+1)]    
        for _ in range(k):
            people=list(accumulate(people))
        print(people[-1])        