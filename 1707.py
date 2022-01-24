# 이분 그래프
# https://www.acmicpc.net/problem/1707

import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    table = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    color = [0] * (v + 1)
    FLAG = True

    for _ in range(e):
        v1, v2 = map(int, input().split())
        table[v1].append(v2)
        table[v2].append(v1)

    def check(vertex):
        global FLAG, visited, color
        color[vertex] = 1
        queue = deque([vertex])
        while queue and FLAG:
            s = queue.popleft()
            c = color[s]

            if visited[s]:
                continue

            visited[s] = 1
            for link in table[s]:
                if visited[link] and color[s] == color[link]:
                    FLAG = False
                    break
                elif not visited[link]:
                    color[link] = -c
                    queue.append(link)

    for i in range(1, v+1):
        if not FLAG:
            break
        if not visited[i]:
            check(i)

    if FLAG: sys.stdout.write("YES\n")
    else: sys.stdout.write("NO\n")
