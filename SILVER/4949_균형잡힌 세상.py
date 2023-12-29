import sys
input=sys.stdin.readline
def check(x):
    stack=[]
    for xx in x:
        if xx=='(' or xx=='[':
            stack.append(xx)
        elif xx==')':
            if stack and stack[-1]=='(':    
                    stack.pop()
            else:
                return'no'        
        elif xx==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                return 'no'    
    if stack:
        return 'no'            
    return 'yes'

while True:
    x=input().rstrip()
    if x=='.':
        break
    elif x[-1]!='.':
        print('no')
    else:
        print(check(x))