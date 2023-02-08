import sys
input=sys.stdin.readline
T=int(input()) # test 개수
for t in range(T):
    H,W,N=map(int, input().split()) # 층 수, 방 수, 몇 번째 손님
    if N%H==0:
        x=H*100
        y=N//H
    else:
        x=(N%H)*100
        y=N//H+1
    print(x+y)    