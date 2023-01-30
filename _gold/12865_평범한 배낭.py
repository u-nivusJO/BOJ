import sys
input=sys.stdin.readline
N, K = map(int, input().split())
bag={0:0}
for _ in range(N):
    now_w, now_v=map(int, input().split())
    temp={}
    for w, v in bag.items():
        if now_w+w <= K and now_v+v> bag.get(now_w+w,0): # 가방에 넣을 수 있는 무게 & 더한 가치보다 클 때
            temp[now_w+w]=now_v+v 
    bag.update(temp)
print(max(bag.values()))            