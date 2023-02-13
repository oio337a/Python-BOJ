import sys
si = sys.stdin.readline


def row(x, y, color):
    # fixed x
    flag = False
    cnt = 0
    for j in range(1, 20):
        if j == y:
            flag = True
            cnt += 1
        elif graph[x][j] == color:
            cnt += 1
        elif flag and graph[x][j] != color:
            return cnt
        elif graph[x][j] != color:
            cnt = 0
    return cnt


def column(x, y, color):
    # fixed y
    flag = False
    cnt = 0
    for i in range(1, 20):
        if i == x:
            flag = True
            cnt += 1
        elif graph[i][y] == color:
            cnt += 1
        elif flag and graph[i][y] != color:
            return cnt
        elif graph[i][y] != color:
            cnt = 0
    return cnt


def gradient_1(x, y, color):  # 기울기가 1인 대각선
    min_ = min(x, y)
    diff = [x - min_, y - min_]

    flag = False
    cnt = 0

    for i in range(1, 20):
        nx, ny = i + diff[0], i + diff[1]
        if (0 < nx < 20) and (0 < ny < 20):
            if nx == x and ny == y:
                flag = True
                cnt += 1
            elif graph[nx][ny] == color:
                cnt += 1
            elif flag and graph[nx][ny] != color:
                return cnt
            elif graph[nx][ny] != color:
                cnt = 0
    return cnt


def gradient_m1(x, y, color):  # 기울기가 -1인 대각선
    sum_ = x + y

    flag = False
    cnt = 0

    for i in range(1, 20):
        nx, ny = i, sum_ - i
        if (0 < nx < 20) and (0 < ny < 20):
            if nx == x and ny == y:
                flag = True
                cnt += 1
            elif graph[nx][ny] == color:
                cnt += 1
            elif flag and graph[nx][ny] != color:
                return cnt
            elif graph[nx][ny] != color:
                cnt = 0
    return cnt


n = int(si())
graph = [[-1 for _ in range(20)] for _ in range(20)]
exit_flag = False

for cnt in range(1, n + 1):
    x, y = map(int, si().split())
    if exit_flag:
        continue

    color = cnt % 2  # 1: black, 0: white
    graph[x][y] = color

    # 가로 세로 대각선 탐색
    if row(x, y, color) == 5 or column(x, y, color) == 5 or gradient_1(x, y, color) == 5 or gradient_m1(x, y, color) == 5:
        print(cnt)
        exit_flag = True

if not exit_flag:
    print(-1)
