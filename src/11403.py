# 경로 찾기

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

''' 틀린 답 '''
# n = int(input())
# node_list = [list(map(int, input().split())) for _ in range(n)]
# connect = [[] for _ in range(n)]
# answer = [[0] * n for _ in range(n)]

# for i in range(n):
#   for j in range(n):
#     if node_list[i][j] == 1:
#       connect[i].append(j)
#       connect[j].append(i)

# for i in range(n):
#   for j in connect[i]:
#     answer[i][j] = 1

# for i in range(n):
#   if answer[i][i] == 0:
#     for j in connect[i]:
#       if answer[j][i] == 1:
#         answer[i][i] = 1
#         break
# print(answer)

''' DFS '''

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]

def dfs(x):
  for i in range(n):
    if graph[x][i] == 1 and visited[i] == 0:
      visited[i] = 1
      dfs(i)

for i in range(n):
  dfs(i)
  for j in range(n):
    if visited[j] == 1:
      print(1, end=' ')
    else:
      print(0, end=' ')
  print()
  visited = [0 for _ in range(n)]


''' BFS '''

# BFS
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()

        for i in range(n):
            if check[i] == 0 and graph[q][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[x][i] = 1

for i in range(0, n):
    bfs(i)

for i in visited:
    print(*i)
 


# DFS
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]

def dfs(x):
    for i in range(n):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

visited = [0 for _ in range(n)]
for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [0 for _ in range(n)]
 

# 플로이드-와샬 알고리즘을 이용한 풀이
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1
                
for g in graph:
    print(*g)
 