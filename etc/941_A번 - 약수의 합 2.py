import sys
input=sys.stdin.readline
N=int(input())
cnt=N
for n in range(2,N+1):
    cnt+=n*(N//n)
print(cnt)            
