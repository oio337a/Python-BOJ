import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]


def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)


for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))

# def bfs(x, mode):
#     q = deque
#     q.append(x)
#     c = [-1 for _ in range(n)]
#     c[x] = 0
#     while q:
#         x = q.popleft()
#         for x, nx in a[x]:
#             if c[nx] == -1:
#                 c[nx] = c[x] + w
#                 q.append(nx)
#     if mode == 1:
#         return c.index(max(c))
#     else:
#         return max(c)


# node = int(input())
# a = [[] for _ in range(node)]

# for _ in range(node-1):
#     x, y, w = map(int, input().split())
#     a[x-1].append([w, y-1])  # 가중치, 자식노드 저장
#     a[y-1].append([w, x-1])  # 가중치, 부모노드 저장
# print(bfs(bfs(0, 1), 2))
