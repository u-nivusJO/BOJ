while True:
    try:
        n=int(input())
    except:
        break  
    x=0
    cnt=1
    while True:
        x=x*10+1
        if x%n==0:
            print(cnt)
            break
        cnt+=1