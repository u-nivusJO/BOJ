import sys
input=sys.stdin.readline
k=123456*2
check=[False,False]+[True]*k
for i in range(2,int(k**0.5)+1):
    if check[i]==True:
        for j in range(i*2,k+1,i):
            check[j]=False 
while True:
    N=int(input())
    if N==0:
        break
    else:
        answer=0
        for i in range(N+1, 2*N+1):
            if check[i]==True:
                answer+=1
        print(answer)        
         
        