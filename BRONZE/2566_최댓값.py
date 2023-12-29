import sys
input=sys.stdin.readline
num=-1
for n in range(1,10):
    row=list(map(int,input().split()))
    if max(max(row), num)!=num:
        num=max(row)
        r_num=n
        c_num=row.index(max(row))+1
print(num)
print(r_num, c_num)        
