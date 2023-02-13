"""
- 최소 스패닝 트리 -

주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
"""

import sys
input = sys.stdin.readline

v, s = map(int, input().split())

edge = []
for _ in range(s):
    a, b, w = map(int, input().split())
    edge.append((w, a, b))

edge.sort(key=lambda x: x[0])

parent = list(range(v + 1))


def union(a, b):
    a = find(a)
    b = find(b)

    parent[a] = b


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


hap = 0
for w, s, e in edge:
    if find(s) != find(e):
        union(s, e)
        hap += w

print(hap)
