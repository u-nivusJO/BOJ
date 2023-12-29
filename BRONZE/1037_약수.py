real_divisor_cnt = int(input())
real_divisor = list(map(int, input().split()))

real_divisor.sort()
print(real_divisor[0]*real_divisor[-1])

# print(min(real_divisor)*max(real_divisor)) 