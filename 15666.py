import sys
from typing import overload
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
out = []


def dfs(d, idx):
    if d == m:
        print(' '.join(map(str, out)))
        return
    overload = 0
    for i in range(idx, n):
        if overload != li[i]:
            out.append(li[i])
            overload = li[i]

            dfs(d+1, i)
            out.pop()


dfs(0, 0)
