N=int(input())
for i in range(N):
    A, B = input().split()
    A=''.join(sorted(A))
    B=''.join(sorted(B))
    if len(A)==len(B):
        for i in range(len(A)):
            if A[i]!=B[i]:
                answer='Impossible'
                break
            else:
                answer='Possible'
    else:
        answer='Impossible'            
    print(answer)            
