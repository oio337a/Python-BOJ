# https://www.acmicpc.net/problem/10830
# 행렬 제곱

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def mul(U, V):
	n = len(U)
	Z = [[0] * n for _ in range(n)]

	for row in range(n):
		for col in range(n):
			e = 0
			for i in range(n):
				e += U[row][i] * V[i][col]
				Z[row][col] = e % 1000
	return Z

def square(a, b):
	if b == 1:
		for x in range(len(a)):
			for y in range(len(a)):
				a[x][y] %= 1000
		return a
	temp = square(a, b//2)
	if b % 2:
		return mul(mul(temp, temp), a)
	else:
		return mul(temp, temp)

result = square(matrix, b)
for r in result:
	print(*r)