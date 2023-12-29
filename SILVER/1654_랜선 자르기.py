K, N =map(int, input().split())
k_list=[int(input()) for _ in range(K)]
answer=0
start, end = min(k_list)//N, max(k_list)*N

while start<=end:
    mid=(start+end)//2
    can_make=0

    for k in k_list:
        can_make+=k//mid
        if can_make>=N:
            break
    if can_make>=N:
        answer=mid
        start=mid+1
    else:
        end=mid-1  

print(answer)