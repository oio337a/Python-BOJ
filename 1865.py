# 웜홀
# https://www.acmicpc.net/problem/1865
"""
헷갈렸던 부분은 시작점이 1번 지점이 아닐 수도 있다는 점이었는데,
임의의 한 지점에서 출발을 하므로 단순히 그래프상에
음의 사이클이 있는지 없는지 확인만 하면 되는 문제로 귀결됩니다.

따라서, 최단 경로를 기록할 리스트의 1번 인덱스에 0으로 초기화할 필요가 없으며,
벨만 포드 알고리즘에서 현재 노드의 값이 INF(무한대)인지 아닌지 확인하는 조건을 넣으면 안 됩니다.
"""

import sys
input = sys.stdin.readline

def bellman_ford():
    global is_possible

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for w, v in arr[j]: #
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
        s, e, t = map(int, input().split())  # 시작, 끝, 시간

        arr[s].append((t, e))
        arr[e].append((t, s))
    for _ in range(w):
        s, e, t = map(int, input().split())  # 시작, 끝, 시간

        arr[s].append((-t, e))

    is_possible = True
    bellman_ford()

    print("NO" if is_possible else "YES")