arr=[False, False]+[True]*1000000
for i in range(2, (1000000//2)+1):
    if arr[i]==True:
        for j in range(i*2,1000001,i):
            arr[j]=False

while True:
    n=int(input())
    if n==0:
        break
    a=3
    while True:
        b=n-a
        if arr[a]==True and arr[b]==True:
            print(n, '=', a, '+', b)
            break
        else:
            a+=2    
