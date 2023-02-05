import sys
input=sys.stdin.readline
N=int(input())
answer=[0]*N
people={}
for num in range(N):
    x,y=map(int, input().split())
    people[num]=(x,y)
people=sorted(people.items(), key=lambda x:(-x[1][0],-x[1][1]))
for num, size in enumerate(people):
    rank=1
    x,y=size[1][0],size[1][1]
    for p_num, p_size in people[:num]:
        p_x,p_y=p_size[0],p_size[1]
        if p_x>x and p_y>y:
            rank+=1
    answer[size[0]]=rank
for a in answer:
    print(a, end=' ')   