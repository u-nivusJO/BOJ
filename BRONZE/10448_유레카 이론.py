T = int(input())
K = [int(input()) for k in range(T)]
Tn=[]
Eureka=[]

for n in range(1, 1001):
    if (n*(n+1)/2)>=1000:
        break
    else:
        Tn.append(n*(n+1)/2)

for one in Tn:
    for two in Tn:
        for three in Tn:
            if (one + two + three) > 1000:
                break
            else:
                Eureka.append(one + two + three)


for k in K:
    if k in Eureka:
        print(1)
    else:
        print(0)    
