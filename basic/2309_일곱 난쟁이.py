A=[]
for _ in range(9):
    A.append(int(input()))
for i in range(9):
    for j in range(i+1,9):
        if sum(A)-(A[i]+A[j])==100:
            n1, n2=A[i], A[j]
            A.remove(n1)
            A.remove(n2)
            A.sort()
            for a in A:
                print(a)
            break
    if len(A)==7:
        break    