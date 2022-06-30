N, K = map(int, input().split())
Alist = []
for i in range(N):
    Alist.append(int(input()))
Alist.sort(reverse=True)

answer=0
for A in Alist:
    if K >= A:
        answer += K//A
        K = K%A

print(answer)