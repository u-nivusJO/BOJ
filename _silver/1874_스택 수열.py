n = int(input())

stack = []
result = []
stack.append(0)
element = 1
printFlag = True
for _ in range(n):
    target = int(input())
    
    while target != stack[-1]:
        if target > stack[-1]:
            stack.append(element)
            element += 1
            result.append('+')
        elif target < stack[-1]:
            if target < element: 
                print('NO')
                printFlag = False
                quit()
            stack.pop()
            result.append('-')
    stack.pop()
    result.append('-')


if printFlag :
    for i in result:
        print(i)