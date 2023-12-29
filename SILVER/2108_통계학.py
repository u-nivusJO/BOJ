import sys
input=sys.stdin.readline
N=int(input())
num=[]
for n in range(N):
    num.append(int(input()))
num.sort()    
print(round(sum(num)/len(num)))
print(num[len(num)//2])

from collections import Counter
cnt=Counter(num)
common=cnt.most_common(2)
if len(num)>1:
    if common[0][1]==common[1][1]:
        print(common[1][0])
    else:
        print(common[0][0])
else:
    print(common[0][0])        
print(max(num)-min(num))
