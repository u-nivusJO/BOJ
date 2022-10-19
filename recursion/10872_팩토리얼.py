result = 1
def factorial(n):
    global result
    if n==0:
        result*=1
        return result   
    else:
        result*=n
        factorial(n-1)
        return result

n=int(input())
print(factorial(n))               