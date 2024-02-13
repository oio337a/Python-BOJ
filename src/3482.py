# Labyrinth

# import sys
# from collections import deque
# from copy import deepcopy
# input = sys.stdin.readline

# def find(c, r):
#   for i in range(r):
#     for j in range(c):
#       if board[i][j] == '.':
#         board[i][j] = 0
#         q.append((i, j, 0))
#         return
  

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# t = int(input())
# for _ in range(t):
#   c, r = map(int, input().split())
#   board = [list(input().rstrip()) for _ in range(r)]
#   temp = deepcopy(board)
#   visited = [[0]*c for _ in range(r)]
#   q = deque()
#   find(c, r)
#   while q:
#     x, y, cnt = q.popleft()
#     visited[x][y] = 1
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if 0 <= nx < c and 0 <= ny < r and not visited[nx][ny] and board[nx][ny] == '.':
#         visited[nx][ny] = 1
#         q.append((nx, ny, cnt + 1))
#         board[nx][ny] = cnt + 1
#   q.append((x, y))
#   temp[x][y] = 0
#   visited = [[0]*c for _ in range(r)]
#   while q:
#     x, y = q.popleft()
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if 0 <= nx < c and 0 <= ny < r and not visited[nx][ny] and temp[nx][ny] == '.':
#         visited[nx][ny] = 1
#         q.append((nx, ny))
#         temp[nx][ny] = temp[x][y] + 1
#   print(f"Maximum rope length is {temp[x][y]}.")

import sys
import copy
from collections import deque
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(start, graph, C, R):
  m = (1, -1, -1)
  q = deque()
  q.append(start)
  graph[start[0]][start[1]] = 1
  while q:
    y, x = q.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if ny >= R or nx >= C or ny < 0 or nx < 0:
        continue
      elif graph[ny][nx] > 0:
        continue
      else:
        graph[ny][nx] = graph[y][x] + 1
        if graph[ny][nx] > m[0]:
          m = (graph[ny][nx], ny, nx)
        q.append((ny, nx))
  return m

T = int(input())
for _ in range(T):
  labyrinth = []
  start = None
  C, R = map(int, input().split())
  for i in range(R):
    lst = []
    t = input().rstrip()
    for j in range(C):
      if t[j] == '#':
        lst.append(1)
      elif t[j] == '.':
        lst.append(0)
        if not start:
          start = (i, j)
    labyrinth.append(lst)

  res1 = bfs(start, copy.deepcopy(labyrinth), C, R)
  res2 = bfs((res1[1], res1[2]), copy.deepcopy(labyrinth), C, R)
  print(f"Maximum rope length is {res2[0] - 1}.")