import sys
input=sys.stdin.readline
N,M=map(int,input().split())
answer=[]
board=[]
for _ in range(N):
    board.append(input()[:-1])
for i in range(N-7):
    for j in range(M-7):
        w_cnt,b_cnt=0,0
        for n in range(i,i+8):
            for m in range(j,j+8):
                if (n+m)%2==0:
                    if board[n][m]!='W': # 화이트로 시작하는 경우-짝수칸은 화이트
                        w_cnt+=1
                    else:
                        b_cnt+=1    # 블랙으로 시작하는 경우-짝수칸은 블랙
                else:
                    if board[n][m]!='W': # 화이트로 시작하는 경우-홀수칸은 블랙
                        b_cnt+=1
                    else:
                        w_cnt+=1    # 블랙으로 시작하는 경우-홀수칸은 화이트    
        answer.append(min(w_cnt,b_cnt))
print(min(answer))            