a = input()
b = input()
cnt=0
a_len=len(a)
b_len=len(b)
for i in range(len(a)):
    if a[i] in b:
        b=b.replace(a[i],'',1)
        cnt+=1

print(a_len+b_len-cnt*2)