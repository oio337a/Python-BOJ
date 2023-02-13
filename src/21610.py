# 마법사 상어와 비바라기
# https://www.acmicpc.net/problem/21610

"""
비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다.

"""
import sys
input = sys.stdin.readline

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = []
for _ in range(m):
    a, b = map(int, input().split())
    moves.append([a-1, b])

clouds = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]

for i in range(m): # 이동
    ####### 1번 #######
    move = moves[i]
    next_clouds = []
    for cloud in clouds:
        x = cloud[0]
        y = cloud[1]
        d = move[0]
        s = move[1]
        nx = (n + x + dx[d] * s) % n
        ny = (n + y + dy[d] * s) % n
        next_clouds.append([nx, ny])

    ####### 2번 ####### 물 증가
    visited = [[False] * n for _ in range(n)]
    for cloud in next_clouds:
        x = cloud[0]
        y = cloud[1]
        board[x][y] += 1
        visited[x][y] = True

    ####### 3번 #######
    clouds = []

    ####### 4번 ####### 물복사버그
    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]
    for cloud in next_clouds:
        x = cloud[0]
        y = cloud[1]
        count = 0
        for i in range(4):
            nx = x + cx[i]
            ny = y + cy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] >= 1:
                count += 1
        board[x][y] += count

    ####### 5번 ####### 구름 생성 (-2)
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and visited[i][j] == False:
                board[i][j] -= 2
                clouds.append([i, j])
ans = 0
for i in range(n):
    ans += sum(board[i])

print(ans)
