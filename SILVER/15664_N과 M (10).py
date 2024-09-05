N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [0]*N
result = []

def backtracking(start):
    check = 0
    if len(result) == M:
        print(*result)
        return
    for i in range(start, N):
        if check != numbers[i] and visited[i]==0:
            result.append(numbers[i])
            check = numbers[i]
            visited[i] = 1
            backtracking(i)
            result.pop()
            visited[i] = 0

backtracking(0)