# https://www.acmicpc.net/problem/3584
# 가장 가까운 공통 조상
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    parent = [0 for _ in range(N + 1)]
    for _ in range(N - 1):
        p, c = map(int, input().split())
        parent[c] = p
    a, b = map(int, input().split())

    a_parent = [a]
    b_parent = [b]

    while parent[a]:
        a_parent.append(parent[a])
        a = parent[a]
    while parent[b]:
        b_parent.append(parent[b])
        b = parent[b]
    a_depth = len(a_parent) - 1
    b_depth = len(b_parent) - 1
    
    while a_parent[a_depth] == b_parent[b_depth]:
        a_depth -= 1
        b_depth -= 1
    print(a_parent[a_depth + 1])
  