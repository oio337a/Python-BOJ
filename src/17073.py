# 나무 위의 빗물
# https://www.acmicpc.net/problem/17073

"""
  1
2   3
  4   5
"""

import sys
input = sys.stdin.readline
#
# def dfs(visited, n, w):
#     stack = [n]
#     visited[n] = True
#
#     while stack:
#         start = stack.pop()
#         water = w[start]
#
#         count = 0
#         for v in graph[start]:
#             if not visited[v]:
#                 count += 1
#         if count == 0:
#             continue
#         val = water / count
#         w[start] = 0
#
#         for v in graph[start]:
#             if not visited[v]:
#                 stack.append(v)
#                 visited[v] = True
#                 w[v] += val
#
# n, w = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# water = [0]
#
# for i in range(1, n + 1):
#     if i == 1:
#         water.append(w)
#     else:
#         water.append(0)
#
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [False] * (n + 1)
# dfs(visited, 1, water)
#
# result, count = 0, 0
# for w in water:
#     if w != 0:
#         result += w
#         count += 1
# print(round(result / count, 10))



n, w = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(2, n + 1):
    if len(graph[i]) == 1:
        cnt += 1
print(round(w / cnt, 10))