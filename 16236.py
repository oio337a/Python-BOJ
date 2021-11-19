from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 상어 위치 찾기
sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            sx, sy = i, j
            break

size = 2
move_cnt = 0
eat = 0
while 1:
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * n for _ in range(n)]
    flag = 1e9
    fish = []
    # 탐색
    while q:
        x, y, count = q.popleft()
        if count > flag:
            break
        # 4방향 탐색
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # 범위 밖 탐색 X
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 물고기의 크기가 크거나 방문했으면 탐색 X
            if arr[nx][ny] > size or visited[nx][ny]:
                continue
            #------------------------------------------#
            if arr[nx][ny] != 0 and arr[nx][ny] < size:
                fish.append((nx, ny, count + 1))
                flag = count
            visited[nx][ny] = True
            q.append((nx, ny, count + 1))
    # 상어 이동
    if len(fish) > 0:
        fish.sort()
        x, y, move = fish[0][0], fish[0][1], fish[0][2]
        move_cnt += move
        eat += 1
        arr[x][y] = 0
        # 상어 크기 증가
        if size == eat:
            size += 1
            eat = 0
        sx, sy = x, y
    else:
        break

print(move_cnt)
