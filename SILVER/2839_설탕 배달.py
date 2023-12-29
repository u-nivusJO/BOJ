import sys
input=sys.stdin.readline
N=int(input())
answer=0
while N>=0:
    if N%5==0:
        answer+=N//5
        print(answer)
        break
    N-=3
    answer+=1
else:
    print(-1)   
    
    
# 23_12_29
N = int(input())
dp = [-1]*5001
dp[3]=1
dp[4]=-1
dp[5]=1
for i in range(6, N+1):
    if min(dp[i-3],dp[i-5]) == -1:
        if max(dp[i-3],dp[i-5]) == -1:
            dp[i] = -1
        else:
            dp[i] = max(dp[i-3],dp[i-5]) + 1
        
    else:
        dp[i] = min(dp[i-3],dp[i-5]) + 1

print(dp[N])