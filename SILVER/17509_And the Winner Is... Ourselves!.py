Dlist=[]
nzeroV=[]
penalty=0
count=0

for i in range(11):
    D, V = map(int, input().split())
    Dlist.append(D)
    if V != 0:
        nzeroV.append(V)    

Dlist.sort()
for D in Dlist:
    count += D
    penalty += count

penalty += sum(nzeroV)*20

print(penalty)
