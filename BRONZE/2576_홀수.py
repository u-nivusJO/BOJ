result=0
minnum=100

for _ in range(7):
    A=int(input())
    if A%2!=0:
        result+=A
        minnum=min(minnum, A)

if result==0:
    print(-1)
else:
    print(result)
    print(minnum)

