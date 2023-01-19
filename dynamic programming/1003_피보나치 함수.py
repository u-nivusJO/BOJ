import sys
input=sys.stdin.readline

def fibonacci(n):
    zero=[1,0,1]
    one=[0,1,1]
    if n>2: 
        for i in range(3,n+1):
            zero.append(zero[i-1]+zero[i-2])  
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])    

T=int(input())
for _ in range(T):
    N=int(input())
    fibonacci(N)
