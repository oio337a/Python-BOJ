# 조합 사용하여 해결

# import sys
# from itertools import combinations

# input = sys.stdin.readline

# while True:
#     li = list(map(int, input().split()))
#     if li[0] == 0:
#         break
#     comb = list(combinations(li[1:], 6))
#     for i in comb:
#         print(*i)
#     print()


# DFS 사용
import sys

input = sys.stdin.readline
dp = [0 for _ in range(6)]


def DFS(start, depth):
    if depth == 6:
        print(*dp)
        return
    for i in range(start, len(li)):
        dp[depth] = li[i]
        DFS(i + 1, depth + 1)


while True:
    li = list(map(int, input().split()))
    if li[0] == 0:
        break

    del li[0]
    DFS(0, 0)
    print()
