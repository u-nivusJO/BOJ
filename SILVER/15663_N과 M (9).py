N, M = map(int, input().split())
raw_numbers = list(map(int, input().split()))
numbers = sorted(raw_numbers)
visited = [0]*N
result = []

def backtracking():
    check = 0
    if len(result) == M:
        print(*result)
        return
    for i in range(N):
        if visited[i] == 0 and check != numbers[i]:
            result.append(numbers[i])
            visited[i] = 1
            check = numbers[i]
            backtracking()
            result.pop()
            visited[i] = 0

backtracking()