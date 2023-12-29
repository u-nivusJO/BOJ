T=int(input())

def VPS(PS):
    stack=[]
    for ps in PS:
        if ps=='(':
            stack.append(ps)
        else:
            if stack:
                stack.pop()
            else:
                return 'NO'          
    if stack:
        return 'NO'
    else:
        return 'YES'                

for _ in range(T):
    PS=input()
    print(VPS(PS))