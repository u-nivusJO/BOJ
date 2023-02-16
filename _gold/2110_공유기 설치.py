import sys
input=sys.stdin.readline
N, C=map(int, input().split())
x_list=[]
for n in range(N):
    x_list.append(int(input()))
x_list.sort()    
start,end=0, x_list[-1]-x_list[0]
answer=0
while start<=end:
    mid=(start+end)//2
    install_x=1
    now_x=x_list[0]
    for i in range(1, len(x_list)):
        x=x_list[i]
        if x-now_x>=mid:
            install_x+=1
            now_x=x_list[i]
    if install_x<C:
        end=mid-1
    else:
        answer=mid
        start=mid+1 
print(answer)