# Q4

def func4(N):
    i=0
    while True:
        K=2**(i)
        if K<N:
            answer=K
            i+=1
        else:
            return answer    

N=int(input())
print(func4(N))
        