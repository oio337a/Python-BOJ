import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
out = []


def dfs(d, m):
    if d == m:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(n):
        print(overlap, li[i], 'hi')
        if overlap != li[i]:
            out.append(li[i])
            overlap = li[i]
            dfs(d+1, m)
            out.pop()


dfs(0, m)
