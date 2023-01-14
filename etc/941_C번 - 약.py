import sys
input=sys.stdin.readline
N=int(input())
a, b=[2], [1]
for i in range(1,N):
    a.append(2*a[i-1]+2*b[i-1])
    b.append(a[i-1]+b[i-1])
print(a[N-1])    
