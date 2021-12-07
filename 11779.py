import sys
import heapq
input = sys.stdin.readline

'''입력 받기'''
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    fr, to, cost = map(int, input().split())
    graph[fr].append((to, cost))  # 노드 연결

FROM, TO = map(int, input().split())

'''변수 설정'''
distance = [float('inf') for _ in range(n+1)]  # 거리
path = [[] for _ in range(n+1)]  # 경로를 담을 배열
path[FROM].append(FROM)  # 시작위치 저장
q = [(0, FROM)]  # 다익스트라 큐
heapq.heapify(q)

'''다익스트라'''

while q:
    now_cost, now = heapq.heappop(q)
    if now_cost > distance[now]:
        continue
    if now == FROM:
        distance[now] = 0
    for next, next_cost in graph[now]:
        path_cost = next_cost + now_cost
        if path_cost < distance[next]:
            distance[next] = path_cost
            heapq.heappush(q, (path_cost, next))
            # path 가 갱신됐을 때 현재까지의 경로를 넣어준다.
            path[next] = []
            for p in path[now]:
                path[next].append(p)
            path[next].append(next)
print(distance[TO])
print(len(path[TO]))
print(' '.join(map(str, path[TO])))
