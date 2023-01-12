import sys
input=sys.stdin.readline
N, S =map(int,input().split())
nums=list(map(int, input().split()))

right, left =0, 0
sum_s=nums[0]
min_ans=100001

while True:
    if sum_s>=S:
        sum_s-=nums[left]
        min_ans=min(right-left+1, min_ans)
        left+=1
    else:
        right+=1
        if right!=N:
            sum_s+=nums[right]
        else:
            break        
print(min_ans)if min_ans!=100001 else print(0)


