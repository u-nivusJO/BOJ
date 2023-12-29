import sys
input=sys.stdin.readline
N, M=map(int, input().split())
site_password={}
for _ in range(N):
    site, password=map(str, input().split())
    site_password[site]=password
for _ in range(M):
    find=input().rstrip()
    print(site_password[find])