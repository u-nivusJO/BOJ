import sys, heapq
input=sys.stdin.readline
N=int(input())
left, right=[], []
mid=int(input())
print(mid)
for i in range(N-1):
    n=int(input())
    if n>mid:
        heapq.heappush(right,n)
        if len(left)+1<len(right):
            heapq.heappush(left,(-mid,mid))
            mid=heapq.heappop(right)
    else:    
        heapq.heappush(left, (-n,n))
        if len(right)<len(left):
            heapq.heappush(right,mid)
            mid=heapq.heappop(left)[1]               
    print(mid)        
