from collections import deque
graph = []
for i in range(8):
    tmp = list(input())
    graph.append(tmp)
visited = [[-1]*8 for _ in range(8)]
# W 좌표 저장
wx = []
wy = []
for y in range(8):
    for x in range(8):
        if graph[y][x] == 'W':
            wx.append(x)
            wy.append(y)


def continuous(nowx, nowy, gapx, gapy):
    cnt = 2
    tmpx = nowx
    tmpy = nowy
    while True:
        tmpx = tmpx+gapx
        tmpy = tmpy+gapy
        if 0 <= tmpx < 8 and 0 <= tmpy < 8:
            if graph[tmpy][tmpx] == 'W':
                cnt += 1
            if graph[tmpy][tmpx] == '.':
                cnt = 0
                return cnt
            if graph[tmpy][tmpx] == 'B':
                return cnt
        else:
            return 0
# 지정한 위치에 검은 돌을 놓을 경우 몇개?


def getCount(x, y):
    global graph
    global wx
    global wy
    gx = [0, 0, 1, -1, 1, -1, 1, -1]
    gy = [1, -1, 0, 0, -1, 1, 1, -1]
    graph[y][x] = 'B'

    # W중에 B로 바뀔애를 탐색
    result = 0
    for i in range(8):
        bx = x+gx[i]
        by = y+gy[i]
        if 0 <= bx < 8 and 0 <= by < 8 and graph[by][bx] == 'W':
            tmpx = bx+(bx-x)
            tmpy = by+(by-y)
            if 0 <= tmpx < 8 and 0 <= tmpy < 8:
                if graph[tmpy][tmpx] == 'B':
                    result += 1
                if graph[tmpy][tmpx] == 'W':
                    #print(tmpx, tmpy, bx-x, by-y)
                    result += continuous(tmpx, tmpy, bx-x, by-y)

    graph[y][x] = '.'
    visited[y][x] = result
    # print(result)
    return result


# W 좌표가 있는 곳의 상화좌우대각선의 검은돌을 놓을 경우
xpos = [0, 0, 1, -1, 1, -1, 1, -1]
ypos = [1, -1, 0, 0, -1, 1, 1, -1]
maxresult = 0
for i in range(len(wx)):
    for k in range(8):
        tmpx = wx[i]+xpos[k]
        tmpy = wy[i]+ypos[k]
        if 0 <= tmpx < 8 and 0 <= tmpy < 8 and graph[tmpy][tmpx] == '.' and visited[tmpy][tmpx] == -1:
            cnt = getCount(tmpx, tmpy)
            maxresult = max(cnt, maxresult)
            #print(tmpx, tmpy, cnt)
print(maxresult)
