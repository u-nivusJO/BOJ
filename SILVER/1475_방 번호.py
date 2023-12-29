N=int(input())

# 0부터 8까지 0으로 초기화된 딕셔너리 만들기
check={}
for i in range(9):
    check[i]=0

# N의 해당 숫자 카운트(단 9는 6으로 합쳐서 카운트)
for n in str(N):
    if int(n)==9:
        check[6]+=1
    else:
        check[int(n)]+=1

# 6의 개수//2 (홀수의 경우 +1)
if check[6]%2==0:
    check[6]= check[6]//2
else:
    check[6]=check[6]//2+1

# check value 값중 가장 큰 값 출력    
print(max(check.values()))            