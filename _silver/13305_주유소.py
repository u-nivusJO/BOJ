import sys
input=sys.stdin.readline
N=int(input())
city=list(map(int,input().split()))
price=list(map(int,input().split()))[:-1]
mprice=min(price)
answer=0
now=0
for n in range(N):
    if price[n]==mprice:
        answer+=sum(city[n:])*mprice
        break
    elif price[now]>price[n]:
        now=n
    answer+=price[now]*city[n]
print(answer)