import sys
input=sys.stdin.readline
N = int(input())
a = sorted(list(map(int, input().split())))
M = int(input())
b = list(map(int, input().split()))

from collections import Counter
count_n=Counter(a)
for target in b:
    if target in count_n:
        print(count_n[target], end=' ')
    else: print(0, end=' ')

# cnt = {}
# for i in a:
#     if i in cnt:
#         cnt[i] += 1
#     else:
#         cnt[i] = 1

# for i in b:
#     if i in cnt:
#         print(cnt[i], end=' ')
#     else:
#         print(0, end=' ')