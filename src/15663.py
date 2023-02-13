import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
visited = [False] * n
out = []


def dfs(d, m):
    if d == m:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != li[i]:
            visited[i] = True
            out.append(li[i])
            overlap = li[i]
            dfs(d+1, m)
            visited[i] = False
            out.pop()


dfs(0, m)
