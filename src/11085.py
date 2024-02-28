# 군사 이동

import sys
import heapq
input = sys.stdin.readline

def find(x):
  if g[x] != x:
    return find(g[x])
  return x

def union(a, b):
  a = find(a)
  b = find(b)

  if a < b:
    g[b] = a
  else:
    g[a] = b
  return


p, w = map(int, input().split())
c, v = map(int, input().split())
g = [i for i in range(p + 1)]
pq = []

for _ in range(w):
  s, e, width = map(int, input().split())
  heapq.heappush(pq, (-width, s, e))

while pq:
  cost, start, end = heapq.heappop(pq)
  union(start, end)

  if find(c) == find(v):
    result = -cost
    break

print(result)