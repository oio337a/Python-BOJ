import sys
input = sys.stdin.readline

"""
dp[N명의 고객을 유치하는데 드는 비용] = 
min(dp[N명의 고객을 유치하는데 드는 비용],
dp[N명의 고객을 유치하는데 드는 비용 - 현재 방문한 도시의 유치 가능한 인원수) + cost)
"""
c, n = map(int, input().split())
ad = [list(map(int, input().split())) for _ in range(n)]

dp = [0] + [sys.maxsize] * (c + 100)
for cost, customer in ad:
    for cur_customer in range(customer, c + 101):
        dp[cur_customer] = min(
            dp[cur_customer], dp[cur_customer - customer] + cost)

print(min(dp[c:c + 101]))
