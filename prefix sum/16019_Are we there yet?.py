from itertools import accumulate
citys=list(map(int, input().split()))
for i in range(len(citys)+1):
    standard_city=citys[:i]
    standard_city.reverse()
    distance=list(accumulate(standard_city))
    distance=sorted(distance, reverse=True)
    for d in distance:
        print(d, end=' ')   
    standard_city=citys[i:]
    distance=accumulate(standard_city, initial=0)
    for d in distance:
        print(d, end=' ')
    print()

# l=[0]+list(map(int,input().split()))
# for i in range(1,5):
#     l[i]+=l[i-1] # 누적 합
#     print(l)
# for i in range(5):
#     for j in range(5):
#         print(abs(l[i]-l[j]),end=' ')
#     print()