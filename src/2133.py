# """
# 1 = 1
# 2 = 3
# 3 = 4
# 4 = 6
# 5 = 7
# 6 = 9
# 7 = 10
# 8 = 12

# 홀수면 전에 수에 1더하기 짝수면 전에수에 2더하기
# """

# n = int(input())

# dp = [0]

# for i in range(1, n+1):
#     if i % 2 == 0:  # 짝수
#         dp.append(dp[i-1]+2)
#     else:  # 홀수
#         dp.append(dp[i-1]+1)

# print(dp[-1])

n = int(input())
dp = [0 for i in range(31)]  # n의 범위가 30까지
dp[2] = 3
for i in range(4, n+1):
    if i % 2 == 0:
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2

print(dp[n])


"""
n = 8

dp[8] = dp[6] * 3
"""
