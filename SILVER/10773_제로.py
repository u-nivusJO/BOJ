import sys
input=sys.stdin.readline
K=int(input())
answer=[]
for _ in range(K):
    N=int(input())
    if N==0:
        answer.pop(-1)
    else:
        answer.append(N)
print(sum(answer))            