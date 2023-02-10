N=int(input())
answer=[]
check=[False,False]+[True]*(N-1)
for i in range(2,N//2+1):
    if check[i]==True:
        for j in range(i*2,N//i+1,i):
            check[j]=False            
t_check=[n for n,t in enumerate(check) if t==True]
while N>=1:
    for i in t_check:
        if N%i==0:
            N=N//i
            answer.append(i)
            break
    if N==1:
        break    
answer.sort()
for a in answer:
    print(a)    