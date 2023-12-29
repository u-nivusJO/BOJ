N=int(input())
result=[0]*(N+1)

for i in range(2, N+1):
    result[i]=result[i-1]+1
    if i%2==0:
        result[i]=min(result[i], result[i//2]+1)
    if i%3==0:
        result[i]=min(result[i], result[i//3]+1)

print(result[N])


# 23_12_29
N = int(input())
dp = [0]*1000001
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4,N+1):
    if i%6 == 0:
        dp[i]=min(dp[i//3], dp[i//2], dp[i-1])+1
    elif i%2 == 0:
        dp[i]=min(dp[i//2], dp[i-1])+1
    elif i%3 == 0:
        dp[i]=min(dp[i//3], dp[i-1])+1
    else:
        dp[i]=dp[i-1]+1
if N==1:
    print(0)
else:
    print(dp[N])