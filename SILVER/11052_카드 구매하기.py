N = int(input())
P = [0] + list(map(int, input().split()))

dp = [0]*(N+1)
dp[1] = P[1]
dp[2] = max(dp[1]+dp[1], P[2])

for i in range(3, N+1):
    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[i-j]+dp[j])
    dp[i] = max(dp[i], P[i])
print(dp[N])