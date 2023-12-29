X=int(input())
i=1
while True:
    if (i*(i+1))//2>=X:
        break
    i+=1
cnt=X-((i-1)*i)//2
if i%2!=0:
    up, down=i+1,0
    for c in range(cnt):
        up-=1
        down+=1
else:
    up, down=0,i+1
    for c in range(cnt):
        up+=1
        down-=1   
print(up,end='')
print('/',end='')
print(down)         