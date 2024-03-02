# 방 청소

import sys
input = sys.stdin.readline

def find(a):
  if a == disjoinSet[a]:
    return a
  
  disjoinSet[a] = find(disjoinSet[a])
  return disjoinSet[a]

def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    if maxSize[a] < maxSize[b]:
      a, b = b, a
    disjoinSet[b] = a
    maxSize[a] += maxSize[b]
    nowSize[a] += nowSize[b]
    maxSize[b] = 0
    nowSize[b] = 0
  
  
n, m = map(int, input().split())
disjoinSet = [i for i in range(m + 1)]
maxSize = [1 for _ in range(m+1)]
nowSize = [0 for _ in range(m+1)]

for i in range(n):
  a, b = map(int, input().split())
  union(a, b)
  if nowSize[find(a)] < maxSize[find(a)]:
    nowSize[find(a)] += 1
    print("LADICA")
  else:
    print("SMECE")
