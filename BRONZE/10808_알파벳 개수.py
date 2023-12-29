from string import ascii_lowercase

s=input()
alpha={}
for i in ascii_lowercase:
    alpha[i]=0
for i in s:
    alpha[i]+=1
for i in alpha.values():
    print(i, end=' ')        