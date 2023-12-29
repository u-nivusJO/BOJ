import sys
N = int(sys.stdin.readline())
a=[]
for i in range(N):
    n = int(sys.stdin.readline())
    a.append(n)
a.sort()    
for i in a:
    print(i)