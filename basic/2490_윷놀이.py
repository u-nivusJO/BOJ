for _ in range(3):
    K = list(map(int, input().split()))
    result={'A':1, 'B':2, 'C':3, 'D':4, 'E':0}
    count0=0
    for k in K:
        if k==0:
            count0+=1
    for i,j in result.items():
        if j==count0:
            print(i)    


