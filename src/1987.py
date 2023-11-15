# 알파벳

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
alpha = set(board[0][0])
max_ = 1
d = [(1,0), (-1,0), (0,1), (0,-1)]

def DFS(x, y, cnt):
    global max_
    max_ = max(max_, cnt)
    
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] not in alpha:
                alpha.add(board[nx][ny])
                DFS(nx, ny, cnt+1)
                alpha.remove(board[nx][ny])
                
DFS(0,0,max_)
print(max_)