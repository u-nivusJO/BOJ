N=int(input())
if N%400==0:
    answer=1
elif N%4==0 and N%100!=0:
    answer=1
else:
    answer=0
print(answer)