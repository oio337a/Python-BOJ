# 웜홀
# https://www.acmicpc.net/problem/1865


import sys
input = sys.stdin.readline

def bellman_ford():
    global is_possible

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for w, v in arr[j]:
                if dist[v] > w + dist[j]:
                    dist[v] = w + dist[j]
                    if i == n:
                        is_possible = False


tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split()) # 노드, 간선, 웜홀 각각의 개수

    INF = int(1e9)
    dist = [INF for _ in range(n + 1)]

    arr = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, t = map(int, input().split())

        arr[s].append((t, e))
        arr[e].append((t, s))
    for _ in range(w):
        s, e, t = map(int, input().split())

        arr[s].append((-t, e))

    is_possible = True
    bellman_ford()

    print("NO" if is_possible else "YES")