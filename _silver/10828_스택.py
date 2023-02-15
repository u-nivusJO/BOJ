import sys
input=sys.stdin.readline
N=int(input())
stack=[]
for n in range(N):
    message=list(map(str, input().split()))
    if message[0]=='push':
        stack.append(message[1])
    elif message[0]=='pop':
        if len(stack)==0:
            print(-1)
        else: print(stack.pop())
    elif message[0]=='size':
        print(len(stack))
    elif message[0]=='empty':
        if len(stack)==0:
            print(1)
        else: print(0)
    elif message[0]=='top':
        if len(stack)==0:
            print(-1)
        else: print(stack[-1])