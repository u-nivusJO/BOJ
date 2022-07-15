N=int(input())
nlist=list(map(int, input().split()))
v=int(input())

count=0
for n in nlist:
    if n==v:
        count+=1
print(count)        
