import sys
from itertools import accumulate
input=sys.stdin.readline
N, M =map(int, input().split())
nums=[0]+list(map(int, input().split()))
sum_nums=list(accumulate(nums))
for _ in range(M):
    i, j =map(int, input().split())
    print(sum_nums[j]-sum_nums[i-1])