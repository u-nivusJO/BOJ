import sys
input=sys.stdin.readline
N, M=map(int, input().split())
S=[]
for _ in range(N):
    S.append(input())

from collections import Counter
counter_S=Counter(S)    

answer=0
for _ in range(M):
    test=input()
    if counter_S[test]:
        answer+=1
print(answer)