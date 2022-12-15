N, K =map(int, input().split())
cnt=0
arr=[False, False] + [True]*(N)
for i in range(2, N+1):
    if arr[i]==True:
        for j in range(i,N+1,i):
            if arr[j]==True:
                arr[j]=False
                cnt+=1    
                if cnt==K:
                    print(j)
                    break    
