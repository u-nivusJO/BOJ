N = int(input())
# 제일 큰 자릿수 처리
i=len(str(N)) # 자릿수
if i==1:
    answer=N
else:
    answer=(N-((10**(i-1))-1))*i
    answer+=9
    for i in range(2,i):
        answer+=(((10**i)-1)-(10**(i-1))+1)*i
print(answer)    