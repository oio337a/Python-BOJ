# Haybale Feast

import sys
input = sys.stdin.readline

def find(x):
  if x == disjoinSet[x]:
    return x
  disjoinSet[x] = find(disjoinSet[x])
  return disjoinSet[x]

def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    li[a] += li[b]
    li[b] = a

n, m = map(int, input().split())
p = []
fs = []

disjoinSet = [i for i in range(n)]
check = [i for i in range(n)]

for i in range(n):
  check[i] = True
  if disjoinSet[i] > 0