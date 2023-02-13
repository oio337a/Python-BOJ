# 저울
# https://www.acmicpc.net/problem/10159

# 플로이드-와샬 알고리즘
# i에서 j로 이동 가능하고 j에서 i로 이동 가능 하면 대소비교 가능
# 그렇지 않다면 cnt 증가

import sys
input = sys.stdin.readline

INF = sys.maxsize

n = int(input()) # 5 <= n <= 100
m = int(input()) # 0 <= m <= 2,000
a = [[0]*n for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    a[x-1][y-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][k] and a[k][j]:
                a[i][j] = 1

for i in range(n):
    cnt = 0
    for j in range(n):
        if not a[i][j] and not a[j][i]:
            cnt += 1
    print(cnt-1)