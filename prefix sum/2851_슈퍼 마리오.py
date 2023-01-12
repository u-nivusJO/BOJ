import sys
input=sys.stdin.readline
sum=0
sum_list={}
for i in range(10):
    sum+=int(input())
    sum_list[i]=[sum,abs(100-sum)]
min_abs=sum_list[0][1]
for i,v in sum_list.items():
    if min_abs>=sum_list[i][1]:
        min_abs=sum_list[i][1]
        answer=sum_list[i][0]
print(answer)
