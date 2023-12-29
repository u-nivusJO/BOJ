hight=[]
for i in range(9):
    a=int(input())
    hight.append(a)   

for i in range(9):
    for j in range(i+1,9):
        if sum(hight)-(hight[i]+hight[j])==100:
            n1, n2 = hight[i], hight[j]
            hight.remove(n1)
            hight.remove(n2)
            hight.sort()

            for i in hight:
                print(i)
            break
    if len(hight)<9:
        break        
