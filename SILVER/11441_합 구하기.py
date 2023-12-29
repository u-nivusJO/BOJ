import sys
input=sys.stdin.readline
from itertools import accumulate
N=int(input())
nums=list(map(int, input().split()))
nums_sum=[0]+list(accumulate(nums))
M=int(input())
for m in range(M):
    i, j=map(int, input().split())
    answer=nums_sum[j]-nums_sum[i-1]
    print(answer)