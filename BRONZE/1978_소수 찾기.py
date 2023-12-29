N = int(input())
num = list(map(int, input().split()))
cnt=0

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1     
                
for n in num:
    if n==2:
        cnt+=1
    elif n>2:
        cnt+=prime(n)   
print(cnt)