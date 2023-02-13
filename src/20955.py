# 민서의 응급 수술
# https://www.acmicpc.net/problem/20955

import sys
input = sys.stdin.readline

# 초기에 각 노드는 자기 자신을 루트 노드로 가지고 있다.

# Find를 통해 반환 되는 값은 그 집합의 대푯값(해당 트리(집합)의 루트노드)이다.
def find(u):
    if (u == parent[u]):
        return u
    parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    u = find(u)
    v = find(v)

    if (u == v):
        return
    if (level[u] > level[v]):
        parent[u] = v
        level[u] += level[v]
    else:
        parent[v] = u
        level[v] += level[u]

n, m = map(int, input().split())

parent = [0] + [i for i in range(1, n + 1)]
level = [0] + [1] * n

for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

cnt = 0
if n - m <= 0:
    cnt = m - n + 1
print(len(set(parent)) - 2 + cnt)


