"""
1 = 1
2 = 1 + 1
    2
3 = 1 + 1 + 1
    1 + 2
4 = 1 + 1 + 1 + 1
    1 + 1 + 2
    2 + 2
    4
5 = 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 2
    1 + 2 + 2
    1 + 4
6 = 1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 2 + 2
    1 + 1 + 4
    2 + 2 + 2    
    2 + 4

홀수는 전의 개수와 같고 2의 배수는 2개씩 늘어남
"""
# n = int(input())
# li = []
# num = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         num += 2
# if n == 1:
#     num = 1
# print(num)

# # ====================================
# n = int(input())

# dp = [0] * 1000001
# dp[0] = 1

# for i in range(1, n+1):
#     dp[i] = (dp[i-1]+(i & 1 == 0 and dp[i//2])) % 1000000000

# print(dp)

# # ====================================


def solution(N):
    nums = [2 ** x for x in range(21)]
    dp = [0] * (N + 1)
    dp[0] = 1
    for num in nums:
        if num <= N:
            for j in range(num, N + 1):
                dp[j] += dp[j - num]
    print(dp[-1] % 1000000000)


if __name__ == "__main__":
    N0 = int(input())
    solution(N0)
