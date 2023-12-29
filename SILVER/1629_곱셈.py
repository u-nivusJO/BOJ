A, B, C = map(int, input().split())

def multi(a, b):
    if b==1:
        return(a%C)
    else:
        temp=multi(a,b//2)
        if b%2==0:
            return(temp*temp%C)
        else:
            return(temp*temp*a%C)    

print(multi(A,B))            