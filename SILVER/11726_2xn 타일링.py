n = int(input())
dp = [0]*1001
dp[1]=1
dp[2]=2
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n]%10007)

# 24_09_06
n = int(input())
dp = [0]*1001
dp[1] = 1
dp[2] = 2

for n in range(3, n+1):
    dp[n] = dp[n-1]+dp[n-2]

print(dp[n]%10007)