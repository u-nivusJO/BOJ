# Q2

def func2(arr, N):
    check=[i for i in range(0,101)]
    for i in arr:
        if check[i]==1:
            return 1
        else:
            check[i]=1
    return 0            

arr=list(map(int, input().split()))
N=int(input())
print(func2(arr, N))   
