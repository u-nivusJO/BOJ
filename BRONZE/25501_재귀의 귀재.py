import sys
input=sys.stdin.readline

T=int(input())
for t in range(T):
    S=input()
    cnt=0

    def recursion(S,s,e,cnt):
        if s>=e:
            return 1, cnt
        elif S[s]!=S[e]:
            return 0, cnt
        else:
            return recursion(S,s+1,e-1,cnt+1)       
    def isPalindrome(S):
        return recursion(S,0,len(S)-2,cnt+1)

    answer=isPalindrome(S)
    print(answer[0], answer[1])