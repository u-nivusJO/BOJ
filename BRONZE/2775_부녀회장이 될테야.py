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
        

# 23_12_31
dp = [[i for i in range(15)]]+[[0 for i in range(15)] for i in range(15)]

for i in range(1, 15):
    for j in range(1, 15):
        for a in range(1, j+1):
            dp[i][j] += dp[i-1][a]
T = int(input())
for t in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n]) 