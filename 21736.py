import sys
sys.setrecursionlimit(1234567)
input = sys.stdin.readline

n, m = map(int, input().split())
a, b = -1, -1
g = []
for i in range(n):
    t = list(input().rstrip())
    if 'I' in t:
        a, b = i, t.index('I')
    g.append(t)

board = [[0] * m for i in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
cnt = 0


def dfs(y, x):
    global cnt
    board[y][x] = 1
    for i in range(4):
        ty, tx = y + dy[i], x + dx[i]
        if not (0 <= ty < n and 0 <= tx < m):
            continue
        if board[ty][tx]:
            continue
        if g[ty][tx] == 'X':
            continue
        if g[ty][tx] == 'P':
            cnt += 1
        dfs(ty, tx)


dfs(a, b)
print(cnt if cnt else "TT")
