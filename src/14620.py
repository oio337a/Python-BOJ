import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
visited = [[False] * n for _ in range(n)]
answer = 987654321

flower = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # 현위치. 상하좌우

# 꽃을 죽이지 않고 놓을 수 있는지 확인


def check(y, x):
    global n
    for dy, dx in flower:
        ny = y + dy
        nx = x + dx
        if 0 > ny or ny > n-1 or 0 > nx or nx > n-1 or visited[ny][nx]:
            return False
    return True

# 꽃 비용 계산


def calculate(y, x):
    result = 0
    for dy, dx in flower:
        ny = y + dy
        nx = x + dx
        result += board[ny][nx]
    return result

# 3개의 꽃 고르기
# 서로 겹치치 않게
# 보드의 끝이면 다음 줄 넘어가기


def dfs(x, cost, cnt):
    global answer
    if cnt == 3:
        answer = min(answer, cost)
        return
    for i in range(x, n):
        for j in range(1, n):
            if check(i, j):
                visited[i][j] = True
                for dy, dx in flower:
                    visited[i+dy][j+dx] = True
                dfs(i, cost + calculate(i, j), cnt+1)
                visited[i][j] = False
                for dy, dx in flower:
                    visited[i+dy][j+dx] = False


dfs(1, 0, 0)
print(answer)
