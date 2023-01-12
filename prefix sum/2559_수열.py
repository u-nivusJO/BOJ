import sys
input=sys.stdin.readline
from itertools import accumulate
N, K =map(int, input().split())
nums=[0]+list(map(int, input().split()))
sum_nums=list(accumulate(nums))
first, last = 0,K
sum_k=sum_nums[last]-sum_nums[first]
while last<(N+1):
    sum_k=max(sum_k, sum_nums[last]-sum_nums[first])   
    first+=1
    last+=1
print(sum_k)