n=int(input())
cnt=0

if n==1 or n==3:
    cnt=-1
elif (n%5)%2==0:
    cnt = (n // 5) + (n % 5) // 2
else:
    cnt= (n//5-1)+(n-((n//5-1)*5))//2
print(cnt)


# five_cnt=(n // 5)
# if n < 5 and n%2!=0:
#     cnt = -1
# else:
#     if n%5==0:
#         cnt=five_cnt
#     elif (n%2==0 and five_cnt % 2 == 0) or (n%2!=0 and five_cnt % 2 != 0):
#             cnt += five_cnt
#             cnt += (n - ((five_cnt) * 5)) // 2
#     else:
#             cnt += five_cnt - 1
#             cnt += (n - ((five_cnt - 1) * 5)) // 2
