import sys
input=sys.stdin.readline
N=int(input())
paper=[[0]*100 for k in range(100)]
for n in range(N):
    a,b=map(int,input().split())
    for i in range(10):
        for j in range(10):
            paper[a+i][b+j]=1
answer=0
for p in paper:
    answer+=sum(p)
print(answer)
