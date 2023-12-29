import sys
input=sys.stdin.readline

def finehight(trees,start,end):
    hight=0
    while start<=end:
        mid=(start+end)//2
        totalcut=0

        for tree in trees:
            if tree > mid:
                totalcut += tree-mid

        if M <= totalcut:
            start = mid+1
            hight = mid
        else:
            end = mid-1

    return hight

N,M=map(int, input().split())
trees = list(map(int, input().split()))
print(finehight(trees,0,max(trees)))