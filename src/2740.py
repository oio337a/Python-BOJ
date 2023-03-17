# https://www.acmicpc.net/problem/2740
# 행렬 곱셈

n, m = map(int, input().split())
matrix_1 = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
matrix_2 = [list(map(int, input().split())) for _ in range(m)]

result = [[0] * k for _ in range(n)]

for row in range(n):
	for col in range(k):
		e = 0
		for i in range(m):
			e += matrix_1[row][i] * matrix_2[i][col]
		result[row][col] = e

for line in result:
	print(*line)