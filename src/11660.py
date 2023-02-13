import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

prefix = [[0] * (n+1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        prefix[i + 1][j + 1] = (prefix[i][j + 1] +
                                prefix[i + 1][j] - prefix[i][j]) + board[i][j]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix[x2][y2] - (prefix[x1 - 1][y2] +
          prefix[x2][y1 - 1] - prefix[x1 - 1][y1 - 1]))
