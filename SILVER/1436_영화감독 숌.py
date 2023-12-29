N=int(input())
check=[]
cnt=0
while True:
    cnt+=1
    if '666' in str(cnt):
        N-=1
    if N==0: break
print(cnt)    