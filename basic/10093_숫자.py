A,B=map(int, input().split())
N1=max(A, B)
N2=min(A, B)
if N1==N2 or N1-1==N2:
    print(0)
else:
    print(N1-N2-1)
    for i in range(N2+1, N1):
        print(i, end=' ')

