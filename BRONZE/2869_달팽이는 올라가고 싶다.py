A, B, V=map(int, input().split())
cnt=(V-A)//(A-B)+1
if (V-A)%(A-B)!=0:
    cnt+=1
print(cnt)        