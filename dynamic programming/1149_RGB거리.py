import sys
input=sys.stdin.readline
N=int(input())
rgb=[]
for i in range(N):
    rgb.append(list(map(int, input().split())))
for n in range(1,N):
    rgb[n][0]+=min(rgb[n-1][1], rgb[n-1][2])
    rgb[n][1]+=min(rgb[n-1][0], rgb[n-1][2])
    rgb[n][2]+=min(rgb[n-1][0], rgb[n-1][1])
print(min(rgb[N-1]))