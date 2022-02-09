# 양팔저울
# https://www.acmicpc.net/problem/2629
#
# import sys
# from itertools import combinations
# input = sys.stdin.readline
#
# chu_cnt = int(input())
# chu = [0] + list(map(int, input().split()))
#
# check_cnt = int(input())
# marble = list(map(int, input().split()))
#
# answer = []
# for j in range(1, chu_cnt + 1):
#     for i in set(combinations(chu, j)):
#         answer.append(abs(sum(i) - sum(set(chu) - set(i))))
#
# answer = set(answer)
#
# for i in marble:
#     if i in answer:
#         print('Y', end=' ')
#     else:
#         print('N', end=' ')

# print(*answer)

import sys
input = sys.stdin.readline

n = int(input())
weight = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
possible = []
answer = [[0 for _ in range(15001)] for _ in range(n + 1)]


def scale(weigth, n, now, left, right):
    new = abs(left - right)
    if new not in possible:
        possible.append(new)
    if now == n:
        return 0
    if answer[now][new] == 0:
        scale(weigth, n, now + 1, left + weigth[now], right)
        scale(weigth, n, now + 1, left, right + weigth[now])
        scale(weigth, n, now + 1, left, right)
        answer[now][new] = 1

scale(weight, n, 0, 0, 0)
for i in check:
    if i in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')


