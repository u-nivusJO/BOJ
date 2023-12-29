import sys
input=sys.stdin.readline
M=int(input())
N=int(input())
pre=[False,False]+[True]*N
for i in range(2, N//2+1):
    if pre[i]==True:
        for j in range(2,N//i+1):
            if pre[i*j]==True:
                pre[i*j]=False
answer=0
min_num=10001
for check in range(M,N+1):
    if pre[check]==True:
        answer+=check
        min_num=min(min_num,check)
if answer==0:
    print(-1)
else:
    print(answer)
    print(min_num)    