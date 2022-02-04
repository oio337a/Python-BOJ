#
# # BFS 벽을 최소 몇 개 부수어야 하는가?
# from collections import deque
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# m,n = map(int, input().split())
# arr = [ list(map(int, input())) for _ in range(n)]
# dist = [[-1] * m for _ in range(n)]  # 가중치
#
# q = deque()
# q.append((0,0))
# dist[0][0] = 0
# while q:
#     x,y = q.popleft()
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < n and 0 <= ny < m:
#             if dist[nx][ny] == -1:
#                 if arr[nx][ny] == 0:
#                     dist[nx][ny] = dist[x][y]
#                     q.appendleft((nx, ny))
#                 else:
#                     dist[nx][ny] = dist[x][y] + 1
#                     q.append((nx, ny))
# print(dist[n-1][m-1])


import sys
from heapq import heappush, heappop
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
def makeMazeEx():
    tr, tc = 0, 0
    for i in range(R * C):
        maze_ex[i] = (tr, tc)
        tc = tc + 1 if tc < R - 1 else 0
        tr = tr + 1 if tc == R - 1 else tr
    cnt=0
    for i in range(R):
        for j in range(C):
            maze_num[i][j]=cnt
            cnt+=1
def daik():
    hq = []
    for n in range(R*C):
        heappush(hq, (0,n)) if n == 0 else heappush(hq, (INF,n))
    while hq:
        weight, a = heappop(hq)
        if dist[a] < weight:
            continue
        for ww, b in maze_two[a]:
            if dist[b] > dist[a] + ww:
                dist[b] = ww + weight
                heappush(hq,(dist[b], b))
if __name__ == "__main__":
    C,R=MIS()
    maze=[[*map(int, list(In()))] for i in range(R)]
    maze_ex=[0]*(R*C)
    maze_num=[[0]*C for i in range(R)]
    makeMazeEx()
    maze_two=[[] for i in range(R*C)]
    for r in range(R):
        for c in range(C):
            a=maze_num[r][c]
            for nr, nc in [(r+1,c), (r,c+1)]:
                if 0<=nr<R and 0<=nc<C:
                    b=maze_num[nr][nc]
                    w = 1 if maze[nr][nc] == 1 else 0
                    maze_two[a].append((w, b))
    INF = float("inf")
    dist = [INF for n in range(R*C)]
    dist[0]=0
    daik()
    print(dist[C*R-1])