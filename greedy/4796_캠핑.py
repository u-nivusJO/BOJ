day={}
i=1

while True:    
    L, P, V = map(int, input().split())
    if L + P + V == 0:
        break
    day[i]=[L, P, V]
    i += 1
    
for key in day:
    answer=0
    L=day[key][0]
    P=day[key][1]
    V=day[key][2]
    answer+=(V//P)*L
    answer+=min(L,V%P)
    print(f'Case {key}: {answer}')



i = 0

while True:    
    L, P, V = map(int, input().split())
    if L + P + V == 0:
        break
    answer=0
    i += 1
    answer+=(V//P)*L
    answer+=min(L,V%P)
    print(f'Case {i}: {answer}')
