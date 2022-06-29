N=int(input())

for i in range(1,N+1):
    A = list(map(int,str(i)))
    if N == i + sum(A):
        print(i)
        break
    if N == i:
        print(0)    
