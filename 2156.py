# import sys
# input = sys.stdin.readline

# """
# 3가지 선택
# 1. 먹기 2. 안먹기 3. 그냥 넘어가기

# 경우의 수
# < - 안먹기, 0 먹기 >

# 1. -00 - dp[i-1]
# 2. 0-0 0 dp[i-3] + podo[i-1] + podo[i]
# 3. 00- 0 dp[i-2] + podo[i]
# """
# n = int(input())
# podo = [0]

# for _ in range(n):
#     podo.append(int(input()))

# dp = [0, podo[1]]
# if n > 1:
#     dp.append(podo[1]+podo[2])
# for i in range(3, n+1):
#     dp.append(max(dp[i-1], dp[i-3] + podo[i-1] + podo[i], dp[i-2] + podo[i]))

# print(dp[n])

from sys import stdin
n = int(input())
t = [int(stdin.readline()) for _ in range(n)]
a, b, c = 0, 0, 0
for i in t:
    a, b, c = max(a, b, c), a+i, b+i
print(max(a, b, c))
