# 공항

import sys
input = sys.stdin.readline

def find(a):
  if a == disjoinSet[a]:
    return a

  disjoinSet[a] = find(disjoinSet[a])
  return disjoinSet[a]

G = int(input())
P = int(input())
li = [int(input()) for _ in range(P)]
cnt = 0
disjoinSet = [i for i in range(G+1)]

for plane in li:
  temp = find(plane)
  if temp == 0:
    break
  disjoinSet[temp] = disjoinSet[temp-1]
  cnt += 1

print(cnt)