import sys
input=sys.stdin.readline
N=int(input())
member={}
for n in range(N):
    member[n]=list(map(str, input().split()))
member=sorted(member.items(),key=lambda x:(int(x[1][0]),x[0]))
for n,mem in member:
    age=int(mem[0])
    name=mem[1]
    print(age, name, sep=' ')