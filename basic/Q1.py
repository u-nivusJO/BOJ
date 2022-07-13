# Q1

def func1(N):
    answer=0
    for n in range(1,N+1):
        if n%3==0 or n%5==0:
            answer+=n
    return answer

N=int(input())
print(func1(N))



   