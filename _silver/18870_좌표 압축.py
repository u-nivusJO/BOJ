import sys
input=sys.stdin.readline
N=int(input())
n_list=list(map(int, input().split()))
n={i:n for i,n in enumerate(n_list)}
n_sort=sorted(n.items(),key=lambda x:x[1])
answer=[-1]*N
for i in range(len(n_sort)):
    num=n_sort[i][0]
    if i==0:
        now=n_sort[i][1]
        cnt=0
        answer[num]=0
    else:
        if now==n_sort[i][1]:
            answer[num]=cnt
        else:
            now=n_sort[i][1]
            cnt+=1
            answer[num]=cnt
for a in answer:
    print(a, end=' ')