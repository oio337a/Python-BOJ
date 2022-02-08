# 벽 부수고 이동하기 2
# https://www.acmicpc.net/problem/14442

from collections import deque
INF = int(1e9)
N, M, K = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))
visited = [[[INF]*(K+1) for _ in range(M)] for _ in range(N)]
xpos = [1, -1, 0, 0]
ypos = [0, 0, 1, -1]

def bfs(stx, sty):
    q = deque()
    q.append((stx, sty, 0))
    visited[sty][stx][0] = 1
    while q:
        tmpx, tmpy, broken = q.popleft()
        if tmpx == M-1 and tmpy == N-1:
            print(visited[N-1][M-1][broken])
            return
        for i in range(4):
            xx = tmpx + xpos[i]
            yy = tmpy + ypos[i]
            if 0 <= xx < M and 0 <= yy < N:
                if graph[yy][xx] == 0 and visited[yy][xx][broken] == INF:
                    visited[yy][xx][broken] = visited[tmpy][tmpx][broken] + 1
                    q.append((xx, yy, broken))
                elif graph[yy][xx] == 1 and broken < K and visited[yy][xx][broken+1] == INF:
                    visited[yy][xx][broken+1] = visited[tmpy][tmpx][broken] + 1
                    q.append((xx, yy, broken+1))
    print(-1)
bfs(0, 0)