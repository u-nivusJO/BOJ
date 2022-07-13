# Q2

def func2(arr,N):
    for a in range(N):
        for b in range(a+1, N):
            if arr[a]+arr[b]==100:
                return 1
    return 0

N=int(input())                
arr=list(map(int, input().split()))
print(func2(arr,N))