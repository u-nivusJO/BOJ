def prime(num):
    if num==1:
        return False
    else:
        for n in range(2, int(num**(1/2))+1):
            if num%n==0:
                return False
        return True        

M, N=map(int, input().split())
for i in range(M, N+1):
    if prime(i):
        print(i)
    