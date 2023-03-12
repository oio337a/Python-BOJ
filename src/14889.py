# https://www.acmicpc.net/problem/14889
# 스타트와 링크

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
members = [list(map(int, input().split())) for _ in range(n)]

comb = list(combinations(range(n), int(n/2)))

team_1 = comb[:len(comb)//2]
team_2 = comb[len(comb)//2 : len(comb)][::-1]

result = 1e9
for i in range(len(team_1)):
    temp_1 = 0
    temp_2 = 0
    for j in range(len(team_1[0])):
        for k in range(j + 1, len(team_1[0])):
          temp_1 += members[team_1[i][j]][team_1[i][k]]
          temp_1 += members[team_1[i][k]][team_1[i][j]]
          temp_2 += members[team_2[i][j]][team_2[i][k]]
          temp_2 += members[team_2[i][k]][team_2[i][j]]
    if abs(temp_1 - temp_2) == 0:
      result = 0
      break
    if result > abs(temp_1 - temp_2):
        result = abs(temp_1 - temp_2)
print(result)


# --------------------------------- #
# 타인의 코드
import sys
from itertools import combinations as cb
N = int(sys.stdin.readline()) // 2
M = 2*N
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
allstat = sum(newstat) // 2
mins = 65535
for l in cb(newstat[:-1], N):
    mins = min(mins, abs(allstat - sum(l)))
print(mins)