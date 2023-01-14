import sys    
input=sys.stdin.readline
M,N=map(int, input().split())
from collections import defaultdict
universe=defaultdict(int)
for m in range(M):
    planets=list(map(int, input().split()))
    sorted_planet=sorted(list(set(planets)))
    index={sorted_planet[i]:i for i in range(len(sorted_planet))}
    rank=tuple(index[p] for p in planets)
    universe[rank]+=1
answer=0
for v in universe.values():
    answer+=v*(v-1)//2
print(answer)        