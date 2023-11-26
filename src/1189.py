# 컴백홈

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r, c, k = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
visit = [[0]*c for _ in range(r)]
res = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def backtrack(y, x, depth):
    global res
    if depth == k and y == 0 and x == c - 1:
        res += 1
    else:
        visit[y][x] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and not visit[ny][nx]:
                if board[ny][nx] == '.':
                    visit[ny][nx] = 1
                    backtrack(ny, nx, depth + 1)
                    visit[ny][nx] = 0
            
            

backtrack(r - 1, 0, 1)
print(res)