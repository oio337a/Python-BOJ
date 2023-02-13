n, m = map(int, input().split())
out = []


def dfs(start):
    if len(out) == m:
        print(' '.join(map(str, out)))
        return
    for i in range(start, n+1):
        if i not in out:
            out.append(i)
            dfs(i+1)
            out.pop()


dfs(1)
