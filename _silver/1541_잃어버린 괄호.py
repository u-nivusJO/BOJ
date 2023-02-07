input=input().split('-')
for i in range(len(input)):
    temp=input[i].split('+')
    temp_answer=0
    for t in temp:
        temp_answer+=int(t)
    if i==0:
        answer=temp_answer
    else:    
        answer-=temp_answer
print(answer)        