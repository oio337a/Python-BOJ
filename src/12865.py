# https://www.acmicpc.net/problem/12865
# 배당 문제
# Knapsack Problem

import sys
input = sys.stdin.readline

'''
배낭에 담을 수 있는 무게의 최댓값이 정해져 있고,
일정 가치와 무게가 있는 짐들을 배낭에 넣을 때,
가치의 합이 최대가 되도록 짐을 고르는 방법을 찾는 알고리즘

dp table 을 만들고 점진적으로 물건을 선택했을 때 최댓값을 dp에 저장한다.
'''

# n, k = map(int, input().split())
# stuffs = [[0, 0]]
# knapsack = [[0 for _ in range((k + 1))] for _ in range(n + 1)]

# for _ in range(n):
# 	w, v = map(int, input().split())
# 	stuffs.append([w, v])

# # 냅색 문제 풀이
# for i in range(1, n + 1):
# 	for j in range(1, k + 1):
# 		weight = stuffs[i][0]
# 		value = stuffs[i][1]

# 		if j < weight:
# 			knapsack[i][j] = knapsack[i - 1][j]
# 		else:
# 			knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

# print(knapsack[n][k])



# 1차원 배열을 가지고 풀이
'''
1. 1차원 배열을 사용하면 K부터 1까지 루프를 돈다.
2. 배낭 용량이 K일 때, 들어간 물건들의 최대 가치합이 들어가게된다.
3. 물건을 넣기를 계속 시도하는 방식
'''

n, k = map(int, input().split())
stuffs = [[0, 0]]
dp = [0] * (k + 1)

for _ in range(n):
	w, v = map(int, input().split())
	stuffs.append([w, v])
	
for i in range(1, n + 1):
	for j in range(k, 0, -1):
		if stuffs[i][0] <= j:
			dp[j] = max(dp[j], dp[j - stuffs[i][0]] + stuffs[i][1])

print(dp[k])