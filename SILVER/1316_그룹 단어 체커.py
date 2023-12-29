N = int(input())
result = 0

for i in range(N):
    word=input()
    alphabet=[word[0]]
    for i in range(1, len(word)):
        if word[i] != word[i-1]:
            alphabet.append(word[i])
    if len(set(alphabet)) == len(alphabet):
        result +=1       
print(result)