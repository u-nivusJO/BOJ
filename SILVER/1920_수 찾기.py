import sys
input=sys.stdin.readline
N=int(input())
n=set(map(int, input().split()))
M=int(input())
m=list(map(int, input().split()))
for i in m:
    if i in n:
        print(1)
    else:
        print(0)    
