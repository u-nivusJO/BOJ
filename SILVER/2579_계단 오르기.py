N = int(input())
points = [0] + [int(input()) for _ in range(N)]
dp = [0]*301

if N == 1:
    dp[1] = points[1]
elif N == 2:
    dp[1] = points[1]
    dp[2] = dp[1] + points[2]
else:
    dp[1] = points[1]
    dp[2] = dp[1] + points[2]
    dp[3] = max(dp[1]+points[3], points[2]+points[3])
    for n in range(4, N+1):
        dp[n] = max(dp[n-2]+points[n], dp[n-3]+points[n-1]+points[n])

print(dp[N])