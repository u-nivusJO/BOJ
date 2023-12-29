card=[i for i in range(1, 21)]
for i in range(10):
    A, B=map(int, input().split())
    changecard=card[A-1:B]
    changecard.reverse()
    card[A-1:B]=changecard
for c in card:
    print(c)



