n=int(input())
def pi(n):
    if n<=1:
        return n
    return pi(n-2)+pi(n-1)
print(pi(n))    