import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
k = int(input())  # 시작점
dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]


def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        W, now = heapq.heappop(heap)
        # 현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
        if dp[now] < W:
            continue
        for w, next_node in graph[now]:
            # 현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
            # = 다음 노드까지의 가중치(next_wei)
            next_w = W + w
            if next_w < dp[next_node]:
                dp[next_node] = next_w
                heapq.heappush(heap, (next_w, next_node))


for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))  # (가중치, 목적지 노드)

Dijkstra(k)
for i in range(1, V+1):
    print("INF" if dp[i] == INF else dp[i])
