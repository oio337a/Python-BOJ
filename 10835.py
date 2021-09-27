# bottom - up
import sys
input = sys.stdin.readline

n = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]  # n 보다 하나씩 더 큰 배열 생성

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if right[j] < left[i]:
            dp[i][j] = max(dp[i][j+1] + right[j], dp[i+1][j], dp[i+1][j+1])
        else:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
        print(dp, i)
print(dp[0][0])

"""
top - down

n = int(input())
left = [0] + list(map(int, input().split()))
right = [0] + list(map(int, input().split()))

dp = [[0 for i in range(n+1)] for i in range(n+1)]

for row in range(1, n+1):
    for col in range(1, n+1):
        if right[col] < left[row]:
            dp[row][col] = max(dp[row][col-1] + right[col], dp[row-1][col], dp[row-1][col-1])
        else:
            dp[row][col] = max(dp[row-1][col], dp[row-1][col-1])

print(dp[n][n])
"""
