# 1로 만들기 2
# https://www.acmicpc.net/problem/12852

"""
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.
"""

import sys
input = sys.stdin.readline

'''
n = int(input())
cnt = 0
process = []

def dfs(n, d):
    global cnt
    if n <= 1:
        return
    process.append(n)
    cnt += 1
    if n % 3 == 0:
        dfs(n/3, d+1)
    elif n % 2 == 0:
        dfs(n/2, d+1)
    else:
        dfs(n-1, d+1)

dfs(n, 0)
print(cnt)

'''

# DP - bottom up #
# n 에서 1을 만드는 것이 아니라 1에서 n을 만드는 방법

n = int(input())
result = [[0, []] for _ in range(n+1)]
result[1][0] = 0 # 최솟값
result[1][1] = [1] # 경로를 담을 리스트

for i in range(2, n+1):
    # 1씩 더하기
    result[i][0] = result[i-1][0] + 1
    result[i][1] = result[i-1][1] + [i]

    # 3 나눠지면 더하기
    if i % 3 == 0 and result[i//3][0] + 1 < result[i][0]:
        result[i][0] = result[i//3][0] + 1
        result[i][1] = result[i//3][1] + [i]

    # 2 나눠지면 더하기
    if i % 2 == 0 and result[i//2][0] + 1 < result[i][0]:
        result[i][0] = result[i//2][0] + 1
        result[i][1] = result[i//2][1] + [i]
print(result[n][0])
print(*result[::-1][0][1][::-1])