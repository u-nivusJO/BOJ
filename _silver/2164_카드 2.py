N=int(input())
from collections import deque
n_list=deque(list(range(1,N+1)))
while n_list:
    if len(n_list)==1:
        print(n_list[0])
        break
    n_list.popleft()
    last=n_list.popleft()
    n_list.append(last)
    