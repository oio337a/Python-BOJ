# 링크와 스타트
# https://www.acmicpc.net/problem/15661

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]

d = 20*100
for i in combinations(range(n),n//2):

    s_team = [*i]
    l_team = list(set(range(n)) - set(s_team))

    s_score = 0
    l_score = 0
    for j in combinations(s_team,2):
        s_score += matrix[j[0]][j[1]] + matrix[j[1]][j[0]]

    for j in combinations(l_team,2):
        l_score += matrix[j[0]][j[1]] + matrix[j[1]][j[0]]

    sub = abs(s_score - l_score)

    if sub == 0:
        d = sub
        break

    elif d > sub:
        d = sub

print(d)