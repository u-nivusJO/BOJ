N=int(input())
answer=0
now=1
while True:
    if now>=N:
        break
    answer+=1
    now+=(answer)*6
    
print(answer+1) # 시작과 끝 포함    