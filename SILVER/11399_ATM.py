import sys 
from itertools import accumulate
input=sys.stdin.readline
N=int(input())
P=list(map(int,input().split()))
P.sort()
answer=sum(accumulate(P))
print(answer)