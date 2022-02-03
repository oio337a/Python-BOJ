#호석이 두 마리 치킨
#https://www.acmicpc.net/problem/21278

import sys
from math import inf
input = sys.stdin.readline

n, m = map(int, input().split())
cost = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    cost[a-1][b-1] = 1
    cost[b-1][a-1] = 1

# 플로이드-와샨 알고리즘
for k in range(n):
    cost[k][k] = 0
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

max = 1_000_000_000
for i in range(n-1):
    for j in range(1, n):
        sum = 0
        for k in range(n):
            sum += min(cost[k][i], cost[k][j])
        if max > sum * 2:
            max = 2 * sum
            answer = [i + 1, j + 1, 2 * sum]
print(*answer)