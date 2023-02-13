# # 링크와 스타트
# # https://www.acmicpc.net/problem/15661
#
# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
#
# n = int(input())
#
# matrix = [list(map(int,input().split())) for _ in range(n)]
#
# d = 20*100
# for i in combinations(range(n),n//2):
#
#     s_team = [*i]
#     l_team = list(set(range(n)) - set(s_team))
#
#     s_score = 0
#     l_score = 0
#     for j in combinations(s_team, 2):
#         s_score += matrix[j[0]][j[1]] + matrix[j[1]][j[0]]
#
#     for j in combinations(l_team, 2):
#         l_score += matrix[j[0]][j[1]] + matrix[j[1]][j[0]]
#
#     sub = abs(s_score - l_score)
#
#     if sub == 0:
#         d = sub
#         break
#
#     elif d > sub:
#         d = sub
#
# print(d)
# # !! 꼭 절반이 아니라 6명일시 2 4로 나눠질 수 있는 가능성을 열어둬야 한다.
#


import sys
input = sys.stdin.readline
M = int(sys.stdin.readline())
N = M // 2
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
row = [sum(i) for i in stat]
col = [sum(i) for i in zip(*stat)]

newstat = [i+j for i, j in zip(row, col)]
allstat = sum(newstat) // 2
newstat.sort()
c = [0]
for i in newstat[:N]:
    c.extend([i + j for j in c])
bot_up = [False] * (allstat + 1)
for i in c:
    bot_up[i] = True
for i in newstat[N:]:
    bot_up[i:] = [a or b for a, b in zip(bot_up[i:], bot_up)]
for i in range(allstat, -1, -1):
    if bot_up[i]:
        print(allstat - i)
        break