import sys
imput=sys.stdin.readline
N=int(input())
time={}
answer=0
for n in range(N):
    s,e=map(int,input().split())
    time[s]=time.get(s,[])+[e]
sort_time=sorted(time.items(), key=lambda x:(min(x[1]),x[0]))
end_time=-1
for s,e in sort_time:
    if end_time<=s:
        if s in e:
            answer+=e.count(s)
            new_e=[i for i in e if i!=s]
            if new_e:
                answer+=1
                end_time=min(new_e)
            else:
                end_time=e[0]
        else:
            answer+=1
            end_time=min(e)
print(answer)            