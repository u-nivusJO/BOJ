multi=1
for i in range(3):
    N=int(input())
    multi*=N
check = {}
for i in range(10):
    check[i]=0    
for m in str(multi):
    check[int(m)]+=1
for v in check.values():
    print(v)