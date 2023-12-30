import sys
input=sys.stdin.readline

def fibonacci(n):
    zero=[1,0,1]
    one=[0,1,1]
    if n>2: 
        for i in range(3,n+1):
            zero.append(zero[i-1]+zero[i-2])  
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])    

T=int(input())
for _ in range(T):
    N=int(input())
    fibonacci(N)


# 23_12_30
dp={i:[0,0] for i in range(41)}
dp[0]=[1, 0]
dp[1]=[0, 1]
for i in range(2,41):
    dp[i][0], dp[i][1] = dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]

T = int(input())
for t in range(T):
    N = int(input())
    print(dp[N][0], dp[N][1])