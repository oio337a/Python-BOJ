dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs():
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            que.append([nx, ny])