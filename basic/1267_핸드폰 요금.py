N=int(input())
calltime=list(map(int, input().split()))
Yprice, Mprice= 0, 0

for call in calltime:
    Yprice+=(call//30)*10+10   
    Mprice+=(call//60)*15+15

if Yprice==Mprice:
    print('Y M', Yprice)
elif min(Yprice, Mprice)==Yprice:
    print('Y', Yprice)
else:     
    print('M', Mprice)
