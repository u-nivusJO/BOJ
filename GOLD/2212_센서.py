N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

dist = [sensor[i] - sensor[i-1] for i in range(1, N)]
dist.sort(reverse=True)
print(sum(dist[K-1:]))