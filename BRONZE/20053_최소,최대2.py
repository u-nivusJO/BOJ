# T=int(input())
# data={}
# for t in range(T):
#     N=int(input())
#     data[t]=list(map(int, input().split()))
   
# for j in data.values():
#     minj=min(j)
#     maxj=max(j)
#     print(minj, maxj)

import sys
T=int(sys.stdin.readline().rstrip())
data={}
for t in range(T):
    N=int(sys.stdin.readline().rstrip())
    data[t]=list(map(int, sys.stdin.readline().split()))
   
for j in data.values():
    minj=min(j)
    maxj=max(j)
    print(minj, maxj)