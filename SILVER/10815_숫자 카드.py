import sys
input=sys.stdin.readline
N=int(input())
card=list(map(int, input().split()))
M=int(input())
have=list(map(int, input().split()))

from collections import Counter
c_card=Counter(card)
for have_card in have:
    if c_card[have_card]:
        print(1, end=' ')
    else:
        print(0, end=' ')    