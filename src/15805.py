# 트리 나라 관광 가이드
# https://www.acmicpc.net/problem/15805

import sys, copy
input = sys.stdin.readline

# n = int(input())
# li = list(map(int, input().split()))
#
# check_li = [-1 for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if li[j] == i and j != n - 1:
#             if check_li[li[j + 1]] == -1:
#                 check_li[li[j + 1]] = i
#
# print(-1, end=' ')
# print(*check_li[1:max(li)+1])

n = int(input())
li = list(map(int, input().split()))
answer = [False for _ in range(200_000)]

s = [False for _ in range(200_000)]
s[li[0]] = True

answer[li[0]] = -1

for i in range(n):
    if s[li[i]] == True:
        continue
    answer[li[i]] = li[i - 1]
    s[li[i]] = True

max_node = max(li) + 1
print(max_node)
print(*answer[0:max_node])