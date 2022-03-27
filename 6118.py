# 숨바꼭질
# https://www.acmicpc.net/problem/6118

import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited):
    queue = deque([1])
    visited[1] = True
    total = [0] * (n+1)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                total[i] = total[v] + 1
                queue.append(i)
                visited[i] = True
    return total

# 1번 헛간에서 가장 먼 헛간 찾기
n, m = map(int, input().split()) # 헛간 개수, 간선의 수
graph = [[] for _ in range(n+1)]

for i in range(m): # 간선 연결
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = bfs(graph, [False] * (n+1))  # bfs 실행

a = result.index(max(result))
b = result[a]
c = result.count(max(result))

print(a,b,c)