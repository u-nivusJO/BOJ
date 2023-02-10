import sys
input=sys.stdin.readline
N=int(input())
answer=[]
for n in range(N):
    answer.append(list(map(int, input().split())))
answer.sort(key=lambda x:(x[1],x[0]))
for a, b in answer:
    print(a,b, sep=' ')    