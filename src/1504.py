# 특정한 최단 경로
# https://www.acmicpc.net/problem/1504

# 1. 1 -> v1 -> v2 -> n
# 2. 1 -> v2 -> v1 -> n

import sys, heapq

input = sys.stdin.readline

# 입력 받기 & 초기화
n, e = map(int, input().split())
s = [[] for i in range(n + 1)]
INF = sys.maxsize

for i in range(e):
    a, b, c = map(int, input().split())
    s[a].append([b, c])
    s[b].append([a, c])
v1, v2 = map(int, input().split())


# 다익스트라
def dijkstra(start):
    dp = [INF for i in range(n + 1)]
    dp[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        w, c = heapq.heappop(heap)
        for n_n, n_w in s[c]:
            wei = n_w + w
            if dp[n_n] > wei:
                dp[n_n] = wei
                heapq.heappush(heap, [wei, n_n])
    return dp


one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
cnt = min(one[v1] + v1_[v2] + v2_[n], one[v2] + v2_[v1] + v1_[n])
print(cnt if cnt < INF else -1)
