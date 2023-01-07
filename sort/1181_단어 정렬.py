N=int(input())
words=[input() for _ in range(N)]
words=list(set(words))
words_sort=[]
for word in words:
    words_sort.append((len(word),word))

answer=sorted(words_sort)
for a in answer:
    print(a[1])