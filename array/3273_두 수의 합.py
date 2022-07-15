n=int(input())
nlist=list(map(int, input().split()))
x=int(input())

check={}
for i in range(1, x):
    check[i]=0
count=0
for n in nlist:
    if 1<=(x-n)<=x-1 and check[(x-n)]==1:
        count+=1
    elif 1<=n<=x-1:
        check[n]+=1

print(count)