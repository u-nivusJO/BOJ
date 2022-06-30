N, L = map(int, input().split())
n = list(map(int, input().split()))
n.sort()

finish = (n[0] + L -1) 
answer=1

for start in n:
    if start > finish:
        answer += 1
        finish = (start + L -1)  
       
print(answer)
