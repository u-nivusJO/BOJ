import sys
input=sys.stdin.readline
while True:
    word=int(input())
    if word==0:
        break
    else:
        word=str(word)
        if len(word)%2==0:
            last=len(word)//2
        else: last=len(word)//2+1    
        if (word[:last])[::-1]==word[len(word)//2:]:
            print('yes')
        else:
            print('no')