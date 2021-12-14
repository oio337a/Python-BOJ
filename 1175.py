# 참고 사이트
# https://yabmoons.tistory.com/310

import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    visited[x][y][-1][0][0] = 1
    queue = deque([[x, y, -1, 0, 0, 0]])

    while queue:
        x, y, dxdy, c, d, cnt = queue.popleft()
        if c == d == 1:
            return cnt

        for i in range(4):
            if dxdy == i:
                continue

            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if graph[nx][ny] == 'C' and not visited[nx][ny][i][1][d]:
                    visited[nx][ny][i][1][d] = 1
                    queue.append([nx, ny, i, 1, d, cnt + 1])

                elif graph[nx][ny] == 'D' and not visited[nx][ny][i][c][1]:
                    visited[nx][ny][i][c][1] = 1
                    queue.append([nx, ny, i, c, 1, cnt + 1])

                elif graph[nx][ny] != '#' and not visited[nx][ny][i][c][d]:  # '.' or 'S'
                    visited[nx][ny][i][c][d] = 1
                    queue.append([nx, ny, i, c, d, cnt + 1])

    return -1


n, m = map(int, si().split())
graph = [list(map(str, si().rstrip())) for _ in range(n)]
# x좌표 n개, y좌표 m개, 4방향, C 방문여부 2가지, D 방문여부 2가지
visited = [[[[[0 for _ in range(2)] for _ in range(2)]
             for _ in range(4)] for _ in range(m)] for _ in range(n)]

flag = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            sx, sy = i, j

        elif not flag and graph[i][j] == 'C':
            graph[i][j] = 'D'
            flag = True

print(bfs(sx, sy))
