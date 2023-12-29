arr=[False, False] + [True]*9999
for i in range(2,5001):
    if arr[i]==True:
        for j in range(i*2,10001,i):
            arr[j]=False       

T=int(input())
for t in range(T):
    n=int(input())

    a=n//2
    b=n//2
    while True: 
        if arr[a] and arr[b]==True:
            print(a, b)
            break
        else:
            a-=1
            b+=1    

