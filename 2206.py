# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

move_cnt = 1
break_cnt = 0


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visit = [[0] * m for i in range(n)]
    visit[x][y] = 1
    while q:
        a, b = q.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0 and temp[x][y] != 0:
                temp[x][y] = 0
                visit[x][y] = 1
                q.append([x, y])
print(move_cnt)