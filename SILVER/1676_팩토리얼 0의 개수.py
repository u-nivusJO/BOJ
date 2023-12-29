N=int(input())
num=1
cnt=0
for i in range(1,N+1):
    num*=i
for n in str(num)[::-1]:
    if n!='0':
        break
    else:
        cnt+=1
print(cnt)        