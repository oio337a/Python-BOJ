import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
visited = [False] * n
out = []


def dfs(d, idx, m):
    if d == m:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(idx, n):
        if not visited[i] and overlap != li[i]:
            visited[i] = True
            overlap = li[i]
            out.append(li[i])
            dfs(d+1, i+1,  m)
            visited[i] = False
            out.pop()


dfs(0, 0, m)
