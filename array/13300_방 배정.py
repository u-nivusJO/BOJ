N, K=map(int, input().split())

# 성별, 학년별로 학생 수 저장할 딕셔너리 만들기
S1={}
S0={}
for s in range(1,7):
    S1[s]=0
    S0[s]=0

# 성별, 학년별로 학생 수 저장
for i in range(N):
    S, Y = map(int, input().split())
    if S == 1:
        S1[Y]+=1
    else:
        S0[Y]+=1    

# 방 개수
count=0

# 남자(0), 여자(1) 구분해서 학년별로 방 배정
for i in range(1,7):
    if S1[i]%K==0:
        count+=S1[i]//K
    else:
        count+=S1[i]//K+1  
    if S0[i]%K==0:
        count+=S0[i]//K
    else:
        count+=S0[i]//K+1
    
print(count)