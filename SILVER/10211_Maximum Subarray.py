import sys
imput=sys.stdin.readline
T=int(input())
for t in range(T):
    N=int(input())
    nums=list(map(int, input().split()))
    dp=[0]*N
    dp[0]=nums[0]
    for n in range(1,N):
        dp[n]=max(nums[n], dp[n-1]+nums[n])
    print(max(dp))        
